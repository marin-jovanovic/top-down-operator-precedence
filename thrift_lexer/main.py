import re
from resources.resource_constants import TOKENS
from resources.token_classes import Token, KeywordToken
import resources.token_classes


# def class_definer(keyword_id, row_number, keyword, is_regex, source_code, match, regex=""):
#     # print(keyword)
#     print(keyword_id, keyword, match)
#     value = keyword
#
#     if len(keyword.split(" ")) == 1:
#         # if keyword_id == "NameSpaceScope":
#         #     return resources.token_classes.NamespaceScopeToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id in (("*", "c_glib", "cpp", "delphi", "haxe", "go", "java", "js", "lua", "netstd", "perl",
#         #                      "php", "py.twisted", "py", "rb", "st", "xsd")):
#         #     return resources.token_classes.NamespaceScopeToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == "=":
#         #     return resources.token_classes.EqualToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == "{":
#         #     return resources.token_classes.LeftCurlyBracketToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == "}":
#         #     return resources.token_classes.RightCurlyBracketToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == "(":
#         #     return resources.token_classes.LeftRoundBracketToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == ")":
#         #     return resources.token_classes.RightRoundBracketToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == "[":
#         #     return resources.token_classes.LeftSquareBracketToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == "]":
#         #     return resources.token_classes.RightSquareBracketToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == "<":
#         #     return resources.token_classes.LeftAngleBracketToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == ">":
#         #     return resources.token_classes.RightAngleBracketToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == "<":
#         #     return resources.token_classes.LeftAngleBracketToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == ":":
#         #     return resources.token_classes.ColonToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id in (("required", "optional")):
#         #     return resources.token_classes.FieldReqToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id in (("bool", "byte", "i8", "i16", "i32", "i64", "double", "string", "binary", "slist")):
#         #     return resources.token_classes.BaseTypeToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id in ((",", ";")):
#         #     return resources.token_classes.CommaToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == "+":
#         #     return resources.token_classes.PlusToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == "-":
#         #     return resources.token_classes.MinusToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == ".":
#         #     return resources.token_classes.DotToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == "e":
#         #     return resources.token_classes.LowerEToken(keyword_id, row_number, match)
#         #
#         # elif keyword_id == "E":
#         #     return resources.token_classes.UpperEToken(keyword_id, row_number, match)
#         #
#         # # elif keyword_id == ".":
#         # #     return resources.token_classes.DotToken(keyword_id, row_number, value)
#
#     else:
#         # regex
#
#         keyword = keyword[2:]
#
#         # if re.match(keyword, source_code):
#         if keyword in (("\" [^\"]* \"", "\' [^\']* \'", "\"[^\"]*\"", "\'[^\']*\'")):
#             # if keyword == "\" [^\"]* \"" or keyword == "\' [^\']* \'" or
#             # keyword == "\"[^\"]*\"" or keyword == "\'[^\']*\'":
#             return resources.token_classes.LiteralToken(keyword_id, row_number, regex)
#
#         elif keyword == "([a-zA-Z]|_)([a-zA-Z]|[0-9]|\.|_)*":
#             return resources.token_classes.IdentifierToken(keyword_id, row_number, regex)
#
#         elif keyword == "([a-zA-Z]|_)([a-zA-Z]|[0-9]|\.|_|-)*":
#             return resources.token_classes.STIdentifierToken(keyword_id, row_number, regex)


def get_tokens(source_code_path):
    source_code = "".join([line for line in open(source_code_path).readlines()])
    output = []

    row_number = 1

    have_i_eaten = False

    while True:
        print(source_code.replace("\n", "\\n"))
        # print(source_code.split("\n"))

        if source_code == "":
            print("lexer; ok")
            break

        for keyword, keyword_id in TOKENS.items():
            if keyword == keyword_id and source_code.startswith(keyword):
                output.append(KeywordToken(keyword_id, row_number, keyword))
                source_code = source_code[len(keyword):]
                have_i_eaten = True
                break

        if not have_i_eaten:

            if source_code.startswith(("*", "c_glib", "cpp", "delphi", "haxe", "go", "java", "js", "lua",
                                       "netstd", "perl", "php", "py.twisted", "py", "rb", "st", "xsd")):

                t = ["*", "c_glib", "cpp", "delphi", "haxe", "go", "java", "js", "lua",
                                       "netstd", "perl", "php", "py.twisted", "py", "rb", "st", "xsd"]
                for elem in t:
                    if source_code.startswith(elem):
                        output.append(resources.token_classes.NamespaceScopeToken("NamespaceScope",
                                                                                  row_number, elem))
                        source_code = source_code[len(elem):]
                        break

                have_i_eaten = True

            elif source_code.startswith("="):
                output.append(resources.token_classes.EqualToken("equal", row_number, "="))
                source_code = source_code[1:]

                have_i_eaten = True

            elif source_code.startswith("{"):
                output.append(resources.token_classes.LeftCurlyBracketToken("left_curly_bracket", row_number, "{"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("}"):
                output.append(resources.token_classes.RightCurlyBracketToken("right_curly_bracket", row_number, "}"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("("):
                output.append(resources.token_classes.LeftRoundBracketToken("left_round_bracket", row_number, "("))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith(")"):
                output.append(resources.token_classes.RightRoundBracketToken("right_round_bracket", row_number, ")"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("["):
                output.append(resources.token_classes.LeftSquareBracketToken("left_square_bracket", row_number, "["))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("]"):
                output.append(resources.token_classes.RightSquareBracketToken("right_square_bracket", row_number, "]"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("<"):
                output.append(resources.token_classes.LeftAngleBracketToken("left_angle_bracket", row_number, "<"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith(">"):
                output.append(resources.token_classes.RightAngleBracketToken("right_angle_bracket", row_number, ">"))
                source_code = source_code[1:]
                have_i_eaten = True

            # elif source_code.startswith("<"):
            #     output.append(resources.token_classes.LeftAngleBracketToken(keyword_id, row_number, match))
            #     source_code = source_code[1:]
            #     have_i_eaten = True

            elif source_code.startswith(":"):
                output.append(resources.token_classes.ColonToken("colon", row_number, ":"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith(("required", "optional")):

                t = ["required", "optional"]

                for elem in t:
                    if source_code.startswith(elem):
                        output.append(resources.token_classes.NamespaceScopeToken("FieldReq",
                                                                                  row_number, elem))
                        source_code = source_code[len(elem):]
                        break

                have_i_eaten = True

            elif source_code.startswith(("bool", "byte", "i8", "i16", "i32", "i64", "double", "string",
                                         "binary", "slist")):


                t = ["bool", "byte", "i8", "i16", "i32", "i64", "double", "string",
                                         "binary", "slist"]
                for elem in t:
                    if source_code.startswith(elem):
                        output.append(resources.token_classes.BaseTypeToken("BaseType", row_number, elem))
                        source_code = source_code[len(elem):]
                        break

                have_i_eaten = True

            # fixme comma vs list separator
            elif source_code.startswith((",", ";")):
                t = [",", ";"]
                for elem in t:
                    if source_code.startswith(elem):
                        output.append(resources.token_classes.BaseTypeToken("ListSeparator", row_number, elem))
                        source_code = source_code[len(elem):]
                        break

                # output.append(resources.token_classes.CommaToken(keyword_id, row_number, match))
                # source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("+"):
                output.append(resources.token_classes.PlusToken("plus", row_number, "+"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("-"):
                output.append(resources.token_classes.MinusToken("minus", row_number, "-"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("."):
                output.append(resources.token_classes.DotToken("dot", row_number, "."))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("e"):
                output.append(resources.token_classes.LowerEToken("lower_e", row_number, "e"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("E"):
                output.append(resources.token_classes.UpperEToken("upper_e", row_number, "E"))
                source_code = source_code[1:]
                have_i_eaten = True

            # functional actions
            elif source_code.startswith((" ", "\t")):
                # space, indentation

                source_code = source_code[1:]

                have_i_eaten = True

            elif source_code.startswith("\n"):
                # new row

                source_code = source_code[1:]
                row_number += 1

                have_i_eaten = True

            elif source_code.startswith("#") or source_code.startswith("//"):
                # single line comment

                while not source_code.startswith("\n"):
                    source_code = source_code[1:]

                source_code = source_code[1:]
                row_number += 1
                have_i_eaten = True

            elif source_code.startswith("/*"):
                # multiline comment

                source_code = source_code[2:]
                # todo check if row starts with "*"
                while not source_code.startswith("*/"):
                    if source_code.startswith("\n"):
                        row_number += 1
                    source_code = source_code[1:]

                # handles */
                source_code = source_code[2:]

                have_i_eaten = True

            else:
                # regex

                keyword = keyword[2:]

                if re.match("\" [^\"]* \"", source_code):
                    t = source_code[:re.match("\" [^\"]* \"", source_code).end()]
                    output.append(resources.token_classes.LiteralToken("Literal", row_number, t))
                    source_code = regex_cropper("\" [^\"]* \"", source_code)

                elif re.match("\' [^\']* \'", source_code):
                    t = source_code[:re.match("\' [^\']* \'", source_code).end()]

                    output.append(resources.token_classes.LiteralToken("Literal", row_number, t))
                    source_code = regex_cropper("\' [^\']* \'", source_code)

                elif re.match("\"[^\"]*\"", source_code):
                    t = source_code[:re.match("\"[^\"]*\"", source_code).end()]
                    output.append(resources.token_classes.LiteralToken("Literal", row_number, t))
                    source_code = regex_cropper("\"[^\"]*\"", source_code)

                elif re.match("\'[^\']*\'", source_code):
                    t = source_code[:re.match("\'[^\']*\'", source_code).end()]
                    output.append(resources.token_classes.LiteralToken("Literal", row_number, t))
                    source_code = regex_cropper("\'[^\']*\'", source_code)

                elif re.match("([a-zA-Z]|_)([a-zA-Z]|[0-9]|\.|_)*", source_code):
                    t = source_code[:re.match("([a-zA-Z]|_)([a-zA-Z]|[0-9]|\.|_)*", source_code).end()]
                    output.append(resources.token_classes.IdentifierToken("Identifier", row_number, t))
                    source_code = regex_cropper("([a-zA-Z]|_)([a-zA-Z]|[0-9]|\.|_)*", source_code)

                elif re.match("([a-zA-Z]|_)([a-zA-Z]|[0-9]|\.|_|-)*", source_code):
                    t = source_code[:re.match("([a-zA-Z]|_)([a-zA-Z]|[0-9]|\.|_|-)*", source_code).end()]

                    output.append(resources.token_classes.STIdentifierToken("STIdentifier", row_number, t))
                    source_code = regex_cropper("([a-zA-Z]|_)([a-zA-Z]|[0-9]|\.|_|-)*", source_code)

                elif re.match("[a-zA-Z]", source_code):
                    t = source_code[:re.match("[a-zA-Z]", source_code).end()]

                    output.append(resources.token_classes.LetterToken("Letter", row_number, t))
                    source_code = regex_cropper("[a-zA-Z]", source_code)

                elif re.match("[0-9]", source_code):
                    t = source_code[:re.match("[0-9]", source_code).end()]

                    output.append(resources.token_classes.DigitToken("Digit", row_number, t))

                    source_code = regex_cropper("[0-9]", source_code)

                else:
                    pass

                have_i_eaten = True



            # for keyword, keyword_id in TOKENS.items():
        #
        #     if keyword == keyword_id and source_code.startswith(keyword):
        #         # keyword
        #
        #         output.append(KeywordToken(keyword_id, row_number, keyword))
        #
        #     elif len(keyword.split(" ")) == 1:
        #         # direct match
        #
        #         # if source_code.startswith(keyword):
        #         #     fixed
        #         match = source_code[:len(keyword)]
        #         output.append(class_definer(keyword_id, row_number, keyword, False, source_code, match))
        #         output.append(Token("0**" + keyword_id, row_number, keyword))
        #         source_code = source_code[len(keyword):]
        #
        #         have_i_eaten = True
        #         break
        #
        #
        #
        #     else:
        #         # regex match
        #
        #         regex = keyword[2:]
        #         # if re.match(regex, source_code):
        #         output.append(class_definer(keyword_id,
        #                                     row_number,
        #                                     keyword,
        #                                     True,
        #                                     source_code,
        #                                     source_code[:re.match(regex, source_code).end()]
        #         ))
        #         output.append(Token("1**" + keyword_id, row_number,
        #                             source_code[:re.match(regex, source_code).end()]))
        #         source_code = regex_cropper(regex, source_code)
        #
        #         have_i_eaten = True
        #         break



        if not have_i_eaten:
            print("error while lexing?")
            break

        have_i_eaten = False

    # print(source_code.split("\n"))

    return output


def regex_cropper(regex, string):
    return string[re.match(regex, string).end():] if re.match(regex, string) else string


if __name__ == '__main__':
    # print("*** tokens ***")

    # [print(k + " -> " + v) for k, v in TOKENS.items()]
    #

    # keyword -> keyword_id
    # double -> BaseType
    # string -> BaseType
    # binary -> BaseType
    # slist -> BaseType
    # map -> map
    # set -> set
    # , -> ListSeparator
    # list -> list
    # cpp_type -> cpp_type
    # + -> plus
    # - -> minus
    # .-> dot
    # E -> upper_e
    # e -> lower_e
    # r \" [^\"]* \" -> Literal
    # r \' [^\']* \' -> Literal
    # r \"[^\"]*\" -> Literal
    # r \'[^\']*\' -> Literal
    # r([a - zA - Z] | _)([a - zA - Z] | [0 - 9] |\.| _) * -> Identifier
    # r([a - zA - Z] | _)([a - zA - Z] | [0 - 9] |\.| _ | -) * -> STIdentifier
    # ; -> ListSeparator
    # r[a - zA - Z] -> Letter
    # r[0 - 9] -> Digit

    #
    # print("\n*** source code ***")
    # print(SOURCE_CODE)

    [print(i) for i in get_tokens("../resources/thrift_source_code_samples\\code4.thrift")]
