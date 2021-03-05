import re

from drivers.resource_constants import KEYWORDS_PREFIX, TOKENS

# fixme nested comments in parser


###########
# token classes
###########

# todo space counter

SPACE_COUNTER = 0
PRINTER = []

LBP = {
    # "KeywordToken": 1
    "LiteralToken": 1
    ,
    "NamespaceScopeToken": 1

    # "BaseTypeToken": 0,
    ,
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


class ListTypeToken(Token):
    pass


class SetTypeToken(Token):
    pass


class MapTypeToken(Token):
    pass


class ContainerTypeToken(Token):
    pass


class DefinitionTypeToken(Token):
    pass


class FieldTypeToken(Token):
    pass


class ThrowsToken(Token):
    pass


class FunctionTypeToken(Token):
    pass


class XsdAttrsToken(Token):
    pass


class FunctionToken(Token):
    pass


class XsdFieldOptionsToken(Token):
    pass


class FieldIDToken(Token):
    pass


class FieldToken(Token):
    pass


class ServiceToken(Token):
    pass


class ExceptionToken(Token):
    pass


class UnionToken(Token):
    pass


class SenumToken(Token):
    pass


class DefinitionToken(Token):
    pass


class EnumToken(Token):
    pass


class TypedefToken(Token):
    pass


class ConstToken(Token):
    pass


class StructToken(Token):
    pass


class NamespaceToken(Token):
    pass


class IncludeToken(Token):
    pass


class HeaderToken(Token):
    pass


class CppIncludeToken(Token):
    pass


class DocumentToken(Token):
    pass


class CppTypeToken(Token):
    pass


class BaseTypeToken(Token):

    def nud(self):
        print("current", token)


class CommaToken(Token):
    pass


class DoubleConstantToken(Token):
    pass


class IntConstantToken(Token):
    pass


class ColonToken(Token):
    pass


class ConstListToken(Token):
    pass


class ConstMapToken(Token):
    pass


class ConstValueToken(Token):
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


class IdentifierToken(Token):

    def nud(self):
        print("id")


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


class UpperEToken(Token):
    pass


is_first_header = True
is_first_definition = True
class NamespaceScopeToken(Token):

    def led(self, left):

        if left == "namespace":

            return ["Header",
                    ["Include", ["\"include\"", "Literal", [self.value], "Identifier", match(IdentifierToken)]],
                    "HeaderManager",
                    expression()
            ]

        else:

            print("namespacescope led err")
            import sys
            sys.exit()

class LiteralToken(Token):

    def led(self, left):

        if left == "include":

            return ["Header",
                    ["Include", ["\"include\"", "Literal", [self.value]]],
                    "HeaderManager",
                    expression()
            ]

        elif left == "cpp_include":

            return ["Header",
                    ["CppInclude", ["\"cpp_include\"", "Literal", [self.value]]],
                    "HeaderManager",
                    expression()
            ]

        else:
            print("err led literal ")
            import sys
            sys.exit()

class KeywordToken(Token):

    def __init__(self, identifier, row, value):
        super().__init__(KEYWORDS_PREFIX + identifier, row, value)

    def nud(self):
        global is_first_header

        if self.value == "include":
            return self.value

        elif self.value == "cpp_include":
            return self.value

        elif self.value == "namespace":
            return self.value

        else:
            print("unexpected token in keyword token led")
            import sys
            sys.exit()


'''lexer'''


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
        # print(source_code.replace("\n", "\\n"))

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


'''parser'''


def starts_with(token):
    if isinstance(token, DigitToken):
        return DigitToken

    elif isinstance(token, LetterToken):
        return LetterToken

    elif isinstance(token, ListSeparatorToken):
        return ListSeparatorToken
    elif isinstance(token, STIdentifierToken):
        return STIdentifierToken
    elif isinstance(token, IdentifierToken):
        return IdentifierToken
    elif isinstance(token, LiteralToken):
        return LiteralToken
    elif isinstance(token, ConstMapToken):
        return "{"
    elif isinstance(token, ConstListToken):
        return "["
    elif isinstance(token, DoubleConstantToken):
        return ["+", "-", DigitToken, ".", "E", "e", None]
    elif isinstance(token, IntConstantToken):
        return ["+", "-", DigitToken]
    elif isinstance(token, ConstValueToken):
        return [starts_with(IntConstantToken),
                starts_with(DoubleConstantToken),
                starts_with(LiteralToken),
                starts_with(IdentifierToken),
                starts_with(ConstListToken),
                starts_with(ConstMapToken)]
    elif isinstance(token, CppTypeToken):
        return "cpp_type"
    elif isinstance(token, ListTypeToken):
        return "list"
    elif isinstance(token, SetTypeToken):
        return "set"
    elif isinstance(token, MapTypeToken):
        return "map"
    elif isinstance(token, ContainerTypeToken):
        return [starts_with(MapTypeToken),
                starts_with(SetTypeToken),
                starts_with(ListTypeToken)]
    elif isinstance(token, BaseTypeToken):
        return BaseTypeToken
    elif isinstance(token, DefinitionTypeToken):
        return [starts_with(BaseTypeToken),
                starts_with(ContainerTypeToken)]
    elif isinstance(token, FieldTypeToken):
        return [starts_with(IdentifierToken),
                starts_with(BaseTypeToken),
                starts_with(ContainerTypeToken)]
    elif isinstance(token, ThrowsToken):
        return "throws"
    elif isinstance(token, FunctionTypeToken):
        return [starts_with(FieldTypeToken),
                "void"]
    elif isinstance(token, FunctionToken):
        return ["oneway", starts_with(FunctionTypeToken)]
    elif isinstance(token, XsdAttrsToken):
        return "xsd_attrs"
    elif isinstance(token, XsdFieldOptionsToken):
        return ["xsd_optional", "xsd_nillable", starts_with(XsdAttrsToken)]
    elif isinstance(token, FieldReqToken):
        return ["required", "optional"]
    elif isinstance(token, FieldIDToken):
        return starts_with(IntConstantToken)
    elif isinstance(token, FieldToken):
        return [starts_with(FieldIDToken),
                starts_with(FieldReqToken),
                starts_with(FieldTypeToken)]
    elif isinstance(token, ServiceToken):
        return "service"
    elif isinstance(token, ExceptionToken):
        return "exception"
    elif isinstance(token, UnionToken):
        return "union"
    elif isinstance(token, StructToken):
        return "struct"
    elif isinstance(token, SenumToken):
        return "senum"
    elif isinstance(token, EnumToken):
        return "enum"
    elif isinstance(token, TypedefToken):
        return "typedef"
    elif isinstance(token, ConstToken):
        return "const"
    elif isinstance(token, DefinitionToken):
        return [starts_with(ConstToken),
                starts_with(TypedefToken),
                starts_with(EnumToken),
                starts_with(SenumToken),
                starts_with(StructToken),
                starts_with(UnionToken),
                starts_with(ExceptionToken),
                starts_with(ServiceToken)]
    elif isinstance(token, NamespaceScopeToken):
        return ['*', 'c_glib', 'cpp', 'delphi', 'haxe', 'go', 'java', 'js', 'lua', 'netstd', 'perl',
                'php', 'py', 'py.twisted', 'rb', 'st', 'xsd']
    elif isinstance(token, NamespaceToken):
        return "namespace"
    elif isinstance(token, CppIncludeToken):
        return "namespace"
    elif isinstance(token, IncludeToken):
        return "namespace"
    elif isinstance(token, HeaderToken):
        return "namespace"
    elif isinstance(token, DocumentToken):
        return [starts_with(HeaderToken), starts_with(DefinitionToken)]

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

    if tok and isinstance(tok, type(token)):
        # if tok and tok != type(token):
        value = "err: skip"

    else:

        value = token.value

    token = get_next_token()
    return value


def get_ast():
    print("\033[92m+++ PARSER +++\033[0m")
    print()

    global tokens
    global token
    token = get_next_token()
    print("+++ token +++\n" + str(token) + "\n")

    ret = expression()

    # print("+++ output +++")
    # print("output:", ret)

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

    print("pre  while token", token)

    while rbp < token.lbp:
        t = token
        token = get_next_token()
        left = t.led(left)

        print("post while token", token)

    return left


def fn(items, level=0):
    for item in items:
        if isinstance(item, list):
            fn(item, level + 1)
        else:
            indentation = " " * level
            print('%s%s' % (indentation, item))


if __name__ == '__main__':
    source_code_path = "../../resources/thrift_source_code_samples/reduced.thrift"

    print("+++ source +++")
    [print(i[:-1]) for i in open(source_code_path).readlines()]
    print()

    global tokens
    tokens = get_tokens(source_code_path)
    print()

    print("+++ tokens +++")
    [print(i) for i in tokens]
    print()

    global token
    global token_pointer
    token_pointer = 0

    ast = ["DOCUMENT", get_ast()]

    print("+++ ast +++")
    print(ast)
    fn(ast)
