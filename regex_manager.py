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


def test_split_by_separator():

    # a'|'b
    if split_by_separator("a\\|b") == ["a\\|b"]:
        print("test pass")
    print()

    # a\\ | b
    if split_by_separator("a\\\\|b") == ["a\\\\", "b"]:
        print("test pass")
    print()

    # a\\\|b
    if split_by_separator("a\\\\\\|b") == ["a\\\\\\|b"]:
        print("test pass")
    print()

    if split_by_separator("a\\\\|b") == ["a\|b"]:
        print("test pass")
    print()

    if split_by_separator("(a|\(|b|c)d|x") == ["(a|\(|b|c)d", "x"]:
        print("test pass")
    print()

    if split_by_separator("(a|\(|b|c)d|x|e") == ["(a|\(|b|c)d", "x", "e"]:
        print("test pass")
    print()

    if split_by_separator("(a|\(|b|c)d|x|e|(d|f)") == ["(a|\(|b|c)d", "x", "e", "(d|f)"]:
        print("test pass")
    print()

    if split_by_separator("(a|\(|b|c)d|\||x|e|(d|f)") == ["(a|\(|b|c)d", "\|","x", "e", "(d|f)"]:
        print("test pass")
    print()

    if split_by_separator("a|\(|b|c") == ["a", "\(", "b", "c"]:
        print("test pass")
    print()


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
                # ovo se nikad nece ostvarit
                if i_0 == 0:
                    state_of_brackets -= 1
                    t_0 = t_0[1:-1]
                    break
                    # print("kraj")

                elif s[i_0 - 1] != "\\":
                    state_of_brackets -= 1
                    t_0 = t_0[1:-1]
                    break
                    # print("kraj")

                # # znaci da je \)
                # else:
                #     print(token)

            # else:
            #     print(token)

    print("extracted: *" + t_0 + "*")

    return t_0


def test_extract_deepest_bracket_content():

    t = 0
    if extract_deepest_bracket_content("(a|\(|b|c)d|x") == "a|\(|b|c":
        print("test passed")
        t += 1

    if extract_deepest_bracket_content("(a|\(|b|c)d|x|e") == "a|\(|b|c":
        print("test passed")

        t += 1

    if extract_deepest_bracket_content("(a|\(|b|c)d|x|e|(d|f)") == "a|\(|b|c":
        print("test passed")

        t += 1

    if extract_deepest_bracket_content("(a|\(|b|c)d|\||x|e|(d|f)") == "a|\(|b|c":
        print("test passed")

        t += 1

    # 5
    if extract_deepest_bracket_content("a|\(|b|c") == "a|\(|b|c":
        print("test passed")
        t += 1

    # 5
    if extract_deepest_bracket_content("a|\((|b(D(E|(F)))|c)") == "F":
        print("test passed")
        t += 1

    print("test", t)


# todo
def check_len_regex(s):
    pass


def test_check_len_regex():
    t = 0
    if check_len_regex("0|1|2|3|4|5|6|7|8|9") == ["1", ""]:
        print("test passed")
        t += 1

    if check_len_regex("0|1|2|3|4|5|6|7|48|9") == ["2", "48"]:
        print("test passed")

        t += 1

    if check_len_regex("0|1|2|3|4|5|6[abc]|7|48|9") == "a|\(|b|c":
        print("test passed")

        t += 1

    if check_len_regex("(a|\(|b|c)d|\||x|e|(d|f)") == "a|\(|b|c":
        print("test passed")

        t += 1

    # 5
    if check_len_regex("a|\(|b|c") == "a|\(|b|c":
        print("test passed")
        t += 1

    # 5
    if check_len_regex("a|\((|b(D(E|(F)))|c)") == "F":
        print("test passed")
        t += 1

    print("test", t)


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

                if state != 1:
                    index_start = i_0
                    state = 1

            elif s[i_0 - 1] != "\\":
                state_of_brackets += 1

                if state != 1:
                    index_start = i_0
                    state = 1

            # # znaci da je \(
            # else:
            #     print(token)

        elif token == ")":
            # ovo se nikad nece ostvarit
            if i_0 == 0:
                state_of_brackets -= 1

            elif s[i_0 - 1] != "\\":
                state_of_brackets -= 1

            if state_of_brackets == 0:
                index_end = i_0
                break

            # # znaci da je \)
            # else:
            #     print(token)

        # else:
        #     print(token)

        if state == 1:
            content += token

    ret = [index_start, index_end, content[1:]]

    print("bracket_handler", ret)
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


# input "avnej|dw|"
# output True
def is_separator_present(s):
    for i_0, token_0 in enumerate(s):

        if token_0 == "|":

            if i_0 == 0:
                return True

            elif s[i_0 - 1] != "\\":
                return True

    return False


# dynamic prog
# ret = list()
def regex_driver(s):
    # ret = list()
    print(["input", s])

    # sr: micanje zagrade s pocetka i kraja

    t_0 = bracket_handler(s)
    if t_0[0] == 0 and t_0[1] == len(s) - 1:
        t_1 = s[t_0[0] + 1: t_0[1]]
        print(["rekurzija", t_1])
        return regex_driver(t_1)

    ret = split_by_separator(s)

    new_ret = list()
    for i_1, token_1 in enumerate(ret):

        if is_separator_present(token_1):
            print(["handle this", token_1])
            new_ret.append(token_1)

        else:
            new_ret.append(token_1)


    # print("ret", ret)
    print("ret")
    [print([i]) for i in new_ret]

    return new_ret


if __name__ == '__main__':
    # test_refractor()

    #
    # test_split_by_separator()
    # import sys
    # sys.exit()

    # ['\\t|\\_']
    # ['\\n']
    # ['#\\|']
    # ['\\|#']
    # ['\\n']
    # ['(\\(|\\)|\\{|\\}|\\||\\*|\\\\|\\$|\\t|\\n|\\_|!|"|#|%|&|\'|+|,|-|.|/|0|1|2|3|4|5|6|7|8|9|:|;|<|=|>|?|@|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|[|]|^|_|`|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|~)']
    # ['((0|1|2|3|4|5|6|7|8|9)(0|1|2|3|4|5|6|7|8|9)*|0x((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D|E|F)((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D|E|F)*)']
    # ['\\(']
    # ['\\)']
    # ['-']
    # ['-(\\t|\\n|\\_)*-']
    # ['\\((\\t|\\n|\\_)*-']
    # ['\\t|\\_']
    # ['\\n']
    # ['-']
    # ['-(\\t|\\n|\\_)*-']

    s = [
        "\\t|\\_",
        "\\n",
        "#\|",
        "\|#",
        "\\n",
        "(\\(|\\)|\\{|\\}|\\||\\*|\\\\|\\$|\\t|\\n|\\_|!|\"|#|%|&|\'|+|,|-|.|/|0|1|2|3|4|5|6|7|8|9|:|;|<|=|>|?|@|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|[|]|^|_|`|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|~)",
        "((0|1|2|3|4|5|6|7|8|9)(0|1|2|3|4|5|6|7|8|9)*|0x((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D|E|F)((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D|E|F)*)",
        "\(",
        "\)",
        "-",
        "-(\\t|\\n|\_)*-",
        "\((\\t|\\n|\_)*-",
        "\\t|\_",
        "\\n",
        "-",
        "-(\\t|\\n|\_)*-"
    ]

    for i_0 in s:
        c = regex_driver(i_0)
        print()

# test_bracket_handler()
# regex_driver("c")

# for i in "0|1|2|3|4|5|6|7|8|9|a|b|c|d|e|f|A|B|C|D|E|F".split("|"):
#     print("S_4, " + str(i) + " -> S_4")

# S_0, 0 -> S_1
# S_0, 1 -> S_1
# S_0, 2 -> S_1
# S_0, 3 -> S_1
# S_0, 4 -> S_1
# S_0, 5 -> S_1
# S_0, 6 -> S_1
# S_0, 7 -> S_1
# S_0, 8 -> S_1
# S_0, 9 -> S_1

# S_1, 0 -> S_1
# S_1, 1 -> S_1
# S_1, 2 -> S_1
# S_1, 3 -> S_1
# S_1, 4 -> S_1
# S_1, 5 -> S_1
# S_1, 6 -> S_1
# S_1, 7 -> S_1
# S_1, 8 -> S_1
# S_1, 9 -> S_1

# S_1, S_4 prihvatljivo

# S_0, 0 -> S_2
# S_2, x -> S_3
# S_3, 0 -> S_4
# S_3, 1 -> S_4
# S_3, 2 -> S_4
# S_3, 3 -> S_4
# S_3, 4 -> S_4
# S_3, 5 -> S_4
# S_3, 6 -> S_4
# S_3, 7 -> S_4
# S_3, 8 -> S_4
# S_3, 9 -> S_4
# S_3, a -> S_4
# S_3, b -> S_4
# S_3, c -> S_4
# S_3, d -> S_4
# S_3, e -> S_4
# S_3, f -> S_4
# S_3, A -> S_4
# S_3, B -> S_4
# S_3, C -> S_4
# S_3, D -> S_4
# S_3, E -> S_4
# S_3, F -> S_4
# S_4, 0 -> S_4
# S_4, 1 -> S_4
# S_4, 2 -> S_4
# S_4, 3 -> S_4
# S_4, 4 -> S_4
# S_4, 5 -> S_4
# S_4, 6 -> S_4
# S_4, 7 -> S_4
# S_4, 8 -> S_4
# S_4, 9 -> S_4
# S_4, a -> S_4
# S_4, b -> S_4
# S_4, c -> S_4
# S_4, d -> S_4
# S_4, e -> S_4
# S_4, f -> S_4
# S_4, A -> S_4
# S_4, B -> S_4
# S_4, C -> S_4
# S_4, D -> S_4
# S_4, E -> S_4
# S_4, F -> S_4

# test_extract_deepest_bracket_content()

# r1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# r2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#
#
#
# for tweet in tweets:
#     ...
#     if tweet.startswith("coffee", 7):
#         ...
#     print(tweet)
#
#
#
#
#
# def analyze_letters(main_buffer):
#     pointer = 0
#     try:
#         while main_buffer[pointer].isalnum():
#             pointer += 1
#     except:
#         pass
#
#     buffer = main_buffer[:pointer]
#     OUTPUT.append("IDN " + str(ROW) + " " + str().join(buffer))
#
#     main_buffer = main_buffer[pointer:]
#     return main_buffer
#
#
# def analyze(input):
#     global ROW, OUTPUT
#
#     main_buffer = list(str(input))
#     OUTPUT.clear()
#     try:
#         while True:
#             if main_buffer[0] == "/" and main_buffer[1] == "/":
#                 main_buffer = main_buffer[main_buffer.index("\n") + 1:]
#                 ROW += 1
#
#             elif main_buffer[0] in {"\t", " ", "\n"}:
#                 ROW += 1 if main_buffer[0] == "\n" else 0
#                 main_buffer = main_buffer[1:]
#
#             elif main_buffer[0] in "zaod" and main_buffer[1] in "zaod" and main_buffer[2] in {" ", "\n", "\t"}:
#                 id = main_buffer[0] + main_buffer[1]
#                 if id in {"za", "az", "od", "do"}:
#                     OUTPUT.append("KR_" + str(id).upper() + " " + str(ROW) + " " + id)
#                 main_buffer = main_buffer[2:] if id in {"za", "az", "od", "do"} else analyze_letters(main_buffer)
#             #     main buffer = za, az, od, do ili nesto sta nije idn
#
#
#             elif main_buffer[0].isnumeric():
#                 pointer = 0
#                 try:
#                     while main_buffer[pointer].isnumeric():
#                         pointer += 1
#                 except:
#                     pass
#                 OUTPUT.append("BROJ " + str(ROW) + " " + str().join(main_buffer[:pointer]))
#                 main_buffer = main_buffer[pointer:]
#
#             elif main_buffer[0] in "()/*-+=":
#                 if main_buffer[0] == ")":
#                     OUTPUT.append("D_ZAGRADA " + str(ROW) + " )")
#                 elif main_buffer[0] == "(":
#                     OUTPUT.append("L_ZAGRADA " + str(ROW) + " (")
#                 elif main_buffer[0] == "*":
#                     OUTPUT.append("OP_PUTA " + str(ROW) + " *")
#                 elif main_buffer[0] == "/":
#                     OUTPUT.append("OP_DIJELI " + str(ROW) + " /")
#                 elif main_buffer[0] == "+":
#                     OUTPUT.append("OP_PLUS " + str(ROW) + " +")
#                 elif main_buffer[0] == "=":
#                     OUTPUT.append("OP_PRIDRUZI " + str(ROW) + " =")
#                 elif main_buffer[0] == "-":
#                     OUTPUT.append("OP_MINUS " + str(ROW) + " -")
#                 main_buffer = main_buffer[1:]
#
#             elif main_buffer[0].isalpha():
#                 main_buffer = analyze_letters(main_buffer)
#     except:
#         return
