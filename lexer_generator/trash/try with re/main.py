import re
import sys

SOURCE = "minusLang.lan"
SOURCE_CODE_PATH = "../../test_cases/minusLang.in"

REGEX_LIST = list()
STATES = list()
NAMES = list()
RULES = list()
INITIAL_STATE = ""

NEW_ROW = "NOVI_REDAK"
ENTER_NEW_STATE = "UDJI_U_STANJE"
GO_BACK = "VRATI_SE"

ROW_COUNTER = 1

def log(*data):
    print(data)


def process_rules():
    global STATES, NAMES, RULES, INITIAL_STATE

    lines = [line[:-1] for line in open(SOURCE).readlines()]

    i, line = init_regex_list(lines)

    init_initial_state(line)

    i, line = init_states_list(i, line, lines)

    i, line = init_names_list(i, line, lines)

    temp = init_rules_list(RULES, i, line, lines)


def init_rules_list(RULES, i, line, lines):
    global REGEX_LIST
    temp = list()
    state = "left"
    right_temp = list()

    while True:
        # end of file
        if line == "":
            break

        # actions starts after this token
        if lines[i] == "{":
            state = "right"

        # actions end with this token
        elif lines[i] == "}":

            temp.append([i for i in right_temp])

            state = "left"
            RULES.append([i for i in temp])
            right_temp.clear()
            temp.clear()

        # current state + input
        elif state == "left":

            # s = current state
            try:
                s = re.search('<(.+?)>', line).group(1)
            except AttributeError:
                print("error while parsing")
                import sys
                sys.exit()

            temp.append(s)

            # pointer = input
            pointer = line[line.find(">") + 1:]

            for j, r in enumerate(REGEX_LIST):
                if pointer.__contains__(str(r[0])):
                    #
                    # (r[0])
                    pointer = pointer.replace(r[0], "(" + str(r[1]) + ")")
                    # log(pointer)

            # regex correction
            # if not escaped, regex errors occur
            new_pointer = ""
            for token in pointer:
                if token in ("/", "+", "?", ".", "\"", "[", "]", "^"):
                    token = "\\" + token
                    # print(token)



                new_pointer += token

            new_pointer = new_pointer.replace("\_", " ")

            novi = ""

            for num, target in enumerate(list(new_pointer)):
                target = str(target)

                if num == 0 and target.isalnum():
                    novi += "[" + target + "]"

                elif target.isalnum() and new_pointer[num - 1] != "\\":
                    novi += "[" + target + "]"

                else:
                    novi += target



            new_pointer = novi

            pointer = new_pointer

            temp.append(pointer)

        # actions
        elif state == "right":
            right_temp.append(line)

        # error handling
        else:
            print("error while parsing input")
            import sys
            sys.exit()

        i += 1
        line = lines[i]

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
        import sys
        sys.exit()

def init_regex_list(lines):
    global REGEX_LIST
    i = 0
    line = lines[i]
    while not line.startswith("%X "):
        try:
            s = re.search('{(.+?)}', line).group(1)
        except AttributeError:
            print("error while parsing")
            import sys
            sys.exit()

        REGEX_LIST.append(["{" + s + "}", line[line.find("}") + 2:]])

        i += 1
        line = lines[i]

    NEW_REGEX = list()
    NEW_REGEX.append(REGEX_LIST[0])

    for raw in REGEX_LIST[1:]:
        left = str(raw[0])
        right = str(raw[1])

        for j, r in enumerate(NEW_REGEX):
            if right.__contains__(str(r[0])):
                right = right.replace(r[0], "(" + str(r[1]) + ")")

        NEW_REGEX.append([left, right])

    REGEX_LIST = NEW_REGEX

    return i, line


def print_rules():
    [print(line) for line in RULES]
    print()
    print("lexical analyzer initial state")
    print(INITIAL_STATE)


def print_source_code():
    print("+++source code+++")
    [print(token) for token in open(SOURCE_CODE_PATH).readlines()]
    print("\n+++source code end+++")


if __name__ == '__main__':
    process_rules()

    # print_rules()

    print_source_code()

    current_state = INITIAL_STATE

    tokens = "".join([line for line in open(SOURCE_CODE_PATH).readlines()])



    # print()
    # [print(i[1]) for i in RULES]

    f = open("demo.txt", "a")


    # f.write("t_in.append(\"" + INITIAL_STATE + "\")\n")
    #
    # for i in RULES:
    #     # print(i)
    #     f.write("t_in.append(" + str(i) + ")\n")
    # # f.write("Now the file has more content!")
    # f.close()


    print_rules()

    sys.exit()
    print("*********************************************************************************************************")

    OUTPUT = list()

    TTL = 500000


    while True:
        print(tokens)

        TTL -= 1

        action_performed = False


        # ovo racuna koje ce pravilo primjenit
        # primjenjuje se pravilo s najduljim matchem
        # ako ih je vise iste duljine onda se primjenjuje prvi od njih
        applyable_rules = list()

        for rule in RULES:
            if current_state == rule[0]:

                if re.match(rule[1], "".join(tokens)):
                    print("______________________________")

                    print(re.search(rule[1], tokens))

                    applyable_rules.append([rule, re.search(rule[1], tokens).end()])

        max = applyable_rules[0]

        for rule in applyable_rules:
            print(rule)

            len = rule[1]

            if max[1] < rule[1]:
                max = rule

        print("max", max)

        rule = max[0]

        # rule je najkraci

        print(rule)
        action_performed = True

        actions = rule[2]
        print("actions", actions)

        is_go_back_activated = False

        for i in actions:
            i = str(i)
            print("action", i)

            if i == "-":
                print("odbacivanje")
            elif i.startswith(ENTER_NEW_STATE):
                i = i.split(" ")
                current_state = i[1]
            elif i.startswith(NEW_ROW):
                ROW_COUNTER += 1
                print("novi red")
            elif i.startswith(GO_BACK):
                i = i.split(" ")
                print("go back")
                print(OUTPUT)

                is_go_back_activated = True
                tokens = tokens[int(i[1]):]

                # sys.exit()
            else:

                OUTPUT.append(str(i) + " " + str(ROW_COUNTER) + " " + re.search(rule[1], tokens).group(0))
                print(i, ROW_COUNTER, re.search(rule[1], tokens).group(0))

        if not is_go_back_activated:

            try:
                print(re.search(rule[1], tokens))

                tokens = tokens[re.search(rule[1], tokens).end():]

            except AttributeError:
                print("error while parsing")
                import sys

                sys.exit()

        print("new state", current_state)
        # print("tokens")
        # print(tokens)

        if not action_performed:
            print("no action")

            print(OUTPUT)
            sys.exit()

        print("*****************************************************************")

        if tokens == "":
            print("uspjesan kraj")
            [print(i) for i in OUTPUT]
            sys.exit()

        if TTL == 0:
            print("----------------------------- err TTL")
            print(tokens)
            sys.exit()
