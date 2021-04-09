import re

from drivers.resource_constants import KEYWORDS_PREFIX, TOKENS
from thrift_parser.tools import print_blue, print_red, fn

NAMESPACE_PREFIX = "NS__"
BASETYPE_PREFIX = "BT__"
IDENTIFIER_PREFIX = "ID__"
# def __init__(self, identifier, row, value):
#     super().__init__(NAMESPACE_PREFIX + identifier, row, value)

ENABLE_LOG = False

LBP = {
    "Literal": 1,
    "NamespaceScope": 1,
    "EOF": -1,
    "Identifier": 1,
    "BaseType": 1,
    "Keyword": 1
    }

def isBaseTypeToken(data):
    return data in ["bool", "byte", "i8", "i16", "i32", "i64", "double", "string", "binary", "slist"]

HEADER_RBP = 0
DEFINITION_RBP = 0

err_message_not_same_type = "err: wrong type"
err_message_no_optional_t = "err: no optional token"


DEFINITION_STARTER_FLAG = False
''' token classes '''


class Token(object):

    def __init__(self, identifier, row, value):
        self.identifier = identifier
        self.row = row
        self.value = value

        # token has length of 5
        self.lbp = LBP.get(self.__class__.__name__[:-5])

    def __str__(self):
        return "{:20} {:10}   {:10}".format(self.identifier, self.row,
                                            self.value)

    def nud(self):
        print("todo nud for", self.__class__.__name__)
        import sys
        sys.exit()

    def led(self, left):
        print("todo led for", self.__class__.__name__)
        import sys
        sys.exit()


"""unused classes"""
class ColonToken(Token):
    pass


class DotToken(Token):
    pass


class DigitToken(Token):
    pass


class EqualToken(Token):
    pass


class FieldReqToken(Token):
    pass

class IntConstantToken(Token):
    pass


class LeftCurlyBracketToken(Token):
    pass


class LeftRoundBracketToken(Token):
    pass


class LeftSquareBracketToken(Token):
    pass


class LeftAngleBracketToken(Token):
    pass


class LowerEToken(Token):
    pass


class ListSeparatorToken(Token):
    pass


class LetterToken(Token):
    pass


class MinusToken(Token):
    pass


class PlusToken(Token):
    pass


class RightCurlyBracketToken(Token):
    pass


class RightRoundBracketToken(Token):
    pass


class RightSquareBracketToken(Token):
    pass


class RightAngleBracketToken(Token):
    pass


class STIdentifierToken(Token):
    pass


class UnderscoreToken(Token):
    pass


class UpperEToken(Token):
    pass


"""used classes"""


class BaseTypeToken(Token):

    def __init__(self, identifier, row, value):
        super().__init__(BASETYPE_PREFIX + identifier, row, value)

    def led(self, left):
        pass
        # return self.value

class IdentifierToken(Token):

    def __init__(self, identifier, row, value):
        super().__init__(IDENTIFIER_PREFIX + identifier, row, value)

    def led(self, left):
        pass
        # print("left", left)


        #
        # if left == "const":
        #     identifier = match(IdentifierToken)
        #
        #     equal = match(EqualToken)
        #
        #     if not optional_match(PlusToken) == err_message_no_optional_t:
        #
        #         return ["Definition", [
        #             "Const",
        #             ["\"const\"", "FieldType", ["Identifier", [self.value]],
        #              "Identifier", [identifier],
        #              equal, "ConstValue",
        #              ["IntConstant", ["+", match(DigitToken)]], "ListSeparator",
        #              [optional_match(ListSeparatorToken)]]
        #         ], "DefinitionManager", expression()]
        #
        #     elif not optional_match(MinusToken) == err_message_no_optional_t:
        #
        #         return ["Definition", [
        #             "Const",
        #             ["\"const\"", "FieldType", ["Identifier", [self.value]],
        #              "Identifier", [identifier],
        #              equal, "ConstValue",
        #              ["IntConstant", ["-", match(DigitToken)]], "ListSeparator",
        #              [optional_match(ListSeparatorToken)]]
        #         ], "DefinitionManager", expression()]
        #
        #     # constValue
        #
        #     return ["Definition", [
        #         "Const",
        #         ["\"const\"", "FieldType", ["Identifier", [self.value]],
        #          "Identifier", [identifier],
        #          equal, "ConstValue", [], "ListSeparator", []]
        #     ], "DefinitionManager", expression()]
        #
        # elif left == "service":
        #
        #     return ["Definition",
        #             ["Service", ["\"service\"", "Identifier", [self.identifier],
        #                          expression(),
        #                          match(LeftCurlyBracketToken),
        #                          "FunctionManager", expression(),
        #                          match(RightCurlyBracketToken)]],
        #             "DefinitionManager",
        #             expression()
        #             ]
        #
        # elif left == "enum":
        #
        #     return ["Definition",
        #             ["Enum", ["\"enum\"",
        #                       "Identifier",
        #                       [self.value],
        #                       match(LeftCurlyBracketToken),
        #                       "Identifier",
        #                       match(IdentifierToken)]
        #              ],
        #             "DefinitionManager",
        #             expression()
        #             ]
        #
        # elif isBaseTypeToken(left):
        #     print("left is base type token")
        #     # self.lbp = 5
        #
        #
        #
        # else:
        #     print(left)
        #
        #     print("IdentifierToken led err")
        #     import sys
        #     sys.exit()

    def nud(self):
        pass
        # print(self)
        #
        # return [
        #     "nud identifier", match(LeftCurlyBracketToken), "check todo", match(RightCurlyBracketToken),
        #
        # "caption manager",
        #
        #     expression(),
        #
        #     "caption manager"
        #
        # ]


class NamespaceScopeToken(Token):
    def __init__(self, identifier, row, value):
        super().__init__(NAMESPACE_PREFIX + identifier, row, value)

    def led(self, left):
        pass
        #
        # if left == "namespace":
        #
        #     return ["Header",
        #             ["Namespace", ["\"namespace\"", "NamespaceScope",
        #                            [self.value], "Identifier",
        #                            [match(IdentifierToken)]]],
        #             "HeaderManager",
        #             expression(HEADER_RBP),
        #             "definition part",
        #             expression()
        #             ]
        #
        # else:
        #
        #     print("namespacescope led err")
        #     import sys
        #     sys.exit()

"""
starting keywords for DefinitionManager
"""
DEFINITION_STARTERS = ["const", "typedef", "enum", "senum", "struct", "union",
                       "exception", "service"]


def printerr():
    print_red("err")
    import sys
    sys.exit()


class LiteralToken(Token):
    #
# enum i__dentifier { }
# typedef bool varijabla


    def led(self, left):
        print(self.__class__.__name__, "-- led --", left, "++", self.value)

        if left == "include":

            return ["Header", ["Include", [left, "Literal", [self.value]]], "HeaderManager", expression(HEADER_RBP)]

        else:
            printerr()
        # pass

        # print(self.__class__.__name__, "-- led --", left, "+++", self.value)
        #
        # if left == "include":
        #
        #     # print(token)
        #
        #     # check if next token is def starter
        #     if token.value in DEFINITION_STARTERS:
        #         # start with definitions
        #         print_blue("definition starter")
        #
        #         return ["Header",
        #                      ["Include", ["\"include\"", "Literal", [self.value]]],
        #                 "HeaderManager",
        #                      ["$"],
        #                 "DefinitionManager",
        #                     expression(HEADER_RBP)
        #                 ]
        #
        #     else:
        #         print_blue("not definition starter")
        #         return ["Header",
        #                 ["Include", ["\"include\"", "Literal", [self.value]]],
        #                 "HeaderManager",
        #                 expression(HEADER_RBP)
        #                 ]
        #
        #
        # elif left == "cpp_include":
        #
        #
        #     if token.value in DEFINITION_STARTERS:
        #         # start with definitions
        #
        #         return ["Header",
        #             ["CppInclude",
        #              ["\"cpp_include\"", "Literal", [self.value]]],
        #             "HeaderManager",
        #             ["$"],
        #                 "DefinitionManager",
        #                 expression(HEADER_RBP)
        #             ]
        #
        #     else:
        #         return ["Header",
        #             ["CppInclude",
        #              ["\"cpp_include\"", "Literal", [self.value]]],
        #             "HeaderManager",
        #             expression(HEADER_RBP)
        #             ]
        #
        # else:
        #     print("err led literal ")
        #     import sys
        #     sys.exit()

    def nud(self):
        pass

        #
        # print(self.__class__.__name__, "-- nud --", self.value)
        # # print("ffff")
        # # print(token)
        #
        # if isinstance(token, EOFToken):
        #     print("end of file")
        #     return ["eof confirm"]
        #
        #
        # import sys
        # sys.exit()


class KeywordToken(Token):

    def __init__(self, identifier, row, value):
        super().__init__(KEYWORDS_PREFIX + identifier, row, value)

    def led(self, left):
        print(self.__class__.__name__, "-- led --", left, "++", self.value)

        return self.value

    def nud(self):
        print(self.__class__.__name__, "-- nud --", self.value)

        if self.value == "include":
            return self.value

        else:
            printerr()

        pass

        # print(self.__class__.__name__, "-- nud --", self.value)
        #
        # if self.value == "include":
        #     return self.value
        #
        # elif self.value == "cpp_include":
        #     return self.value
        #
        # elif self.value == "namespace":
        #     return self.value
        #
        # print_red("--- definition part ---")
        #
        # """definition part"""
        #
        # if self.value == "const":
        #     return self.value
        #
        # elif self.value == "typedef":
        #     return self.value
        #
        # elif self.value == "enum":
        #     return self.value
        #
        # elif self.value == "senum":
        #     return self.value
        #
        # elif self.value == "struct":
        #     return self.value
        #
        # elif self.value == "union":
        #     return self.value
        #
        # elif self.value == "exception":
        #     return self.value
        #
        # elif self.value == "service":
        #     return self.value
        #
        # else:
        #     print("unexpected token in keyword token led")
        #     import sys
        #     sys.exit()


class EOFToken(Token):

    # @staticmethod
    def nud(self):
        return ["$ end of header instructions"]

    def __str__(self):
        return "EOF token"

"""other"""


def optional_match(expected_token):
    global token

    if isinstance(expected_token, type(token)):
        value = err_message_no_optional_t

    else:
        value = token.value
        token = get_next_token()

    return value


'''lexer'''


# def regex_cropper(regex, string):
#     return string[re.match(regex, string).end():] if
#     re.match(regex, string) else string


def get_tokens(source_code_path, enabled_log=False):
    if enabled_log:
        print("\033[92m+++ LEXER +++\033[0m")

    output = []
    row_number = 0

    # todo multiline comments and nested multiline comments,
    #  multiline comment starts with * ?
    # todo connected lines

    for line in open(source_code_path).read().split("\n"):
        row_number += 1

        print(row_number, line.split(" "))

        for t in line.split(" "):

            if t == "//":
                # single line comment
                break

            is_matched = False

            for k, v in TOKENS.items():
                if re.match(v, t):
                    exec("output.append(" + k + "Token(t, row_number, t))")
                    is_matched = True
                    break

            if not is_matched:
                print("no match")

    if enabled_log:
        print("lexing done")

    return output


'''parser'''


def get_next_token():
    """
    used instead of generator

    :return: next token
    """
    global token_pointer
    global tokens

    try:
        curr_token = tokens[token_pointer]
    except:
        print("no more tokens")
        return EOFToken("EOF", -1, "EOF")

    token_pointer += 1
    return curr_token


def match_multiple(expected_tokens=None):
    global token

    print(expected_tokens)

    if expected_tokens and type(token) in expected_tokens:
        print("match for ", token.value, "ok")
        print("match at index ", expected_tokens.index(type(token)))
        value = token.value

    else:
        value = "err: skip"

    token = get_next_token()
    return value


def match(tok=None):
    """
    checks if next token is expected token

    :param tok: expected token
    :return: void
    """
    global token

    if tok:
        print("flag 1")

    if isinstance(token, tok):
        print('flag 2')

    if isinstance(token, type(tok)):
        print("flag 3")

    if tok and isinstance(token, tok):
        # if tok and isinstance(tok, type(token)):
        # if tok and tok != type(token):
        value = "err: skip"

    else:

        value = token.value

    token = get_next_token()
    return value





def expression(rbp=0):
    """
    main driver

    try matching by prefix for current token

    :param rbp:
    :return:
    """
    global token

    left = token.nud()
    token = get_next_token()

    # t = token
    # token = get_next_token()
    # left = t.nud()

    try:
        rbp < token.lbp
    except TypeError:
        print_red("no lbp for")
        print(token)

        import sys
        sys.exit()

    while rbp < token.lbp:
        print("curr tree", left)
        # t = token
        # token = get_next_token()
        # left = t.led(left)

        left = token.led(left)
        token = get_next_token()

        try:
            rbp < token.lbp
        except TypeError:
            print_red("inside while ,no lbp for")
            print(token)

            import sys
            sys.exit()

    return left


"""other functions"""
def get_head_ast(enabled_log=False):
    if enabled_log:
        print("\033[92m+++ PARSER +++\033[0m")

    global token

    token = get_next_token()
    print(token)


    if isinstance(token, EOFToken):
        print_red("eof")
        return ["HeaderManager", ["$"], "DefinitionManager", ["$"]]

    return expression()

def run_tests():
    import os
    # global test_prefix

    test_prefix = "../tests/"

    print(os.listdir(test_prefix))

    for inp, out in zip(*[iter(os.listdir(test_prefix))] * 2):
        print(inp, out)

        if inp.endswith(".in"):
            ast = driver(test_prefix + inp, True)

        if out.endswith(".out"):
            test_lines = open(test_prefix + out).read().split("\n")[:-1]



        ast_printable = fn(ast)

        if ast_printable == test_lines:
            print_red("correct")

        else:
            print_red("error")
            print("ast", ast)
            print("a p", ast_printable)
            print("out", test_lines)
            # max width of lines in correct_output_line
            max_length = 0
            for correct_output_line in test_lines:
                if len(correct_output_line) > max_length:
                    max_length = len(correct_output_line)

            print("\n" + str("    ").rjust(2) + "left is correct")
            counter = 0
            for correct_output_line in test_lines:

                temp_len = max_length - len(correct_output_line)

                try:
                    print(str(counter).rjust(2) + "  " + correct_output_line +
                          (temp_len + 2) * " " + "| " + ast_printable[
                              counter])
                    if correct_output_line != ast_printable[counter]:
                        print("error occured in previous line")

                except IndexError:
                    print("index error")
                    break
                counter += 1
            import sys
            sys.exit()
            print()

        print(80 * "-")






def driver(file_path, enable_log=False):
    """load source code
    """
    if enable_log:
        print("opening", file_path)

    from os import path
    print(path.exists(file_path))

    # source
    source_code_path = file_path

    print("--- source code ---")

    print(open(source_code_path).read())

    """lexer
    """
    tokens = get_tokens(source_code_path)
    if enable_log:
        print()

    if enable_log:
        print_blue("--- tokens ---")
        [print(i) for i in tokens]
        print()

    """parser
    """

    ast = ["Documentation", get_head_ast()]


    return ast


if __name__ == '__main__':

    run_tests()
