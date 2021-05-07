LBP = {
    "Addition": 3,
    "Subtraction": 3,
    "Literal": 0,
    "EOF": 0,
    "MAX": 100,
    "Multiply": 4,
    "Divide": 4,
    "Subtraction": 3
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
    "Addition": 3,
    "Literal": None,
    "Multiply": 4,
    "EOF": None,
    "Divide": 4,
    "Subtraction": 3
}

# todo assignment, boolean, power

def tokenize(program):
    for token in program.split(" "):

        if token == "+":
            yield TokenAddition()

        elif token == "-":
            yield TokenSubtraction()

        elif token == "*":
            yield TokenMultiply()

        elif token == "/":
            yield TokenDivide()
        #
        # elif operator in ["sin", "cos"]:
        #     yield Token_trigonometry(operator)
        #
        # elif operator in ["{", "(", "["]:
        #     yield Token_left_bracket(operator)
        #
        # elif operator in ["}", ")", "]"]:
        #     yield Token_right_bracket(operator)

        elif token.isnumeric():
            yield TokenLiteral(token)

        else:
            raise SyntaxError('unknown token: %s', token)

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


class TokenAddition(Token):

    def __init__(self):
        Token.__init__(self, value="+")

    def led(self, left):
        global token, lexer

        return [self.value, left, expression(self.rbp)]


class TokenSubtraction(Token):

    def __init__(self):
        Token.__init__(self, value="-")

    def led(self, left):
        return [self.value, left, expression(self.rbp)]

    def nud(self):
        return [self.value, expression(LBP.get("MAX"))]


class TokenMultiply(Token):

    def __init__(self):
        Token.__init__(self, value="*")

    def led(self, left):
        return [self.value, left, expression(self.rbp)]


class TokenDivide(Token):

    def __init__(self):
        Token.__init__(self, value="/")

    def led(self, left):
        return [self.value, left, expression(self.rbp)]


class TokenLiteral(Token):

    def nud(self):
        return self.value


class TokenEOF(Token):

    def __init__(self):
        Token.__init__(self, value="EOF")


def match(tok=None):
    global token
    if tok and tok != type(token):
        raise SyntaxError('Expected %s' % tok)
    token = next.__next__()


def parse(program):
    # print(80 * "=")

    global lexer

    lexer = tokenize(program)

    # token = lexer.__next__()

    print("source:", program)

    ret = expression()

    # print("output:", ret)

    return ret


def expression(rbp=0):
    # global token
    # t = token
    # token = next.__next__()
    # left = t.nud()
    # while rbp < token.lbp:
    #     t = token
    #     token = next.__next__()
    #     left = t.led(left)
    # return left

    global token, lexer

    token = lexer.__next__()
    left = token.nud()

    token = lexer.__next__()
    # try:
    #     token = lexer.__next__()
    # except StopIteration:
    #     return left
    # print("left up", left)

    while rbp < token.lbp:
        left = token.led(left)
    return left


"""support functions"""


def test(test_input, correct_output):
    if str(parse(test_input)) == correct_output:
        print("test passed")
    else:
        print("expect:", correct_output)
        print("got    ", parse(test_input))
        print("test failed")
        import sys
        sys.exit()


def formated_print(data, s_c=0):
    if isinstance(data, (str, int)):
        print(s_c * 4 * " " + str(data))

    else:
        for i in data:
            formated_print(i, s_c + 1)


""""""


def main():

    test("1 + 2", "['+', '1', '2']")
    test("2 + 3 + 4", "['+', ['+', '2', '3'], '4']")
    test("2 + 3 * 5", "['+', '2', ['*', '3', '5']]")
    test("2 + 3 * 4 * 5", "['+', '2', ['*', ['*', '3', '4'], '5']]")
    test("2 * 3 + 4 * 5", "['+', ['*', '2', '3'], ['*', '4', '5']]")
    test("1 / 2", "['/', '1', '2']")
    test("1 / 2 / 3 * 4", "['*', ['/', ['/', '1', '2'], '3'], '4']")
    test("1 + 2 / 2 * 4 + 5 / 3 + 6 * 4",
         "['+', ['+', ['+', '1', ['*', ['/', '2', '2'], '4']], ['/', '5', '3']], ['*', '6', '4']]")

    test("1 - 2", "['-', '1', '2']")
    test("1 - 2 - 3", "['-', ['-', '1', '2'], '3']")

    k = "- 1 - 2"
    t = parse(k)
    print(t)
    print()
    print("test(\"" + k + "\", \"" + str(t) + "\")")
    # [print(i) for i in t]

    # formated_print(t)

    # t = parse("2 + 3 + 4 - 2 * ( - 2 + 3 )")
    # print(t)
    #
    # formated_print(t)
    #
    #
    #
    # print(80 * "=")
    # print("all tests passed")
    # print(80 * "=")


if __name__ == '__main__':
    main()
