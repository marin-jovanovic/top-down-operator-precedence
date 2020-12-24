OUTPUT = list()
ROW = 1

# \_ je razmak
# ['S_pocetno', 'a|ab', ['-']]


# ['S_pocetno', '\\t|\\_', ['-']]
# ['S_pocetno', '\\n', ['-', 'NOVI_REDAK']]
# ['S_pocetno', '#\\|', ['-', 'UDJI_U_STANJE S_komentar']]
# ['S_komentar', '\\|#', ['-', 'UDJI_U_STANJE S_pocetno']]
# ['S_komentar', '\\n', ['-', 'NOVI_REDAK']]
# ['S_komentar', '(\\(|\\)|\\{|\\}|\\||\\*|\\\\|\\$|\\t|\\n|\\_|!|"|#|%|&|\'|+|,|-|.|/|0|1|2|3|4|5|6|7|8|9|:|;|<|=|>|?|@|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|[|]|^|_|`|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|~)', ['-']]
# ['S_pocetno', '((0|1|2|3|4|5|6|7|8|9)(0|1|2|3|4|5|6|7|8|9)*|0x((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D|E|F)((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D|E|F)*)', ['OPERAND']]
# ['S_pocetno', '\\(', ['LIJEVA_ZAGRADA']]
# ['S_pocetno', '\\)', ['DESNA_ZAGRADA']]
# ['S_pocetno', '-', ['OP_MINUS']]
# ['S_pocetno', '-(\\t|\\n|\\_)*-', ['OP_MINUS', 'UDJI_U_STANJE S_unarni', 'VRATI_SE 1']]
# ['S_pocetno', '\\((\\t|\\n|\\_)*-', ['LIJEVA_ZAGRADA', 'UDJI_U_STANJE S_unarni', 'VRATI_SE 1']]
# ['S_unarni', '\\t|\\_', ['-']]
# ['S_unarni', '\\n', ['-', 'NOVI_REDAK']]
# ['S_unarni', '-', ['UMINUS', 'UDJI_U_STANJE S_pocetno']]
# ['S_unarni', '-(\\t|\\n|\\_)*-', ['UMINUS', 'VRATI_SE 1']]

import sys
def driver():
    state = "S_pocetno"
    source = "".join([i for i in open("minusLang.in").readlines()])
    print(source)

    [print(list(i)) for i in open("minusLang.in").readlines()]

    # sys.exit()

    if state == "S_pocetno":
        if source.startswith(("\t", " ")):
            print(1)
            pass

        if source.startswith("\n"):
            print(2)
            print("novi redak")

        if source.startswith("#|"):
            print(3)
            state = "S_komentar"
            source = source[2:]

    if state == "S_komentar":
        if source.startswith("|#"):
            print(4)
            state = "S_pocetno"
            source = source[2:]

        if source.startswith("\n"):
            print(5)
            print("novi redak")


def split_by_separator(v_regex):

    state_of_brackets = 0

    t_0 = ""

    print(v_regex)
    ret = list()

    for iterator_1, token in enumerate(v_regex):
        print(token)
        t_0 += token
        if token == "(":
            if iterator_1 == 0:
                state_of_brackets += 1
                print("zagrada")

            elif v_regex[iterator_1 - 1] != "\\":
                state_of_brackets += 1
                print("zagrada")

        elif token == ")":
            if iterator_1 == 0:
                pass

            elif v_regex[iterator_1 - 1] != "\\":
                state_of_brackets -= 1
                print("zagrada")

        elif token == "|":

            if state_of_brackets == 0 and v_regex[iterator_1 - 1] != "\\":

                ret.append("".join([i for i in t_0[:-1]]))
                print("dodajem", "".join([i for i in t_0[:-1]]))
                print("split")
                t_0 = ""
        else:
            pass

    ret.append("".join([i for i in t_0]))
    print("ret", ret)
    # [print(i) for i in ret]
    return ret


def test_split_by_separator():

    split_by_separator("(a|\(|b|c)d|x")

    t = 0
    if split_by_separator("(a|\(|b|c)d|x") == ["(a|\(|b|c)d", "x"]:
        t += 1

    if split_by_separator("(a|\(|b|c)d|x|e") == ["(a|\(|b|c)d", "x", "e"]:
        t += 1

    if split_by_separator("(a|\(|b|c)d|x|e|(d|f)") == ["(a|\(|b|c)d", "x", "e", "(d|f)"]:
        t += 1

    if split_by_separator("(a|\(|b|c)d|\||x|e|(d|f)") == ["(a|\(|b|c)d", "\|","x", "e", "(d|f)"]:
        t += 1

    # 5
    if split_by_separator("a|\(|b|c") == ["a", "\(", "b", "c"]:
        t += 1

    print("test", t)


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

# extract_deepest_bracket_content("((0|1|2|3|4|5|6|7|8|9)(0|1|2|3|4|5|6|7|8|9)*|"
#     "# 0x((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D|E|F)((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D|E|F)*)")


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
