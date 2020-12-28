import re
LANGUAGE = [line[:-1] for line in open("test_cases/minusLang.lan").readlines()]
TOKENS = "".join([line for line in open("test_cases/minusLang.in").readlines()])


REGEX = list()
RULES = list()
INITIAL_STATE = list()
STATES = list()


# citanje iz .lan datoteke
def load_language():
    global REGEX, RULES, INITIAL_STATE

    state = 0
    for line in open("test_cases/minusLang.lan").readlines():
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
            new_regex = [REGEX[0]]

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


def source():
    start_state = "S_pocetno"

    source_code = "".join([i for i in open("test_cases/minusLang.in").readlines()])
    print([source_code])
    print(list(source_code))

    current_state = start_state



    if current_state == "S_pocetno":

        if source_code.startswith("\t"):
            print("S_pocetno, \\t -> [\"-\"]")

            # source_code = source_code[len("\t"):]
            # print(source_code)
            #
            # source_code = source_code[2:]
            # print(source_code)

        # todo \_ -> " "
        if source_code.startswith(" "):
            print("S_pocetno, \_ -> [\"-\"]")

    if current_state == "S_pocetno":

        if source_code.startswith("\n"):
            print("S_pocetno, \n -> [\'-\', \'NOVI_REDAK\']")

    if current_state == "S_pocetno":

        # todo \| -> |
        if source_code.startswith("#|"):
            print("S_pocetno, #\| -> [\'-\', \'UDJI_U_STANJE S_komentar\']")



if __name__ == '__main__':

    s = "".join([i for i in open("test_cases/minusLang.in").readlines()])
    print(list(s))
    print()

    # source()
    #
    # import sys
    # sys.exit()

    load_language()

    restructure_rules()

    # ['S_komentar', '{sviZnakovi}', ['-']]
    # ->
    # ['S_komentar', '(a|b|c)...', ['-']]
    insert_regex()

    from regex_manager import regex_driver

    lexer_code = []

    lexer_code.append("from nfa.main import driver")
    lexer_code.append("")
    lexer_code.append("MAX_EATER_NUMBER = -1")
    lexer_code.append("MAX_EATER_POINTER = -1")
    lexer_code.append("SOURCE_CODE = \"\".join([i for i in open(\"test_cases/minusLang.in\").readlines()])")
    lexer_code.append("CURRENT_STATE = \"S_pocetno\"")
    lexer_code.append("OUTPUT = list()")
    lexer_code.append("LINE_NUMBER = 1")
    lexer_code.append("OP_NEW_LINE = \"NOVI_REDAK\"")
    lexer_code.append("OP_ENTER_STATE = \"UDJI_U_STANJE\"")
    lexer_code.append("OP_RET = \"VRATI_SE\"")
    lexer_code.append("NO_OP = \"-\"")

    lexer_code.append("")
    lexer_code.append("")

    for k, rule in enumerate(RULES):
        lexer_code.append("def f_" + str(k) + "(may_i_eat=False):")
        lexer_code.append("    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT, OP_NEW_")
        lexer_code.append("    global OP_RET, OP_ENTER_STATE, OP_NEW_LINE, LINE_NUMBER, NO_OP")

        lexer_code.append("")

        t = regex_driver(rule[1])

        for i in t[0]:
            lexer_code.append("    # " + str(i))
        lexer_code.append("    # " + str(rule))

        lexer_code.append("    if CURRENT_STATE == \"" + rule[0] + "\":")

        lexer_code.append("        " + "t_in = [")
        lexer_code.append("            " + "str(SOURCE_CODE),")
        lexer_code.append("            " + str(t[2]) + ",")
        lexer_code.append("            " + "\"S_0\"" + ",")
        for i in (t[0])[:-1]:
            source = i[0]
            input_symbol = i[1]
            destination = i[2]
            print(input_symbol)
            if input_symbol in ["\\(", "\\)", "\\{", "\\}", "\\$", "\\_", "\\\\", "\\|"]:
                if input_symbol == "\\_":
                    input_symbol = " "
                else:
                    input_symbol = input_symbol[1:]

            lexer_code.append("            " + str([source, input_symbol, destination]) + ",")
        t = (t[0])[-1]
        source = t[0]
        input_symbol = t[1]
        destination = t[2]
        if input_symbol in ["\\(", "\\)", "\\{", "\\}", "\\$", "\\_", "\\\\", "\\|"]:
            if input_symbol == "\\_":
                input_symbol = " "
            else:
                input_symbol = input_symbol[1:]
        lexer_code.append("            " + str([source, input_symbol, destination]))
        lexer_code.append("        " + "]")

        lexer_code.append("        " + "t_0 = driver(t_in)")
        lexer_code.append("")

        lexer_code.append("        if may_i_eat:")
        lexer_code.append("            actions = " + str(rule[2]))
        lexer_code.append("            # " + str(rule[2]))

        lexer_code.append("")
        lexer_code.append("            is_reduction_made = False")
        lexer_code.append("")
        lexer_code.append("            for action in actions:")
        lexer_code.append("                t = actions.split(" ")")
        lexer_code.append("                k = t[0]")
        lexer_code.append("                v = t[1]")
        lexer_code.append("")
        lexer_code.append("                if k == OP_NEW_LINE:")
        lexer_code.append("                    LINE_NUMBER += 1")
        lexer_code.append("                elif k == OP_ENTER_STATE:")
        lexer_code.append("                    CURRENT_STATE = v")
        lexer_code.append("                elif k == NO_OP:")
        lexer_code.append("                    pass")
        lexer_code.append("                elif k == OP_ENTER_STATE:")
        lexer_code.append("                    SOURCE_CODE = SOURCE_CODE[v:]")
        lexer_code.append("                    is_reduction_made = True")
        lexer_code.append("                else:")
        lexer_code.append("                    OUTPUT.append(action)")
        lexer_code.append("")
        lexer_code.append("            if not is_reduction_made:")
        lexer_code.append("                SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]")
        lexer_code.append("")
        lexer_code.append("        else:")
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
    lexer_code.append("    while TTL != 0:")
    lexer_code.append("        TTL -= 1")
    lexer_code.append("")

    for k in range(1, len(RULES)):
        lexer_code.append("        f_" + str(k) + "()")

    lexer_code.append("")
    lexer_code.append("        print(\"MAX_EATER_NUMBER\", MAX_EATER_NUMBER)")

    lexer_code.append("        if MAX_EATER_POINTER == 0:")
    lexer_code.append("            f_0(True)")

    for k in range(1, len(RULES)):
        lexer_code.append("        elif MAX_EATER_POINTER == " + str(k) + ":")
        lexer_code.append("            f_" + str(k) + "(True)")
    lexer_code.append("        print(SOURCE_CODE)")
    lexer_code.append("    # file = [i[:-1] for i in open(\"lexer.py\").readlines()]")
    lexer_code.append("    # [print(\"lexer_code.append(\\\"\" + str(i) + \"\\\")\") for i in file]")
    lexer_code.append("    pass")







    [print(i) for i in lexer_code]

    f = open("lexer.py", "w")
    [f.write(str(i) + "\n") for i in lexer_code]
    f.close()

# todo $
