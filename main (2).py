import re
LANGUAGE = [line[:-1] for line in open("minusLang.lan").readlines()]
TOKENS = "".join([line for line in open("minusLang.in").readlines()])


REGEX = list()
RULES = list()
INITIAL_STATE = list()


def load_language():
    global REGEX, RULES, INITIAL_STATE

    state = 0
    for line in open("minusLang.lan").readlines():
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


def restruct_rules():
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


load_language()

restruct_rules()

# ['S_komentar', '{sviZnakovi}', ['-']]
# ->
# ['S_komentar', '(a|b|c)...', ['-']]
insert_regex()

[print(i) for i in RULES]
print()
[print(i[1]) for i in RULES]
print()
# print(TOKENS)

# print("-----")




for iterator in RULES:

    input_raw = iterator[1]
    print(input_raw)

    splited_regexes = list()
    state_of_brackets = 0

    t_0 = ""

    for iterator_1, token in enumerate(input_raw):
        print(iterator_1, token)

        if token == "|":

            if state_of_brackets == 0:
                if iterator_1 == 0:
                    pass

                if input_raw[iterator_1 - 1] == "\\":
                    print("ovo je znak")

                else:

                    splited_regexes.append(t_0)
                    t_0 = ""
                    print("ovdje podijeli")

        else:
            t_0 += token

    splited_regexes.append(t_0)

    print(splited_regexes)


        # elif token == "(":
        #     if iterator_1 == 0:
        #         state_of_brackets += 1
        #         print("zagrada")
        #         t_0 = ""
        #
        #     elif input_raw[iterator_1] != "\\":
        #         state_of_brackets += 1
        #         print("zagrada")
        #         t_0 = ""
        #
        # elif token == ")":
        #     if iterator_1 == 0:
        #         pass
        #
        #     elif input_raw[iterator_1] != "\\":
        #         state_of_brackets -= 1
        #         print("zagrada")



        #
        # if state_of_brackets == 0:
        #     print("na nuli smo")
        #     print(t_0)


    # new_input = list()
    #
    # state_of_brackets = 0
    #
    # t_0
    # t_0 = ""
    #
    # for iterator_1, token in enumerate(input):
    #     print(token)
    #
    #     if token == "(":
    #         if iterator_1 == 0:
    #             state_of_brackets += 1
    #             print("zagrada")
    #             t_0 = ""
    #
    #         elif input[iterator_1] != "\\":
    #             state_of_brackets += 1
    #             print("zagrada")
    #             t_0 = ""
    #
    #     elif token == ")":
    #         if iterator_1 == 0:
    #             pass
    #
    #         elif input[iterator_1] != "\\":
    #             state_of_brackets -= 1
    #             print("zagrada")
    #
    #
    #
    #
    #     if state_of_brackets == 0:
    #         print("na nuli smo")
    #         print(t_0)


    # print(new_input)
    print()






import sys
sys.exit()


t_0 = ""
current_state = INITIAL_STATE
TTL = 10

while True:
    TTL -= 1
    if TTL == 0:
        break

    for rule in RULES:

        state = rule[0]

        if current_state == state:
            print(state)




    break


















