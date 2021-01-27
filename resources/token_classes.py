from resources.resource_constants import KEYWORDS_PREFIX


class Token:

    def __init__(self, identifier, row, value):
        self.identifier = identifier
        self.row = row
        self.value = value

    def __str__(self):
        return self.identifier + " " + str(self.row) + " " + self.value


class KeywordToken(Token):

    def __init__(self, identifier, row, value):
        self.identifier = KEYWORDS_PREFIX + identifier
        self.row = row
        self.value = value


class NamespaceScope(Token):

    def __str__(self):
        return "Identifier " + self.row + " " + self.value


# fixme lbp, expression
class EqualToken(Token):
    lbp = "todo"

    def led(self, left):

        return [left, "=", expression(self.lbp)]


class LeftCurlyBracketToken(Token):

    pass


class RightCurlyBracketToken(Token):
    pass


class LeftRoundBracketToken(Token):
    pass


class RightRoundBracketToken(Token):
    pass


class LeftSquareBracketToken(Token):
    pass


class RightSquareBracketToken(Token):
    pass


class LeftAngleBracketToken(Token):
    pass


class RightAngleBracketToken(Token):
    pass


class ColonToken(Token):
    pass


class FieldReqToken(Token):
    pass


class BaseTypeToken(Token):
    pass


class CommaToken(Token):
    pass


class PlusToken(Token):
    pass


class MinusToken(Token):
    pass


class DotToken(Token):
    pass


class UpperEToken(Token):
    pass


class LowerEToken(Token):
    pass


class LiteralToken(Token):
    pass


class IdentifierToken(Token):
    pass


class STIdentifierToken(Token):
    pass


class ListSeparatorToken(Token):
    pass


class LetterToken(Token):
    pass


class DigitToken(Token):
    pass


if __name__ == '__main__':
    t = KeywordToken("id", 2, "val")
    print(t)


