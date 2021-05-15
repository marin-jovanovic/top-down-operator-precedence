"""
code based on: https://eli.thegreenplace.net/2010/01/02/top-down-operator-precedence-parsing
"""

import argparse
import sys


# left binding power values
LBP = {
    "Power": 12,
    "Division": 10,
    "Multiplication": 10,
    "Subtraction": 8,
    "Addition": 8,
    "Ternary": 4,
    "Assignment": 2,
}

RBP = {
    "Subtraction": 13,
    "Power": 9,
    "LeftBracket": 7,
    "Assignment": 5,
    "If": 1,
}

# error bracket manager
L_R_BRACKETS = {
    "(": "err )",
    "{": "err }",
    "[": "err ]",
    "err (": "err )",
    "err {": "err }",
    "err [": "err ]",
}

R_L_BRACKETS = {
    ")": "err (",
    "}": "err {",
    "]": "err [",
    "err )": "err (",
    "err }": "err {",
    "err ]": "err [",
}

DEFAULT_ERR_L_B = "err ("
DEFAULT_ERR_R_B = "err )"


# lexer vars
LEXER = None
TOKEN = None


def lex_generator(program):
    """
    simple lexer
    splits input by space
    implemented as generator because it is only used for creating code{ast}
    """

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

        elif operator in ["!=", "==", "<=", ">="]:
            yield TokenAssignment(operator)

        elif operator in ["sin", "cos", "tan"]:
            yield TokenTrigonometry(operator)

        elif operator in ["true", "false"]:
            yield TokenBoolean(operator)

        # elif operator in ["||", "&&"]:
        #     yield TokenBooleanOperator(operator)

        elif operator == "?":
            yield TokenTernary(operator)

        elif operator == ":":
            yield TokenColon(operator)

        elif operator == "if":
            yield TokenIf(operator)

        elif operator == "then":
            yield TokenThen(operator)

        elif operator == "else":
            yield TokenElse(operator)

        else:
            yield TokenVariable(operator)

    yield TokenEOF()


class Token:
    """
    template class for all tokens
    handles logic for code{lbp}
    handles error messages when function or constant is not present
    """

    def __init__(self, value):
        self.identifier = self.__class__.__name__
        self.value = value

        # token has length of 5
        sufix = self.__class__.__name__[5:]

        if sufix in LBP:
            self.lbp = LBP.get(sufix)

        else:
            self.lbp = 0

        if sufix in RBP:
            self.rbp = RBP.get(sufix)

        else:
            self.rbp = 0

    def __str__(self):
        return "{:20} {:10} {:10}".format(self.identifier, self.value, self.lbp)

    def nud(self):
        """
        null denotation
        """

        print("todo nud for", self.__class__.__name__)

        sys.exit()

    def led(self, left):
        """
        left denotation
        """

        print("todo led for", self.__class__.__name__)

        sys.exit()


def expression(rbp=0):
    """
    driver
    check if current token is bindable
    while left binding power code{lbp} allows it try to match current code{left}
    with current token
    code{lbp} acts as controller which defines what code{left} can be bound
    with which tokens
    """

    global TOKEN
    t = TOKEN
    TOKEN = LEXER.__next__()
    left = t.nud()
    while rbp < TOKEN.lbp:
        t = TOKEN
        TOKEN = LEXER.__next__()
        left = t.led(left)
    return left


class TokenTernary(Token):
    """
    exp ? true_exp : false_exp
    """

    def led(self, left):
        global TOKEN

        truthy = expression()

        if not isinstance(TOKEN, TokenColon):
            print("error colon")
            sys.exit()

        colon = TOKEN.value
        TOKEN = LEXER.__next__()

        falsy = expression()

        return [self.value, left, truthy, colon, falsy]


class TokenIf(Token):
    """
    if exp then exp (else exp)
    """

    def nud(self):
        global TOKEN

        if_e = expression(self.rbp)

        if not isinstance(TOKEN, TokenThen):
            print("error then")

            sys.exit()

        then_t = TOKEN.value
        TOKEN = LEXER.__next__()

        then_e = expression()

        # else is optional
        if isinstance(TOKEN, TokenElse):
            else_t = TOKEN.value
            TOKEN = LEXER.__next__()

            else_e = expression()

            return [self.value, if_e, then_t, then_e, else_t, else_e]

        return [self.value, if_e, then_t, then_e]


class TokenBoolean(Token):
    """
    true false
    """

    def nud(self):
        return self.value


class TokenLiteral(Token):
    """
    numeric
    """

    def nud(self):
        return self.value


class TokenAssignment(Token):
    """
    ==
    """

    def led(self, left):
        return [self.value, left, expression(self.rbp)]


class TokenAddition(Token):
    """
    +
    """

    def led(self, left):
        return ["+", left, expression(self.lbp)]


class TokenSubtraction(Token):
    """
    -
    """

    def nud(self):
        return ["-", expression(self.rbp)]

    def led(self, left):
        return ["-", left, expression(self.lbp)]


class TokenMultiplication(Token):
    """
    *
    """

    def led(self, left):
        return ["*", left, expression(self.lbp)]


class TokenDivision(Token):
    """
    /
    """

    def led(self, left):
        return ["/", left, expression(self.lbp)]


class TokenPower(Token):
    """
    **
    """

    def led(self, left):
        return ["**", left, expression(self.rbp)]


class TokenLeftBracket(Token):
    """
    (
    """

    def nud(self):
        global TOKEN

        expr = expression(self.rbp)

        if not isinstance(TOKEN, TokenRightBracket):
            # print("error right bracket")

            r_b = L_R_BRACKETS.get(self.value)

        else:
            r_b = TOKEN.value
            TOKEN = LEXER.__next__()

        return [self.value, expr, r_b]


class TokenTrigonometry(Token):
    """
    sin cos tan
    """

    def nud(self):
        global TOKEN

        l_b_err = False

        if not isinstance(TOKEN, TokenLeftBracket):
            # print("error left bracket")

            l_b = DEFAULT_ERR_L_B
            l_b_err = True

        else:

            l_b = TOKEN.value
            TOKEN = LEXER.__next__()

        expr = expression()

        if not isinstance(TOKEN, TokenRightBracket):
            r_b = L_R_BRACKETS.get(l_b)

        else:
            r_b = TOKEN.value
            TOKEN = LEXER.__next__()

        if l_b_err:
            l_b = R_L_BRACKETS.get(r_b)

        return [self.value, l_b, expr, r_b]


class TokenVariable(Token):
    """
    var
    """

    def nud(self):
        return self.value


class TokenRightBracket(Token):
    """
    )
    """


class TokenThen(Token):
    """
    then
    """


class TokenElse(Token):
    """
    else
    """


class TokenColon(Token):
    """
    :
    """


class TokenEOF(Token):
    """
    end of file
    """

    def __init__(self):
        Token.__init__(self, value="EOF")


def formatted_print(data, s_c=0):
    """
    print with indentation
    """

    if isinstance(data, (str, int)):
        print(s_c * 4 * " " + str(data))

    else:
        for i in data:
            formatted_print(i, s_c + 1)


def get_args():
    """
    argument parser
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("expression", type=str)
    args = parser.parse_args()
    return args


def main():
    """
    demo
    """

    global LEXER, TOKEN

    args = get_args()

    LEXER = lex_generator(args.expression)

    TOKEN = LEXER.__next__()

    ast = expression()
    print(ast)


if __name__ == "__main__":
    main()
