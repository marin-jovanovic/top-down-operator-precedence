k = 0
LBP = {
    "Power": 35 + k,

    "Division": 25 + k,
    "Multiplication": 25 + k,

    "Subtraction": 15 + k,
    "Addition": 15 + k,

    "LeftBracket": 0 + k,
    "RightBracket": 0 + k,
    "Trigonometry": 0 + k,

    "Assignment": 2,

    "Ternary": 3,

    "Colon": -404,

    "Literal": -404,
    "Boolean": -404,
    "Variable": -404,
    "EOF": -404,

    "If": 1,
    "Then": -404,
    "Else": -404,

}

"""
If.rpb > Then.lbp
Assigment.rbp > Ternary.lbp

class TokenAssignment(Token):

    def led(self, left):
        return [self.value, left, expression(self.rbp)]

class TokenTernary(Token):

    def led(self, left):
        # exp
        # ?
        # exp
        # :
        # exp

        global token

        truthy = expression()

        if not isinstance(token, TokenColon):
            print("error colon")
            import sys
            sys.exit()

        colon = token.value
        token = lexer.__next__()

        falsy = expression()

        return [left, self.value, truthy, colon, falsy]

left is [self.value, left, expression(self.rbp)] from TokenAssignment.led

"""

RBP = {
    "Addition": 100,
    "Subtraction": 100,

    "LeftBracket": 5,
    "Assignment": 4,

    "Colon": -404,
    "Literal": -404,
    "Multiplication": -404,
    "Division": -404,
    "Power": -404,
    "RightBracket": -404,
    "Trigonometry": -404,
    "EOF": -404,
    "Variable": -404,
    "Boolean": -404,
    "Ternary": -404,

    "If": 2,
    "Then": -404,
    "Else": -404,

}


# todo if then else, ternary operator
# if
# exp
# then
# exp
# else
# exp



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

        elif operator in ["!=", "==", "<=", ">="]:
            yield TokenAssignment(operator)

        elif operator in ["sin", "cos", "tan"]:
            yield TokenTrigonometry(operator)

        elif operator in ["true", "false"]:
            yield TokenBoolean(operator)

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

        # else:
        #     print("lexer error")
        #     sys.exit()

        # test("if x + 1 == a + b then a else c", "")

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


class TokenTernary(Token):

    def led(self, left):
        # exp
        # ?
        # exp
        # :
        # exp

        global token

        truthy = expression()

        if not isinstance(token, TokenColon):
            print("error colon")
            import sys
            sys.exit()

        colon = token.value
        token = lexer.__next__()

        falsy = expression()

        return [self.value, left, [colon, truthy, falsy]]
        # return [left, self.value, truthy, colon, falsy]


class TokenIf(Token):

    def nud(self):
        return [self.value, expression(self.rbp)]


class TokenThen(Token):
    pass

class TokenElse(Token):
    pass

class TokenColon(Token):
    pass


class TokenBoolean(Token):

    def nud(self):
        return self.value

class TokenAssignment(Token):

    def led(self, left):
        return [self.value, left, expression(self.rbp)]


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

        expr = expression(self.rbp)

        if not isinstance(token, TokenRightBracket):
            print("error right bracket")
            import sys
            sys.exit()

        r_b = token.value
        token = lexer.__next__()

        return [self.value, expr, r_b]


class TokenRightBracket(Token):
    pass


class TokenTrigonometry(Token):

    def nud(self):
        global token

        # return [self.value, expression()]

        if not isinstance(token, TokenLeftBracket):
            print("error left bracket")
            import sys
            sys.exit()

        l_b = token.value
        token = lexer.__next__()

        expr = expression()

        if not isinstance(token, TokenRightBracket):
            print("error right bracket")
            import sys
            sys.exit()

        r_b = token.value
        token = lexer.__next__()

        return [self.value, l_b, expr, r_b]


class TokenVariable(Token):

    def nud(self):
        return self.value


class TokenEOF(Token):

    def __init__(self):
        Token.__init__(self, value="EOF")


def formatted_print(data, s_c=0):
    if isinstance(data, (str, int)):
        print(s_c * 4 * " " + str(data))

    else:
        for i in data:
            formatted_print(i, s_c + 1)


TEST_PASSED_COUNT = 0
TEST_COUNT = 0


def test(test_input, expected_output):
    global lexer, token
    global TEST_COUNT, TEST_PASSED_COUNT

    print(test_input)

    TEST_COUNT += 1

    lexer = lex_generator(test_input)

    token = lexer.__next__()

    ast = expression()

    if ast == expected_output:
        TEST_PASSED_COUNT += 1
        print("test passed")
    else:
        print(f"{test_input=}")

        print("expect:", expected_output)
        print("got    ", ast)
        formatted_print(ast)

        print(f"test(\"{test_input}\", {ast})")
        print("test failed")


def run_tests():
    test("1 + 2", ['+', '1', '2'])
    test("2 + 3 + 4", ['+', ['+', '2', '3'], '4'])

    test("2 + 3 * 5", ['+', '2', ['*', '3', '5']])
    test("2 + 3 * 4 * 5", ['+', '2', ['*', ['*', '3', '4'], '5']])
    test("2 * 3 + 4 * 5", ['+', ['*', '2', '3'], ['*', '4', '5']])

    test("1 / 2", ['/', '1', '2'])
    test("1 / 2 / 3 * 4", ['*', ['/', ['/', '1', '2'], '3'], '4'])
    test("1 + 2 / 2 * 4 + 5 / 3 + 6 * 4",
         ['+', ['+', ['+', '1', ['*', ['/', '2', '2'], '4']], ['/', '5', '3']],
          ['*', '6', '4']])

    test("1 - 2", ['-', '1', '2'])
    test("1 - 2 - 3", ['-', ['-', '1', '2'], '3'])

    test("3 * ( 2 + - 4 ) ^ 4",
         ['*', '3', ['**', ['(', ['+', '2', ['-', '4']], ')'], '4']])
    test("2 + ( ( 3 ) + ( ( 2 - 4 ) + 3 ) ) + 1", ['+', ['+', '2', ['(', ['+',
                                                                          ['(',
                                                                           '3',
                                                                           ')'],
                                                                          ['(',
                                                                           ['+',
                                                                            [
                                                                                '(',
                                                                                [
                                                                                    '-',
                                                                                    '2',
                                                                                    '4'],
                                                                                ')'],
                                                                            '3'],
                                                                           ')']],
                                                                    ')']], '1'])

    test("sin ( 1 ) + 2", ['+', ['sin', '(', '1', ')'], '2'])
    test("1 - cos ( 3 + 1 )", ['-', '1', ['cos', '(', ['+', '3', '1'], ')']])

    test("1 - cos ( alpha + beta + 2 )",
         ['-', '1', ['cos', '(', ['+', ['+', 'alpha', 'beta'], '2'], ')']])

    test("1 - x != 5 + p", ['!=', ['-', '1', 'x'], ['+', '5', 'p']])

    test("( 2 )", ['(', '2', ')'])

    test("[ j * ( 7 + l ) + f ]",
         ['[', ['+', ['*', 'j', ['(', ['+', '7', 'l'], ')']], 'f'], ']'])

    test("1 - x + 2 * cos ( 2 ) != 5 + { m - [ j * ( 7 + l ) + f ] / h } + p",
         ['!=', ['+', ['-', '1', 'x'], ['*', '2', ['cos', '(', '2', ')']]],
          ['+', ['+', '5', ['{', ['-', 'm', ['/', ['[', ['+', ['*', 'j', ['(',
                                                                          ['+',
                                                                           '7',
                                                                           'l'],
                                                                          ')']],
                                                         'f'], ']'], 'h']],
                            '}']], 'p']])

    test("true != false", ['!=', 'true', 'false'])

    test("2 == 2 ? x : y", ['?', ['==', '2', '2'], [':', 'x', 'y']])

    test("2 == 1 + 1 ? x + 1 : y + 7", ['?', ['==', '2', ['+', '1', '1']],
                                        [':', ['+', 'x', '1'],
                                         ['+', 'y', '7']]])

    test("4 != 2 + x ? a : b",
         ['?', ['!=', '4', ['+', '2', 'x']], [':', 'a', 'b']])


def main():

    run_tests()

    test("if x + 1 == a + b then a else c", "")
    #     # if a then b else c

    print(TEST_PASSED_COUNT, "/", TEST_COUNT)


if __name__ == '__main__':
    main()
