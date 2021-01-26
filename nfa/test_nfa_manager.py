import os

##########
# Constants
##########

TESTS_PATH = "C:/git/lexer/nfa/test_cases/"
PROGRAM_PATH = "C:\\git\\nfa\\main.py"
INPUT_FILES_PATH = "test.a"
OUTPUT_FILES_PATH = "test.b"

UPPER_TIME_BOUND = "10" # in seconds
TEST_COUNT = 1
PASSED_TESTS = 0


##########
# Subroutines
##########


def get_number_of_tests():
    import os

    list = os.listdir(TESTS_PATH)  # dir is your directory path
    return len(list)


if __name__ == '__main__':

    num_of_tests = get_number_of_tests()

    # TODO break option if time is above max time
    import datetime

    biggest_execution_time_seconds = 0
    biggest_execution_time_miliseconds = 0

    for file in os.listdir(TESTS_PATH):

        start_time = datetime.datetime.now()

        program_output_lines = os.popen("py toy_math_operations.py < \"" + TESTS_PATH +
                                        file + "/" + INPUT_FILES_PATH +
                                        "\"").read().split("\n")
        end_time = datetime.datetime.now()
        execution_time = end_time - start_time
        time_raw = str(execution_time).split(".")
        miliseconds = int(time_raw[1])

        seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], time_raw[0].split(":")))

        if seconds > biggest_execution_time_seconds \
            or (seconds == biggest_execution_time_seconds and miliseconds > biggest_execution_time_miliseconds):
            biggest_execution_time_seconds = seconds
            biggest_execution_time_miliseconds = miliseconds

        correct_output_lines = open(TESTS_PATH + file + "/" + OUTPUT_FILES_PATH,
                                    "resources").read().split("\n")

        if program_output_lines == correct_output_lines:
            print("\33[31mtest " + str(TEST_COUNT).rjust(len(str(num_of_tests))) +
                  " =\033[0m \x1b[3;34;30m correct! \x1b[0m")

            PASSED_TESTS += 1
        else:
            print("\33[31mtest " + str(TEST_COUNT).rjust(
                len(str(num_of_tests))) + " =\033[0m \33[34mfalse\033[0m")

            print("   program's output " + str(program_output_lines))
            print("   correct output   " + str(correct_output_lines))

            # max width of lines in correct_output_line
            max_length = 0
            for correct_output_line in correct_output_lines:
                if len(correct_output_line) > max_length:
                    max_length = len(correct_output_line)

            # num of lines in correct output file
            with open(TESTS_PATH + file + "/" + INPUT_FILES_PATH) as f:
                for i, l in enumerate(f):
                    pass
            num_of_lines = i + 1

            print("\n" + str("    ").rjust(2) + "left is correct")
            counter = 0
            for correct_output_line in correct_output_lines:

                temp_len = max_length - len(correct_output_line)
                try:
                    print(str(counter).rjust(2) + "  " + correct_output_line +
                          (temp_len + 2) * " " + "| " + program_output_lines[counter])
                    if correct_output_line != program_output_lines[counter]:
                        print("error occured in previous line \nrest of output is not displayed")
                        break
                except:
                    print("error")
                    break
                counter += 1

            print()
        TEST_COUNT += 1

    print("\nanalysis results")
    print("tests passed: " + str(PASSED_TESTS) + " / " + str(TEST_COUNT - 1))
    print("longest execution time: " + str(biggest_execution_time_seconds) + "."
          + str(biggest_execution_time_miliseconds) + " [s]")
