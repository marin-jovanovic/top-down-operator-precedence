import sys

LBP = {
    "Literal": -404,
    "Addition": 10,
    "Subtraction": 10,
    "Multiplication": 20,
    "Division": 20,
    "Power": 30,
    "LeftBracket": 0,
    "RightBracket": 0,
    "EOF": -404,

    # "Addition": 3,
    # "Subtraction": 3,
    # "Literal": 0,
    # "EOF": 0,
    # "MAX": 100,
    # "Multiply": 4,
    # "Divide": 4,
    # "Subtraction": 3
    # "variable_type": 1,
    # "variable": 1,
    # "lparen": 0,
    # "rparen": 0,  # not important
    # "end_of_line": -1,
    # "association": 2,
    # "add": 3,
    # "sub": 3,
    # "mul": 4,
    # "div": 4,
    # "pow": 5,
    # "equal": 2,
    # "function name": 1,
    # "left curly bracket": 0,
    # "right curly bracket": 0
}

RBP = {
    "Literal": -404,
    "Addition": 100,
    "Subtraction": 100,
    "Multiplication": -404,
    "Division": -404,
    "Power": -404,
    "LeftBracket": -404,
    "RightBracket": -404,
    "EOF": -404,

    # "Addition": 3,
    # "Literal": None,
    # "Multiply": 4,
    # "EOF": None,
    # "Divide": 4,
    # "Subtraction": 3
}


# todo assignment, boolean, power, variables


def lex_generator(program):
    for operator in program.split(" "):

        if operator.isnumeric():
            yield TokenLiteral(operator)

        elif operator == "+":
            yield TokenAddition(operator)

        elif operator == "-":
            yield TokenSubtraction(operator)

        elif operator == "*":
            yield TokenMultiplication(operator)

        elif operator == "/":
            yield TokenDivision(operator)

        elif operator == "^":
            yield TokenPower(operator)

        elif operator in ["(", "{", "["]:
            yield TokenLeftBracket(operator)

        elif operator in [")", "}", "]"]:
            yield TokenRightBracket(operator)

        else:
            print("lexer error")
            sys.exit()

    yield TokenEOF()


class Token(object):

    def __init__(self, value):
        self.identifier = self.__class__.__name__
        self.value = value

        # token has length of 5
        sufix = self.__class__.__name__[5:]

        if sufix in LBP:
            self.lbp = LBP.get(sufix)

        else:
            print(f"no {sufix=} in LBP")
            import sys
            sys.exit()

        if sufix in RBP:
            self.rbp = RBP.get(sufix)

        else:
            print(f"no {sufix=} in RBP")
            import sys
            sys.exit()

    def __str__(self):
        return "{:20} {:10} {:10}".format(self.identifier, self.value, self.lbp)

    def nud(self):
        print("todo nud for", self.__class__.__name__)
        import sys
        sys.exit()

    def led(self, left):
        print("todo led for", self.__class__.__name__)
        import sys
        sys.exit()


def expression(rbp=0):
    global token
    t = token
    token = lexer.__next__()
    left = t.nud()
    while rbp < token.lbp:
        t = token
        token = lexer.__next__()
        left = t.led(left)
    return left


class TokenLiteral(Token):

    def nud(self):
        return self.value


class TokenAddition(Token):

    def nud(self):
        return expression(self.rbp)

    def led(self, left):
        right = expression(self.lbp)

        return ["+", left, right]


class TokenSubtraction(Token):

    def nud(self):
        return ["-", expression(self.rbp)]

    def led(self, left):
        return ["-", left, expression(self.lbp)]


class TokenMultiplication(Token):

    def led(self, left):
        return ["*", left, expression(self.lbp)]


class TokenDivision(Token):

    def led(self, left):
        return ["/", left, expression(self.lbp)]


class TokenPower(Token):

    def led(self, left):
        return ["**", left, expression(self.lbp - 1)]


class TokenLeftBracket(Token):

    def nud(self):
        global token

        expr = expression()

        if TokenRightBracket and TokenRightBracket != type(token):
            print("error right bracket")
            import sys
            sys.exit()

        token = lexer.__next__()

        return ["(", expr, ")"]


class TokenRightBracket(Token):
    pass


class TokenEOF(Token):

    def __init__(self):
        Token.__init__(self, value="EOF")

    pass


def main():
    global token, lexer

    exp = "3 * ( 2 + - 4 ) ^ 4"
    exp = "2 + ( ( 3 ) + ( ( 2 - 4 ) + 3 ) ) + 1"

    lexer = lex_generator(exp)

    token = lexer.__next__()

    ast = expression()

    print(ast)


if __name__ == '__main__':
    main()
