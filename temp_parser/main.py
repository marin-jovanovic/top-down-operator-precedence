import re

from drivers.resource_constants import KEYWORDS_PREFIX, TOKENS

# fixme nested comments in parser


###########
# token classes
###########

SPACE


LBP = {
    "KeywordToken": 0,
    "BaseTypeToken": 0,
    "EOFToken": -1
}


class Token(object):

    def __init__(self, identifier, row, value):
        self.identifier = identifier
        self.row = row
        self.value = value
        self.lbp = LBP.get(self.__class__.__name__)

    def __str__(self):
        return self.identifier + " " + str(self.row) + " " + self.value


class BaseTypeToken(Token):

    def nud(self):

        print("current", token)


class CommaToken(Token):
    pass


class ColonToken(Token):
    pass


class ConstValueToken(object):
    pass


class DotToken(Token):
    pass


class DigitToken(Token):
    pass


class EqualToken(Token):
    pass


class EOFToken(Token):

    # @staticmethod
    def nud(self):
        return ["EOF"]

    def __str__(self):
        return "EOF token"


class FieldReqToken(Token):
    pass


# class FieldTypeToken(Token):
#     pass


class IdentifierToken(Token):
    pass



def match_by_name(expected_token):
    print("+++ matcher +++")

    global token
    token = get_next_token()
    return "todo"


class KeywordToken(Token):

    def __init__(self, identifier, row, value):
        super().__init__(KEYWORDS_PREFIX + identifier, row, value)

    def nud(self):
        print("+++ KeywordToken +++")

        if self.value == "namespace":

            v1 = match(NamespaceScopeToken)
            v2 = match(IdentifierToken)

            print(["namespace", v1, v2])
            print("next", token)

            return [["namespace", v1, v2], expression()]

        elif self.value == "include":

            v1 = match(LiteralToken)

            print(["include", v1])

            return [["include", v1], expression()]

        elif self.value == "cpp_include":

            v1 = match(LiteralToken)

            print(["cpp_include", v1])

            return [["cpp_include", v1], expression()]

        else:
            import sys
            sys.exit()


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


class LiteralToken(Token):
    pass


class ListSeparatorToken(Token):
    pass


class LetterToken(Token):
    pass


class NamespaceScopeToken(Token):
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


class UpperEToken(Token):
    pass


###########
# lexer
###########


def regex_cropper(regex, string):
    return string[re.match(regex, string).end():] if re.match(regex, string) else string


def get_tokens(source_code_path):
    print("\033[92m+++ LEXER +++\033[0m")

    '''string of source code'''
    source_code = "".join([line for line in open(source_code_path).readlines()])
    output = []

    row_number = 1

    have_i_eaten = False

    while True:
        print(source_code.replace("\n", "\\n"))

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
                        output.append(NamespaceScopeToken("NamespaceScope", row_number, elem))
                        source_code = source_code[len(elem):]
                        break

                have_i_eaten = True

            elif source_code.startswith("="):
                output.append(EqualToken("equal", row_number, "="))
                source_code = source_code[1:]

                have_i_eaten = True

            elif source_code.startswith("{"):
                output.append(LeftCurlyBracketToken("left_curly_bracket", row_number, "{"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("}"):
                output.append(RightCurlyBracketToken("right_curly_bracket", row_number, "}"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("("):
                output.append(LeftRoundBracketToken("left_round_bracket", row_number, "("))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith(")"):
                output.append(RightRoundBracketToken("right_round_bracket", row_number, ")"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("["):
                output.append(LeftSquareBracketToken("left_square_bracket", row_number, "["))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("]"):
                output.append(RightSquareBracketToken("right_square_bracket", row_number, "]"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("<"):
                output.append(LeftAngleBracketToken("left_angle_bracket", row_number, "<"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith(">"):
                output.append(RightAngleBracketToken("right_angle_bracket", row_number, ">"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith(":"):
                output.append(ColonToken("colon", row_number, ":"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith(("required", "optional")):

                t = ["required", "optional"]

                for elem in t:
                    if source_code.startswith(elem):
                        output.append(NamespaceScopeToken("FieldReq",
                                                          row_number, elem))
                        source_code = source_code[len(elem):]
                        break

                have_i_eaten = True

            elif source_code.startswith(("bool", "byte", "i8", "i16", "i32", "i64", "double", "string",
                                         "binary", "slist")):

                t = ["bool", "byte", "i8", "i16", "i32", "i64", "double", "string", "binary", "slist"]
                for elem in t:
                    if source_code.startswith(elem):
                        output.append(BaseTypeToken("BaseType", row_number, elem))
                        source_code = source_code[len(elem):]
                        break

                have_i_eaten = True

            # fixme comma vs list separator
            elif source_code.startswith((",", ";")):
                t = [",", ";"]
                for elem in t:
                    if source_code.startswith(elem):
                        output.append(BaseTypeToken("ListSeparator", row_number, elem))
                        source_code = source_code[len(elem):]
                        break

                # output.append(resources.token_classes.CommaToken(keyword_id, row_number, match))
                # source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("+"):
                output.append(PlusToken("plus", row_number, "+"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("-"):
                output.append(MinusToken("minus", row_number, "-"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("."):
                output.append(DotToken("dot", row_number, "."))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("e"):
                output.append(LowerEToken("lower_e", row_number, "e"))
                source_code = source_code[1:]
                have_i_eaten = True

            elif source_code.startswith("E"):
                output.append(UpperEToken("upper_e", row_number, "E"))
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

                # regex = "\' [^\']* \'"
                # token = resources.token_classes.DigitToken("Digit", row_number, "t")

                if re.match("\" [^\"]* \"", source_code):
                    t = source_code[:re.match("\" [^\"]* \"", source_code).end()]
                    output.append(LiteralToken("Literal", row_number, t))
                    source_code = regex_cropper("\" [^\"]* \"", source_code)

                # elif re.match(regex, source_code):
                #     t = source_code[:re.match(regex, source_code).end()]
                #     output.append(resources.token_classes.LiteralToken("Literal", row_number, t))
                #     source_code = regex_cropper(regex, source_code)

                elif re.match("\' [^\']* \'", source_code):
                    t = source_code[:re.match("\' [^\']* \'", source_code).end()]
                    output.append(LiteralToken("Literal", row_number, t))
                    source_code = regex_cropper("\' [^\']* \'", source_code)

                elif re.match("\"[^\"]*\"", source_code):
                    t = source_code[:re.match("\"[^\"]*\"", source_code).end()]
                    output.append(LiteralToken("Literal", row_number, t))
                    source_code = regex_cropper("\"[^\"]*\"", source_code)

                elif re.match("\'[^\']*\'", source_code):
                    t = source_code[:re.match("\'[^\']*\'", source_code).end()]
                    output.append(LiteralToken("Literal", row_number, t))
                    source_code = regex_cropper("\'[^\']*\'", source_code)

                elif re.match("([a-zA-Z]|_)([a-zA-Z]|[0-9]|\.|_)*", source_code):
                    t = source_code[:re.match("([a-zA-Z]|_)([a-zA-Z]|[0-9]|\.|_)*", source_code).end()]
                    output.append(IdentifierToken("Identifier", row_number, t))
                    source_code = regex_cropper("([a-zA-Z]|_)([a-zA-Z]|[0-9]|\.|_)*", source_code)

                elif re.match("([a-zA-Z]|_)([a-zA-Z]|[0-9]|\.|_|-)*", source_code):
                    t = source_code[:re.match("([a-zA-Z]|_)([a-zA-Z]|[0-9]|\.|_|-)*", source_code).end()]
                    output.append(STIdentifierToken("STIdentifier", row_number, t))
                    source_code = regex_cropper("([a-zA-Z]|_)([a-zA-Z]|[0-9]|\.|_|-)*", source_code)

                elif re.match("[a-zA-Z]", source_code):
                    t = source_code[:re.match("[a-zA-Z]", source_code).end()]
                    output.append(LetterToken("Letter", row_number, t))
                    source_code = regex_cropper("[a-zA-Z]", source_code)

                elif re.match("[0-9]", source_code):
                    t = source_code[:re.match("[0-9]", source_code).end()]
                    output.append(DigitToken("Digit", row_number, t))
                    source_code = regex_cropper("[0-9]", source_code)

                else:
                    pass

                have_i_eaten = True

        if not have_i_eaten:
            print("error while lexing?")
            break

        have_i_eaten = False

    return output


###########
# parser
###########


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


class Error(object):

    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message


def match(tok=None):
    """
    checks if next token is expected token

    :param tok: expected token
    :return: void
    """
    global token

    if tok and tok != type(token):
        value = "err: skip"

    else:
        print("match for", token.value, "ok")

        value = token.value

    token = get_next_token()
    return value


def match_exact_current_t(value):
    global token

    print("+++ match_exact +++")
    print(value)
    print(token.value)

    if value != token.value:
        print("not expected value")
        raise SyntaxError("Expected " + str(value))
as

def get_ast():
    print("\033[92m+++ PARSER +++\033[0m")
    print()

    global tokens
    print("+++ tokens +++")
    [print(i) for i in tokens]
    print()

    global token
    token = get_next_token()
    print("+++ token +++\n" + str(token) + "\n")

    ret = expression()

    print("+++ output +++")
    print("output:", ret)

    return ret


def expression(rbp=0):
    """
    try matching by prefix for current token

    :param rbp:
    :return:
    """
    global token
    t = token
    token = get_next_token()
    left = t.nud()
    while rbp < token.lbp:
        t = token
        token = get_next_token()
        left = t.led(left)
    return left


if __name__ == '__main__':
    global tokens
    tokens = get_tokens("../resources/thrift_source_code_samples//reduced.thrift")

    global token
    global token_pointer
    token_pointer = 0

    ast = get_ast()

    print("+++ ast +++")
    print("Document")
    print(ast)
    print()