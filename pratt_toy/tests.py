import os
import subprocess
import unittest

import main

class TestMain(unittest.TestCase):
    def execute(self, language="python", arguments=""):
        """Execute a single solution and return the output
        """

        # Max allowed 2 minutes
        max_time = 120  # seconds
        # Cache current directory
        curdir = os.getcwd()
        # Move to solution directory
        # os.chdir(path_to_solution)

        # Determine run command based on language
        if language == 'python':
            ex_cmd = 'python solution.py'
            command = ex_cmd + ' ' + arguments

        elif language == 'java':
            ex_cmd = 'java -cp target/classes ui.Solution' if os.name != 'nt' \
                else 'java -cp target/classes -Dfile.encoding=UTF-8 ui.Solution'
            command = ex_cmd + ' ' + arguments

        elif language == 'cpp':
            ex_cmd = './solution'
            command = ex_cmd + ' ' + arguments

        print(f"Running: {command}")
        # print("ok")

        try:
            result = subprocess.check_output(command.split(),
                                             stderr=subprocess.STDOUT,
                                             timeout=max_time,
                                             env={**os.environ.copy(),
                                                  'PYTHONUTF8': '1'})
        except subprocess.CalledProcessError as e:
            os.chdir(curdir)
            error_message = e.output.decode("utf-8")
            return "ERR_EXECUTE", error_message, command
        except subprocess.TimeoutExpired as e:
            os.chdir(curdir)
            return "ERR_TIMEOUT", None, command

        result = result.decode("utf-8").strip()

        os.chdir(curdir)
        return CODE_OK, result, command

    def get_output(self, expression):
        print(self.execute())
        return "a"

    def test_a(self):
        self.assertEqual("a", "a")

    def test_b(self):
        self.assertEqual("a", "b")

    def test_c(self):
        self.assertEqual(self.get_output("sin x + 1 )"), ['sin', 'err (', ['+', 'x', '1'], ')'])


if __name__ == '__main__':
    unittest.main()
