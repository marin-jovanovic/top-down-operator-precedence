import re

def log(*data):
    print(data)


SOURCE = "minusLang.lan"

REGEX_LIST = list()
STATES = list()
NAMES = list()
RULES = list()
INITIAL_STATE = ""

NEW_ROW = "NOVI_REDAK"
ENTER_NEW_STATE = "UDJI_U_STANJE"
GO_BACK = "VRATI_SE"

SOURCE_CODE_PATH = "minusLang.in"


def process_rules():
    global STATES, NAMES, RULES, INITIAL_STATE

    lines = [line[:-1] for line in open(SOURCE).readlines()]

    i, line = init_regex_list(lines)

    init_initial_state(line)

    i, line = init_states_list(i, line, lines)

    i, line = init_names_list(i, line, lines)

    temp = init_rules_list(RULES, i, line, lines)

    log(temp)
    log()


def init_rules_list(RULES, i, line, lines):
    global REGEX_LIST
    temp = list()
    state = "left"
    right_temp = list()
    while True:
        if line == "":
            break

        log(line)

        if lines[i] == "{":
            state = "right"

        elif lines[i] == "}":
            temp.append([i for i in right_temp])
            log(temp)
            log()
            state = "left"
            RULES.append([i for i in temp])
            # temp.clear()
            right_temp.clear()
            temp.clear()

        elif state == "left":

            try:
                s = re.search('<(.+?)>', line).group(1)
            except AttributeError:
                print("error while parsing")
                import sys
                sys.exit()

            temp.append(s)

            pointer = line[line.find(">") + 1:]

            for j, r in enumerate(REGEX_LIST):
                if pointer.__contains__(str(r[0])):
                    log(r[0])
                    pointer = pointer.replace(r[0], "(" + str(r[1]) + ")")
                    log(pointer)

            temp.append(pointer)



        elif state == "right":
            right_temp.append(line)
            # temp.append(line)

        else:
            print("error while parsing input")
            import sys
            sys.exit()

        i += 1
        line = lines[i]
    # ovo ne zelimo jer se valjda izvrsavaju po redu pravila
    # RULES.sort(key=lambda x: x[0])




    return temp


def init_names_list(i, line, lines):
    global NAMES
    NAMES = [l for l in line[3:].split(" ")]
    i += 1
    line = lines[i]
    return i, line


def init_states_list(i, line, lines):
    global STATES
    # not regex
    STATES = [l for l in line[3:].split(" ")]
    i += 1
    line = lines[i]
    return i, line


def init_initial_state(line):
    global INITIAL_STATE
    try:
        INITIAL_STATE = (line.split(" "))[1]
    except AttributeError:
        print("error while parsing")


def init_regex_list(lines):
    global REGEX_LIST
    i = 0
    line = lines[i]
    while not line.startswith("%X "):
        log(line)
        try:
            s = re.search('{(.+?)}', line).group(1)
        except AttributeError:
            print("error while parsing")
            import sys
            sys.exit()

        log(s)
        log(line[line.find("}") + 2:])
        REGEX_LIST.append(["{" + s + "}", line[line.find("}") + 2:]])

        i += 1
        line = lines[i]

    NEW_REGEX = list()
    NEW_REGEX.append(REGEX_LIST[0])

    for raw in REGEX_LIST[1:]:
        log(raw)
        left = str(raw[0])
        right = str(raw[1])

        for j, r in enumerate(NEW_REGEX):
            if right.__contains__(str(r[0])):
                log(r[0])
                right = right.replace(r[0], "(" + str(r[1]) + ")")
                log(right)

        log([left, right])
        NEW_REGEX.append([left, right])

    REGEX_LIST = NEW_REGEX

    return i, line


def print_rules():
    print()
    print("regex")
    [print(line) for line in REGEX_LIST]
    print()
    print("lexical analyzer states")
    [print(line) for line in STATES]
    print()
    print("lexical token names")
    [print(line) for line in NAMES]
    print()
    print("lexical analyzer rules")
    [print(line) for line in RULES]
    print()
    print("lexical analyzer initial state")
    print(INITIAL_STATE)


import sys
if __name__ == '__main__':
    process_rules()

    print_rules()

    print("\n+++source code+++")
    [print(token) for token in open(SOURCE_CODE_PATH).readlines()]
    print("\n+++source code end+++")

    current_state = INITIAL_STATE

    for line_number, line in enumerate(open(SOURCE_CODE_PATH).readlines()):
        log(line_number, line)

        for token_number, token in enumerate(line):
            log(token_number, token)

    print()

    print_rules()

    for line_number, line in enumerate(open(SOURCE_CODE_PATH).readlines()):
        log(line_number, line)

        for token_number, token in enumerate(line):
            log(token_number, token)

    print()

    current_state = INITIAL_STATE

    tokens = list()
    for line in open(SOURCE_CODE_PATH).readlines():
        for i in list(line):
            tokens.append(i)


    print(tokens)

    [print(i) for i in RULES]

    i = 0
    token = tokens[i]
    print()
    # while True:
    #
    #     for rule in RULES:
    #         if current_state == rule[0]:
    #             print(rule[1])
    #
    #             if token == (rule[1])[0]:
    #                 print(rule)
    #
    #     sys.exit()



    while True:

        for rule in RULES:
            if current_state == rule[0]:
                print(rule)

                if re.match(rule[1], "".join(tokens)):
                    print(rule)

                    try:
                        print(re.search(rule[1], "".join(tokens)).end())
                        print("".join(tokens))
                        print()
                        tokens = tokens[re.search(rule[1], "".join(tokens)).end():]
                        print("".join(tokens))
                    except AttributeError:
                        print("error while parsing")
                        import sys

                        sys.exit()
                    sys.exit()




        sys.exit()
                # if re.match(rule[1], str(tokens)):
                #     print(rule)
                #
                # # if re.match():
                # #     print(rule)
                # #
                # # tweets = ["to thine own self coffee be true",
                # #                "coffee break python",
                # #                "coffees are awesome",
                # #                "coffe is cool"]
                # #
                # # for tweet in tweets:
                # #     if re.match("coff*", tweet):
                # #         print(tweet)
                #     print(tokens)
                #     print("".join(tokens))
                #     sys.exit()