"""
code based on: https://eli.thegreenplace.net/2010/01/02/top-down-operator-precedence-parsing
 
"""

"""
left binding power values
"""
LBP = {
    "Power": 12,

    "Division": 10,
    "Multiplication": 10,

    "Subtraction": 8,
    "Addition": 8,

    "Ternary": 4,
    "Assignment": 2,

    # not used
    "Then": -404,
    "If": -404,
    "LeftBracket": -404,
    "RightBracket": -404,
    "Trigonometry": -404,
    "Else": -404,
    "Colon": -404,
    "Literal": -404,
    "Boolean": -404,
    "Variable": -404,
    "EOF": -404,
}

"""
If.rpb > Then.lbp
Assigment.rbp > Then.lbp

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
    "Addition": 13,
    "Subtraction": 13,

    "Power": 9,

    "LeftBracket": 7,

    "Assignment": 5,

    "If": 1,

    # not used
    "Then": -404,
    "Else": -404,
    "Colon": -404,
    "Literal": -404,
    "Multiplication": -404,
    "Division": -404,
    "RightBracket": -404,
    "Trigonometry": -404,
    "EOF": -404,
    "Variable": -404,
    "Boolean": -404,
    "Ternary": -404,

}


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


class Token(object):
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
    """
    driver

    check if current token is bindable

    while left binding power code{lbp} allows it try to match current code{left}
    with current token

    code{lbp} acts as controller which defines what code{left} can be bound
    with which tokens

    """

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
        global token

        truthy = expression()

        if not isinstance(token, TokenColon):
            print("error colon")
            import sys
            sys.exit()

        colon = token.value
        token = lexer.__next__()

        falsy = expression()

        return [self.value, left, truthy, colon, falsy]


class TokenIf(Token):

    def nud(self):
        global token

        """if expression"""
        if_e = expression(self.rbp)

        """then token"""
        if not isinstance(token, TokenThen):
            print("error then")
            import sys
            sys.exit()

        then_t = token.value
        token = lexer.__next__()

        """then expression"""
        then_e = expression()

        """else is optional"""
        if isinstance(token, TokenElse):
            """else token"""
            else_t = token.value
            token = lexer.__next__()

            """else expression"""
            else_e = expression()

            return [self.value, if_e, then_t, then_e, else_t, else_e]

        else:
            return [self.value, if_e, then_t, then_e]


class TokenBoolean(Token):

    def nud(self):
        return self.value


class TokenLiteral(Token):

    def nud(self):
        return self.value


class TokenAssignment(Token):

    def led(self, left):
        return [self.value, left, expression(self.rbp)]


class TokenAddition(Token):

    def led(self, left):
        return ["+", left, expression(self.lbp)]


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
        return ["**", left, expression(self.rbp)]


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


class TokenTrigonometry(Token):

    def nud(self):
        global token

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


class TokenRightBracket(Token):
    pass


class TokenThen(Token):
    pass


class TokenElse(Token):
    pass


class TokenColon(Token):
    pass


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

    """binary"""

    test("true != false", ['!=', 'true', 'false'])

    """ternary"""

    test("2 == 2 ? x : y", ['?', ['==', '2', '2'], 'x', ':', 'y'])

    test("2 == 1 + 1 ? x + 1 : y + 7",
         ['?', ['==', '2', ['+', '1', '1']], ['+', 'x', '1'], ':',
          ['+', 'y', '7']])

    test("4 != 2 + x ? a : b",
         ['?', ['!=', '4', ['+', '2', 'x']], 'a', ':', 'b'])

    test("a ? b : c ? d : e", ['?', 'a', 'b', ':', ['?', 'c', 'd', ':', 'e']])

    """if then else"""
    test("if a then b", ['if', 'a', 'then', 'b'])
    test("if a then b else c", ['if', 'a', 'then', 'b', 'else', 'c'])
    test("if a then if b then c", ['if', 'a', 'then', ['if', 'b', 'then', 'c']])
    test("if a then if b then c else d",
         ['if', 'a', 'then', ['if', 'b', 'then', 'c', 'else', 'd']])
    test("if a then if b then c else d else f",
         ['if', 'a', 'then', ['if', 'b', 'then', 'c', 'else', 'd'], 'else',
          'f'])
    test("if a then if b then c else d else if e then f else g",
         ['if', 'a', 'then', ['if', 'b', 'then', 'c', 'else', 'd'], 'else',
          ['if', 'e', 'then', 'f', 'else', 'g']])

    test("if x + 1 == a + b then a else c",
         ['if', ['==', ['+', 'x', '1'], ['+', 'a', 'b']],
          'then', 'a', 'else', 'c'])

    test("if x + 1 == a + b then a + m + sin ( x ) else c + d",
         ['if', ['==', ['+', 'x', '1'], ['+', 'a', 'b']], 'then', ['+',
                                                                   ['+', 'a',
                                                                    'm'],
                                                                   ['sin', '(',
                                                                    'x', ')']],
          'else', ['+', 'c', 'd']])
    test("if x + 1 == a + b then if a == m then sin ( x ) else c else if x "
         "then a else b", ['if', ['==', ['+', 'x', '1'], ['+', 'a', 'b']],
                           'then', ['if', ['==', 'a', 'm'], 'then',
                                    ['sin', '(', 'x', ')'],
                                    'else', 'c'], 'else',
                           ['if', 'x', 'then', 'a', 'else', 'b']])

    test("if x + 1 == a + b then a",
         ['if', ['==', ['+', 'x', '1'], ['+', 'a', 'b']], 'then', 'a'])
    test("if x + 1 == a + b + sin ( x ) then a + b + ( a + d )", ['if', ['==',
                                                                         ['+',
                                                                          'x',
                                                                          '1'],
                                                                         ['+',
                                                                          ['+',
                                                                           'a',
                                                                           'b'],
                                                                          [
                                                                              'sin',
                                                                              '(',
                                                                              'x',
                                                                              ')']]],
                                                                  'then', ['+',
                                                                           ['+',
                                                                            'a',
                                                                            'b'],
                                                                           ['(',
                                                                            [
                                                                                '+',
                                                                                'a',
                                                                                'd'],
                                                                            ')']]])

    test("3 * ( 2 + - 4 ) ^ 4 ^ 5 ^ 6", ['*', '3', ['**', ['(', ['+', '2',
                                                                 ['-', '4']],
                                                           ')'], ['**', '4',
                                                                  ['**', '5',
                                                                   '6']]]])
    print(TEST_PASSED_COUNT, "/", TEST_COUNT)


def main():
    run_tests()


if __name__ == '__main__':
    main()
