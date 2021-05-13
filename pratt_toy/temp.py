import os
import subprocess


def load():

    t_list = []
    a = ""
    for line in open("temp.txt").read().split("\n"):
        line = line.strip()
        print(line)
        if line.startswith("test"):
            t_list.append(a)
            a = line
        else:
            a += line

    [print(i) for i in t_list]
    print()

    for t in t_list:
        if not t:
            continue

        # print(t)
        t = t[4:]
        # print(t)
        t = eval(t)
        print(t)
        print(t[0])
        print(t[1])

        print(f"self.assertEqual(get_output(\"{t[0]}\", {t[1]})")

        print()
        # t = t.split(", ")
        # print(t)
        # print(f"self.assertEqual(get_output{t[0]})")
        # print("self.assertEqual(get_output" + t[4:])

def execute(arguments=""):
    """code copied from https://github.com/zoranmedic/autograder"""



    curdir = os.getcwd()
    max_time = 10  # seconds
    # print(os.environ)
    # [print(i) for i in os.environ]
    # ex_cmd = 'python main.py'
    ex_cmd = 'py main.py'
    command = ex_cmd + ' ' + arguments
    # os.chdir("/")

    print(f"Running: {command}")

    try:
        #
        # result = subprocess.check_output(command.split(),

        result = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         timeout=max_time,
                                         env={**os.environ.copy(),
                                              'PYTHONUTF8': '1'}
                                         )

    except subprocess.CalledProcessError as e:
        os.chdir(curdir)
        error_message = e.output.decode("utf-8")
        return "ERR_EXECUTE", error_message, command

    except subprocess.TimeoutExpired:
        os.chdir(curdir)
        return "ERR_TIMEOUT", None, command

    os.chdir(curdir)

    result = result.decode("utf-8").strip()

    return result


if __name__ == '__main__':
    a = execute("\"1 + 2\"")
    print(a)
