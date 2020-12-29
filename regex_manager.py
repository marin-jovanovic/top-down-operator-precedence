OUTPUT = list()
ROW = 1


# ret true ako je ovo |
# ret false ako je ovo \|
def is_escaped_at_index(s, index):

    s = s[:index]

    count = 0
    for i_0 in reversed(s):
        if i_0 != "\\":
            break
        else:
            count += 1

    return not (count + 1) % 2 == 0


# input: a|\|b|c
# output: [a, \|b, c]
def split_by_separator(v_regex):
    # print(["input", v_regex])
    # print(v_regex)
    state_of_brackets = 0

    t_0 = ""

    ret = list()

    for iterator_1, token in enumerate(v_regex):
        t_0 += token
        if token == "(":
            if iterator_1 == 0:
                state_of_brackets += 1

            elif is_escaped_at_index(v_regex, iterator_1):
                state_of_brackets += 1

        elif token == ")":
            if iterator_1 == 0:
                pass

            elif is_escaped_at_index(v_regex, iterator_1):
                state_of_brackets -= 1

        elif token == "|":

            if state_of_brackets == 0 and is_escaped_at_index(v_regex, iterator_1):

                ret.append("".join([i for i in t_0[:-1]]))
                t_0 = ""
        else:
            pass

    ret.append("".join([i for i in t_0]))
    # print(ret)
    # [print(i) for i in ret]
    return ret


# finds first open bracket
# bracket_handler("a(bc)d") == [1, 4, "bc"]:
def bracket_handler(s):
    # print(s)

    state_of_brackets = 0

    index_start = -1
    index_end = -1
    content = ""
    state = 0

    for i_0, token in enumerate(s):

        if token == "(":
            if i_0 == 0:
                state_of_brackets += 1

                if state == 0:
                    index_start = i_0
                    state = 1

            elif s[i_0 - 1] != "\\":
                state_of_brackets += 1

                if state == 0:
                    index_start = i_0
                    state = 1

        elif token == ")":
            if i_0 == 0:
                state_of_brackets -= 1

            elif s[i_0 - 1] != "\\":
                state_of_brackets -= 1

            if state_of_brackets == 0:
                index_end = i_0

                state = 2
                continue

        if state == 1:
            content += token

        elif state == 2:
            if token in ["+", "*"]:
                index_end += 1
            break

    ret = [index_start, index_end, content[1:]]

    print("bracket_handler", s, ret)
    return ret


def test_bracket_handler():
    t = 0
    if bracket_handler("(((((a)))))") == [0, 10, "((((a))))"]:
        print("test passed")
        t += 1

    if bracket_handler("((abc))") == [0, 6, "(abc)"]:
        print("test passed")

        t += 1

    if bracket_handler("a(bc)d") == [1, 4, "bc"]:
        print("test passed")

        t += 1

    print("test", t)


# todo bracket skip
# returns True if @s contains "|", not "\\|"
def is_separator_present(s):
    for i_0, token_0 in enumerate(s):

        if token_0 == "|":

            if i_0 == 0:
                return True

            elif s[i_0 - 1] != "\\":
                return True

    return False


# if bracket at start of @s
# returns @-1
# input: \*, output: 1
# input: *, output: 0
def get_first_token_index(s):

    t_0 = bracket_handler(s)

    while t_0[0] != -1:
        if t_0[0] == 0:
            return -1

        s = s[: t_0[0]] + s[t_0[1] + 1:]
        t_0 = bracket_handler(s)

    # print(s)

    if s[0] == "\\":
        return 1
    else:
        return 0


def regex_driver(s, start_index=0, max_index=0):
    rules = list()
    # max_index = 0
    # start_index = 0
    prefix = "S_"
    accept_states = []

    # remove brackets if exist
    # t_0 = bracket_handler(s)
    # if t_0[0] == 0 and t_0[1] == len(s) - 1:
    #     t_1 = s[t_0[0] + 1: t_0[1]]
    #     return regex_driver(t_1)

    streams = split_by_separator(s)

    for s in streams:

        i_0 = -1
        while i_0 != len(s) - 1:
            i_0 += 1
            token_0 = s[i_0]

            # actions
            # (, ), +, *

            # tokens
            # \(, \), \+, \*

            source = prefix + str(start_index if i_0 == 0 else max_index)
            destination = prefix + str(max_index + 1)
            max_index += 1

            a_states_buffer = []

            # action
            if token_0 == "(":
                t_1 = bracket_handler(s[i_0:])

                t_2 = s[i_0 + t_1[0] + 1: i_0 + t_1[1] - 1]
                i_0 = t_1[1] + i_0

                # new_streams = split_by_separator(t_2)

                start_index_2 = max_index

                for i in split_by_separator(t_2):
                    rules.append([source, "$", prefix + str(max_index)])
                    max_index += 1

                    new_rules, max_index, new_accept_states = regex_driver(i,
                                                                           max_index - 1,
                                                                           max_index - 1)

                    [a_states_buffer.append(i) for i in new_accept_states]

                    [rules.append(i) for i in new_rules]

                destination = prefix + str(max_index)

                # from end to new state
                for i in a_states_buffer:
                    rules.append([i, "$", destination])

                if s[i_0] in ["*", "+"]:

                    # from end to new state
                    for i in a_states_buffer:
                        rules.append([i, "$", prefix + str(start_index_2 - 1)])

                    if s[i_0] == "*":
                        rules.append([source, "$", destination])

            # token prefix handler
            elif token_0 == "\\":

                i_0 += 1
                token_0 = s[i_0]

                # no need to check if token
                rules.append([source, "\\" + token_0, destination])

            # token
            else:
                rules.append([source, token_0, destination])

        accept_states.append(max_index)

    # print(s)
    # [print(i) for i in rules]
    # print("accept states:")
    # [print(prefix + str(i)) for i in accept_states]
    # print("****************************************************************************************************")
    return rules, max_index + 1, [(prefix + str(i)) for i in accept_states]


def run_tests():

    # todo escape symbols
    regex_driver("(\\(|\\)|\\{|\\}|\\||\\*|\\\\|\\$|\\t|\\n|\\_|!|\"|#|%|&|\'|+|,|-|.|/|0|1|2|3|4|5|6|7|8|9|:|;|<|=|>|?"
                 "|@|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|[|]|^|_|`|a|b|c|d|e|f|g|h|i|j|k|"
                 "l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|~)")

    regex_driver("\\n")

    regex_driver("\\(")

    regex_driver("\\)")

    regex_driver("-")

    regex_driver("\\t|\\_")

    regex_driver("#\\|")

    regex_driver("\\|#")

    regex_driver("-(\\t|\\n|\\_)*-")

    regex_driver("\\((\\t|\\n|\\_)*-")

    regex_driver("-(\\t|\\n|\\_)*-")

    regex_driver("a|b|(c)+|d")

    # regex_driver("ab|cd")
    # regex_driver("\\ab|cd")
    # regex_driver("ab|\\cd")
    # regex_driver("\\ab|\\cd")

    inp = "(ab)+efd|(de)*def"
    regex_driver(inp, 0, 0)

    # t = bracket_handler(c)
    # print(c[t[0]:t[1] + 2])

    inp = "a|test|(dwa)har"
    regex_driver(inp, 0, 0)

    inp = "((0|1|2|3|4|5|6|7|8|9)(0|1|2|3|4|5|6|7|8|9)*|0x((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D"\
          "|E|F)((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D|E|F)*)"

    # inp = "(0|1|2|3|4|5|6|7|8|9)"
    regex_driver(inp, 0, 0)

    inp = "(0|1|2|3|4|5|6|7|8|9)"
    regex_driver(inp, 0, 0)

    inp = "(0|1|2|3|4|5|6|7|8|9)*"
    regex_driver(inp, 0, 0)


# todo
#     special chars
#     +, *, (, ), [, ], .,
if __name__ == '__main__':

    run_tests()
