import re
LANGUAGE = [line[:-1] for line in open("minusLang.lan").readlines()]


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


def print_language():
    [print(i) for i in REGEX]
    print(RULES)


load_language()

print_language()