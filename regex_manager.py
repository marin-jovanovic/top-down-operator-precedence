OUTPUT = list()
ROW = 1


# vraca true ako je ovo |
# vraca false ako je ovo znak \|
def is_escaped_at_index(s, index):

    # sve ispred indexa
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


# input: ((0|1|2|3|4|5|6|7|8|9)(0|1|2|3|4|5|6|7|8|9)*|
# output: 0|1|2|3|4|5|6|7|8|9
# provjeri prije jel postoji zagrada
def extract_deepest_bracket_content(s):

    state_of_brackets = 0
    deepest_left_bracket_index = 0
    deepest_left_bracket_depth = 0

    for i_0, token in enumerate(s):

        if token == "(":
            if i_0 == 0:
                state_of_brackets += 1

                if state_of_brackets > deepest_left_bracket_depth:
                    deepest_left_bracket_depth = state_of_brackets
                    deepest_left_bracket_index = i_0

            elif s[i_0 - 1] != "\\":
                state_of_brackets += 1

                if state_of_brackets > deepest_left_bracket_depth:
                    deepest_left_bracket_depth = state_of_brackets
                    deepest_left_bracket_index = i_0

                # # znaci da je \(
                # else:
                #     print(token)

            elif token == ")":
                # ovo se nikad nece ostvarit
                if i_0 == 0:
                    state_of_brackets -= 1

                elif s[i_0 - 1] != "\\":
                    state_of_brackets -= 1

                # # znaci da je \)
                # else:
                #     print(token)

            # else:
            #     print(token)

    # print(deepest_left_bracket_index)
    # print(deepest_left_bracket_depth)

    t_0 = ""

    for i_0, token in enumerate(s[deepest_left_bracket_index:]):
        t_0 += token

        if token == ")":
            # never true
            if i_0 == 0:
                state_of_brackets -= 1
                t_0 = t_0[1:-1]
                break
                # print("kraj")

            elif s[i_0 - 1] != "\\":
                state_of_brackets -= 1
                t_0 = t_0[1:-1]
                break

            # \)
            # else:
            #     print(token)

        # else:
            #     print(token)

    print("extracted: *" + t_0 + "*")

    return t_0


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


def split_by_state(s):
    # ret = list()

    t_0 = list()

    # append_tokens = True

    for i, token in enumerate(s):
        print(i, token)

        # if not append_tokens:
        #     append_tokens_counter

        if token == "(":
            if is_escaped_at_index(s, i):
                print("lijeva zagrada")
                # print(s[i:])
                # t_1 = bracket_handler(s[i:])
                # append_tokens = False
                # append_tokens_counter = t_1[1]
            else:
                print("token")

        elif token == ")":
            if is_escaped_at_index(s, i):
                print("desna zagrada")
            else:
                print("token")

        elif token == "+":
            if is_escaped_at_index(s, i):
                print("plusic")
            else:
                print("token")

        elif token == "*":
            if is_escaped_at_index(s, i):
                print("mnozenje")
            else:
                print("token")

        # else:
        #     pass

    # print(t_0)
    return t_0


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

    print(s)

    if s[0] == "\\":
        return 1
    else:
        return 0

    # count = 0
    # t_0 = ""
    #
    # i_1 = -1
    # is_prev_escaper = False
    # while i_1 != len(s) - 1:
    #     i_1 += 1
    #     token_1 = s[i_1]
    #
    #     print(i_1, token_1)
    #     t_0 += token_1
    #
    #     if i_1 == 0:
    #
    #         if token_1 == "\\":
    #             continue
    #
    #         elif token_1 not in ["("]:
    #             count += 1
    #
    # print(t_0)
    # return True


def regex_driver(s):
    print(["input", s])
    rules = list()
    max_index = 0
    start_index = 0
    prefix = "S_"
    accept_states = []

    # zagrade na pocetku i kraju
    # mice zagrade s pocetka i kraja dok postoje
    # hendla svu logiku da mice samo ako ima smisla micat
    t_0 = bracket_handler(s)
    if t_0[0] == 0 and t_0[1] == len(s) - 1:
        t_1 = s[t_0[0] + 1: t_0[1]]
        print(["rekurzija, mako sam zagrade", t_1])
        return regex_driver(t_1)

    streams = split_by_separator(s)
    print("streams: " + str(streams))

    for s in streams:

        i_0 = -1
        while i_0 != len(s) - 1:
            i_0 += 1
            token_0 = s[i_0]

            # actions
            # (, ), +, *

            # tokens
            # \(, \), \+, \*

            # start of stream
            if i_0 == 0:

                print(1, i_0, token_0)

                # todo complete action actions

                # action
                if token_0 == "(":
                    print("a")
                    t_1 = bracket_handler(s[i_0:])
                    t_0 = s[i_0 + t_1[0]: i_0 + t_1[1] + 1]
                    i_0 = t_1[1] + i_0

                    rules.append([prefix + str(start_index), t_0, prefix + str(max_index + 1)])
                    max_index += 1

                # token prefix handler
                elif token_0 == "\\":

                    i_0 += 1
                    token_0 = s[i_0]

                    # no need to check if token
                    rules.append([prefix + str(start_index), "\\" + token_0, prefix + str(max_index + 1)])
                    max_index += 1

                # token
                else:
                    print("c")
                    rules.append([prefix + str(start_index), token_0, prefix + str(max_index + 1)])
                    max_index += 1

            elif s[i_0 - 1] == "\\":
                print(2, i_0, token_0)

                # action
                if is_escaped_at_index(s, i_0):
                    print("TODO action")

                    if token_0 == "(":
                        print("TODO left bracket")

                # token
                else:

                    rules.append([prefix + str(max_index), "\\" + token_0, prefix + str(max_index + 1)])
                    max_index += 1

            else:
                print(3, i_0, token_0)
                # action
                if token_0 in ["(", ")", "+", "*"]:

                    if token_0 == "(":
                        t_1 = bracket_handler(s[i_0:])
                        t_0 = s[i_0 + t_1[0]: i_0 + t_1[1] + 1]
                        i_0 = t_1[1] + i_0

                        rules.append([prefix + str(max_index), t_0, prefix + str(max_index + 1)])
                        max_index += 1

                # fixme
                elif token_0 == "\\":
                    continue

                # token
                else:
                    rules.append([prefix + str(max_index), token_0, prefix + str(max_index + 1)])
                    max_index += 1

        accept_states.append(max_index)

    [print(i) for i in rules]
    print("accept states:")
    [print(prefix + str(i)) for i in accept_states]
    print("****************************************************************************************************")
    return rules


# todo
#     specijalni znakovi
#     +, *, (, ), [, ], .,
if __name__ == '__main__':

    # print(get_first_token_index("0\\123(3(1(2)+4)5)*67(2)89"))
    #
    # import sys
    # sys.exit()

    regex_driver("\\n")

    regex_driver("\\(")

    regex_driver("\\)")

    regex_driver("-")

    regex_driver("\\t|\\_")

    regex_driver("#\\|")

    regex_driver("\\|#")

    # todo " nije imao \, hendlaj sve te escapeove
    regex_driver("(\\(|\\)|\\{|\\}|\\||\\*|\\\\|\\$|\\t|\\n|\\_|!|\"|#|%|&|\'|+|,|-|.|/|0|1|2|3|4|5|6|7|8|9|:|;|<|=|>|?"
                 "|@|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|[|]|^|_|`|a|b|c|d|e|f|g|h|i|j|k|"
                 "l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|~)")

    regex_driver("((0|1|2|3|4|5|6|7|8|9)(0|1|2|3|4|5|6|7|8|9)*|0x((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D"
                 "|E|F)((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D|E|F)*)")

    regex_driver("-(\\t|\\n|\\_)*-")

    regex_driver("\\((\\t|\\n|\\_)*-")

    regex_driver("-(\\t|\\n|\\_)*-")

    regex_driver("a|b|(c)+|d")

    # regex_driver("ab|cd")
    # regex_driver("\\ab|cd")
    # regex_driver("ab|\\cd")
    # regex_driver("\\ab|\\cd")

    regex_driver("(ab)+efd|(de)*def")
    regex_driver("a|test|(dwa)har")

    # c = "a|test(dwakad)+djnaidjai"
    # t = bracket_handler(c)
    # print(c[t[0]:t[1] + 2])
