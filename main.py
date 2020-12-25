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

    # [print(i) for i in RULES]
    #
    # print()
    #
    # [print(i) for i in REGEX]
    #
    from regex_manager import regex_driver
    #
    # print()

    [print(i) for i in RULES]




    for rule in RULES:

        print(rule)


        print(regex_driver(rule[1]))
        # init_state = rule[0]
        # inputs = regex_driver(rule[1])
        # actions = rule[2]
        #
        # # print([rule[1]])
        # write_content = ""
        #
        # write_content += "if current_state == \"" + init_state + "\":\n"
        # write_content += "\n"
        # write_content += "\tif source_code.startswith(\""
        #
        #
        # print(inputs)
        #
        # print(write_content)




'''
    specijalni regex znakovi
    (, ), {, }, |, *, $, \
    
    $
        prazan niz
    
    \n 
        novi red
    \t
        tab
        
    \_
        razmak
    
    
'''