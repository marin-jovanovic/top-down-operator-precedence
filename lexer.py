from nfa.main import driver

MAX_EATER_NUMBER = -1
MAX_EATER_POINTER = -1
SOURCE_CODE = "".join([i for i in open("test_cases/2/nadji_a2.in").readlines()])
CURRENT_STATE = "S_poc"
OUTPUT = list()
LINE_NUMBER = 1


def f_0(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_poc', 'a', ['A']]
    if CURRENT_STATE == "S_poc":
        print(0)
        t_in = [
            str(SOURCE_CODE),
            ['S_1'],
            "S_0",
            ['S_0', 'a', 'S_1']
        ]
        t_0, is_accepted = driver(t_in)

        if may_i_eat:
            OUTPUT.append("A " + str(LINE_NUMBER) + " " + SOURCE_CODE[:MAX_EATER_NUMBER])
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        elif is_accepted:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 0

        return t_0.count("|")


def f_1(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_poc', '\\n', ['-', 'NOVI_REDAK']]
    if CURRENT_STATE == "S_poc":
        print(1)
        t_in = [
            str(SOURCE_CODE),
            ['S_1'],
            "S_0",
            ['S_0', '\n', 'S_1']
        ]
        t_0, is_accepted = driver(t_in)

        if may_i_eat:
            LINE_NUMBER += 1
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        elif is_accepted:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 1

        return t_0.count("|")


if __name__ == '__main__':
    TTL = 15

    while TTL != 0:
        TTL -= 1
        MAX_EATER_NUMBER -= 1
        MAX_EATER_POINTER = -1

        f_0()
        f_1()

        print("MAX_EATER_NUMBER", MAX_EATER_NUMBER)
        if MAX_EATER_POINTER == 0:
            f_0(True)
        elif MAX_EATER_POINTER == 1:
            f_1(True)
        print(100 * "*")
        print(list(SOURCE_CODE))
        print(SOURCE_CODE)
        [print(i) for i in OUTPUT]
        print(CURRENT_STATE)
        if MAX_EATER_NUMBER < 0:
            SOURCE_CODE = SOURCE_CODE[1:]
    # file = [i[:-1] for i in open("lexer.py").readlines()]
    # [print("lexer_code.append(\"" + str(i) + "\")") for i in file]
    pass
