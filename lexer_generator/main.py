import re

LAN_PATH = "test_cases/0/minusLang.lan"
IN_PATH = "test_cases/0/minusLang.in"

LAN_PATH = "test_cases/1/nadji_a1.lan"
IN_PATH = "test_cases/1/nadji_a1.in"
#
LAN_PATH = "test_cases/2/nadji_a2.lan"
IN_PATH = "test_cases/2/nadji_a2.in"
#
LAN_PATH = "test_cases/3/simplePpjLang.lan"
IN_PATH = "test_cases/3/simplePpjLang.in"
#
LAN_PATH = "test_cases/4/svaki_drugi_a1.lan"
IN_PATH = "test_cases/4/svaki_drugi_a1.in"
#
LAN_PATH = "test_cases/5/svaki_drugi_a2.lan"
IN_PATH = "test_cases/5/svaki_drugi_a2.in"

LAN_PATH = "test_cases/java/language.lan"
IN_PATH = "test_cases/java/java.in"

LANGUAGE = [line[:-1] for line in open(LAN_PATH).readlines()]
TOKENS = "".join([line for line in open(IN_PATH).readlines()])

REGEX = list()
RULES = list()
INITIAL_STATE = list()
STATES = list()


# citanje iz .lan datoteke
def load_language():
    global REGEX, RULES, INITIAL_STATE

    state = 0
    for line in open(LAN_PATH).readlines():
        line = str(line[:-1])

        if state == 0:

            if line.startswith("%X "):
                INITIAL_STATE = (line.split(" "))[1]
                state = 1

            else:
                try:
                    s = re.search('{(.+?)}', line).group(1)
                except AttributeError:
                    print("error while parsing regex")
                    import sys
                    sys.exit()

                REGEX.append(["{" + s + "}", line[line.find("}") + 2:]])

        elif state == 1:
            try:
                new_regex = [REGEX[0]]
            except IndexError:
                new_regex = []

            for raw in REGEX[1:]:
                right = str(raw[1])

                for j, r in enumerate(new_regex):
                    if right.__contains__(str(r[0])):
                        right = right.replace(r[0], "(" + str(r[1]) + ")")

                new_regex.append([str(raw[0]), right])

            REGEX = new_regex

            state = 2

        else:
            RULES.append(line)


# extractanje da sve bude u rules
def restructure_rules():
    global RULES
    # put @RULES in list
    new_rules_list = list()
    # starting state
    state_0 = 0
    arg_0 = ""
    arg_1 = ""
    arg_2 = list()
    i_0 = -1
    while True:
        i_0 += 1

        try:
            line = RULES[i_0]
        except IndexError:
            break

        # state and params
        if state_0 == 0:
            line = RULES[i_0]

            # extract state and input params
            state_1 = 0
            t_0 = ""
            t_1 = ""

            for i_1 in line[1:]:
                if state_1 == 0:
                    if i_1 == ">":
                        state_1 = 1
                    else:
                        t_0 += i_1

                else:
                    t_1 += i_1

            arg_0 = t_0
            arg_1 = t_1

            state_0 = 1

        # {
        elif state_0 == 1:
            state_0 = 2

        # operations or }
        else:
            line = RULES[i_0]

            # }
            if line == "}":

                new_rules_list.append([arg_0, arg_1, [i for i in arg_2]])

                arg_0 = ""
                arg_1 = ""
                arg_2.clear()

                state_0 = 0

            # operations
            else:
                arg_2.append(line)

    RULES = new_rules_list


def insert_regex():
    global RULES
    new_rules_list = list()
    for rule in RULES:

        pointer = rule[1]

        for j, r in enumerate(REGEX):
            if pointer.__contains__(str(r[0])):
                pointer = pointer.replace(r[0], "(" + str(r[1]) + ")")

        new_rules_list.append([rule[0], pointer, rule[2]])

    RULES = new_rules_list


if __name__ == '__main__':

    s = "".join([i for i in open(IN_PATH).readlines()])

    load_language()

    restructure_rules()

    # ['S_komentar', '{sviZnakovi}', ['-']]
    # ->
    # ['S_komentar', '(a|b|c)...', ['-']]
    insert_regex()

    # for i in RULES:
    #     print(i)

    # input("t")

    [print(i) for i in RULES]

    from lexer_generator.regex_manager import regex_driver

    lexer_code = ["from nfa.main import driver",
                  "",
                  "MAX_EATER_NUMBER = -1",
                  "MAX_EATER_POINTER = -1",
                  "SOURCE_CODE = \"\".join([i for i in open(\"" + IN_PATH + "\").readlines()])",
                  "CURRENT_STATE = \"" + INITIAL_STATE + "\"",
                  "OUTPUT = list()",
                  "LINE_NUMBER = 1",
                  "",
                  ""
                  ]

    for k, rule in enumerate(RULES):
        lexer_code.append("def f_" + str(k) + "(may_i_eat=False):")
        lexer_code.append("    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT")
        lexer_code.append("    global LINE_NUMBER")

        lexer_code.append("")

        t = regex_driver(rule[1])

        # for i in t[0]:
        #     lexer_code.append("    # " + str(i))
        lexer_code.append("    # " + str(rule))

        lexer_code.append("    if CURRENT_STATE == \"" + rule[0] + "\":")
        lexer_code.append("        print(" + str(k) + ")")

        lexer_code.append("        " + "t_in = [")
        lexer_code.append("            " + "str(SOURCE_CODE),")
        lexer_code.append("            " + str(t[2]) + ",")
        lexer_code.append("            " + "\"S_0\"" + ",")
        for i in (t[0])[:-1]:
            source = i[0]
            input_symbol = i[1]
            destination = i[2]

            if input_symbol == "\\*":
                input_symbol = "*"

            if input_symbol == "\\_":
                input_symbol = " "

            elif input_symbol in ["\\(", "\\)", "\\{", "\\}", "\\$", "\\\\", "\\|"]:
                input_symbol = input_symbol[1:]

            elif input_symbol == "\\n":
                input_symbol = "\n"
            elif input_symbol == "\\t":
                input_symbol = "\t"

            lexer_code.append("            " + str([source, input_symbol, destination]) + ",")
        t = (t[0])[-1]
        source = t[0]
        input_symbol = t[1]
        destination = t[2]

        if input_symbol == "\\*":
            input_symbol = "*"

        if input_symbol == "\\_":
            input_symbol = " "

        elif input_symbol in ["\\(", "\\)", "\\{", "\\}", "\\$", "\\\\", "\\|"]:
            input_symbol = input_symbol[1:]

        elif input_symbol == "\\n":
            input_symbol = "\n"
        elif input_symbol == "\\t":
            input_symbol = "\t"

        lexer_code.append("            " + str([source, input_symbol, destination]))
        lexer_code.append("        " + "]")

        lexer_code.append("        " + "t_0, is_accepted = driver(t_in)")
        lexer_code.append("")

        lexer_code.append("        if may_i_eat:")

        #

        actions = rule[2]
        print()
        print(actions)

        # input("try for " + str(rule))

        is_line_count_increased = False
        reduction_count = -1
        output_action = ""
        is_output_action_present = False
        is_reduction_made = False
        for action in actions:

            if action == "NOVI_REDAK":
                lexer_code.append("            LINE_NUMBER += 1")
                is_line_count_increased = True

            elif action == "-":
                pass

            else:
                t = action.split(" ")
                t_1 = t[0]

                if t_1 == "VRATI_SE":
                    reduction_count = t[1]
                    lexer_code.append("            reduction_value = SOURCE_CODE[:" + t[1] + "]")

                    is_reduction_made = True

                elif t_1 == "UDJI_U_STANJE":
                    lexer_code.append("            CURRENT_STATE = \"" + t[1] + "\"")

                else:
                    output_action = t_1
                    is_output_action_present = True

        if is_output_action_present:
            lexer_code.append("            OUTPUT.append(\"" + output_action + " \"" +
                              " + str(LINE_NUMBER" + (" -1" if is_line_count_increased else "") + ")" +
                              " + \" \" + SOURCE_CODE[:" +
                              (str(reduction_count) if is_reduction_made else "MAX_EATER_NUMBER") + "])"
                              )

        if is_reduction_made:
            lexer_code.append("            SOURCE_CODE = SOURCE_CODE[" + t[1] + ":]")

        else:
            lexer_code.append("            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]")

        lexer_code.append("        elif is_accepted:")
        lexer_code.append("")
        lexer_code.append("            if t_0.count(\"|\") > MAX_EATER_NUMBER:")
        lexer_code.append("                MAX_EATER_NUMBER = t_0.count(\"|\")")
        lexer_code.append("                MAX_EATER_POINTER = " + str(k))

        lexer_code.append("")
        lexer_code.append("        return t_0.count(\"|\")")
        lexer_code.append("")
        lexer_code.append("")

    lexer_code.append("if __name__ == '__main__':")
    lexer_code.append("    TTL = 15")
    lexer_code.append("")
    lexer_code.append("    while SOURCE_CODE != \"\":")
    # lexer_code.append("    while TTL != 0:")
    lexer_code.append("        TTL -= 1")

    lexer_code.append("        MAX_EATER_NUMBER -= 1")
    lexer_code.append("        MAX_EATER_POINTER = -1")

    lexer_code.append("")

    for k in range(0, len(RULES)):
        lexer_code.append("        f_" + str(k) + "()")

    lexer_code.append("")
    lexer_code.append("        print(\"MAX_EATER_NUMBER\", MAX_EATER_NUMBER)")

    lexer_code.append("        if MAX_EATER_POINTER == 0:")
    lexer_code.append("            f_0(True)")

    for k in range(1, len(RULES)):
        lexer_code.append("        elif MAX_EATER_POINTER == " + str(k) + ":")
        lexer_code.append("            f_" + str(k) + "(True)")

    lexer_code.append("        print(100 * \"*\")")
    lexer_code.append("        print(list(SOURCE_CODE))")

    lexer_code.append("        print(SOURCE_CODE)")
    lexer_code.append("        [print(i) for i in OUTPUT]")
    lexer_code.append("        print(CURRENT_STATE)")

    lexer_code.append("        if MAX_EATER_NUMBER < 0:")
    lexer_code.append("            SOURCE_CODE = SOURCE_CODE[1:]")

    lexer_code.append("    # file = [i[:-1] for i in open(\"lexer.py\").readlines()]")
    lexer_code.append("    # [print(\"lexer_code.append(\\\"\" + str(i) + \"\\\")\") for i in file]")
    lexer_code.append("    pass")

    f = open("lexer.py", "w")
    [f.write(str(i) + "\n") for i in lexer_code]
    f.close()

    [print(i) for i in open(IN_PATH).readlines()]
