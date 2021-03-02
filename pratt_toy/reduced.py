SPACE_COUNT = 0
MAX_OFFSET = 0

LBP = {
    "variable_type": 1,
    "variable": 1,
    "literal": None,
    "lparen": 0,
    "rparen": 0,  # not important
    "EOF": 0,
    "end_of_line": -1,
    "association": 2,
    "add": 3,
    "sub": 3,
    "mul": 4,
    "div": 4,
    "pow": 5,
    "equal": 2,
    "function name": 1,
    "left curly bracket": 0,
    "right curly bracket": 0

}


def tokenize(program):
    for operator in program.split(" "):
        if operator == "imeFunkcije":
            yield FunctionToken("imeFunkcije")
        elif operator.isnumeric():
            yield literal_token(operator)
        elif operator == "+":
            yield operator_add_token()
        elif operator == "-":
            yield operator_sub_token()
        elif operator == "*":
            yield operator_mul_token()
        elif operator == "/":
            yield operator_div_token()
        elif operator == "^":
            yield operator_pow_token()
        elif operator == '(':
            yield LeftRoundBracketToken()
        elif operator == ')':
            yield RightRoundBracketToken()
        elif operator == "{":
            yield LeftCurlyBracketToken()
        elif operator == "}":
            yield RightCurlyBracketToken()
        elif operator == "=":
            yield operator_association_token()
        elif operator == ";":
            yield operator_end_of_line_token()
        elif operator == "int":
            yield operator_int_type_token()
        elif operator == "class":
            yield ClassDefinitionToken()
        elif operator == "className":
            yield ClassNameToken()
        elif operator == "public":
            yield VisibilityToken()
        elif operator == "void":
            yield ReturnTypeToken()
        elif operator == "methodName":
            yield MethodNameToken()
        elif operator in ["==", "<", ">", ">=", "<=", "!="]:
            yield EqualOperatorToken(operator)
        elif operator[0].isalpha():
            yield variable_token(operator)
        else:
            raise SyntaxError('unknown operator: %s', operator)

    yield end_token()


class ClassDefinitionToken:
    def nud(self):
        match(ClassNameToken)

        match(LeftCurlyBracketToken)

        methods = expression(-1)

        match(RightCurlyBracketToken)

        return ["class", "className", methods]

    def led(self, left):
        return


class ClassNameToken:
    def nud(self):
        return

    def led(self, left):
        return


class VisibilityToken:
    def nud(self):
        return

    def led(self, left):
        return


class ReturnTypeToken:
    def nud(self):
        return

    def led(self, left):
        return


class MethodNameToken:
    def nud(self):
        return

    def led(self, left):
        return


def match(tok=None):
    global token
    if tok and tok != type(token):
        raise SyntaxError('Expected %s' % tok)
    token = next.__next__()


def parse(program):
    print(80 * "=")

    global token, next

    next = tokenize(program)

    token = next.__next__()

    print("source:", program)

    ret = expression()
    print("output:", ret)

    return ret


def expression(rbp=0):
    global token
    t = token
    token = next.__next__()
    left = t.nud()
    while rbp < token.lbp:
        t = token
        token = next.__next__()
        left = t.led(left)
    return left


class LeftRoundBracketToken(object):
    lbp = LBP.get("lparen")

    def nud(self):
        # handle till ")"
        expr = expression(self.lbp)

        # handles ")"
        match(RightRoundBracketToken)

        return expr


class RightRoundBracketToken(object):
    lbp = LBP.get("rparen")


class LeftCurlyBracketToken:
    lbp = LBP.get("left curly bracket")


class RightCurlyBracketToken:
    lbp = LBP.get("right curly bracket")


class FunctionToken(object):
    lbp = LBP.get("function name")

    def __init__(self, value):
        self.value = value

    def nud(self):
        # expects "("
        match(LeftRoundBracketToken)

        args = []

        if RightRoundBracketToken != type(token):
            # expects args
            args = expression(0)

        # expects ")"
        match(RightRoundBracketToken)

        # expects "{"
        match(LeftCurlyBracketToken)

        # expects instructions
        body = expression(0)
        print(body)

        """
            body.lbp < RightCurlyBracketToken.lbp 
        """

        # expects "}"
        match(RightCurlyBracketToken)

        return ['function', '(', ["args", args], ')', '{', ['body', body], '}']

    def led(self, left):
        # right = expression(self.lbp)

        print(left)

        # return ["bool tester", ["LS", left], self.value, ["RS", right], ";"]

        return ['function', '(', ')', '{', ['tijelo', left], '}']


class EqualOperatorToken(object):
    lbp = LBP.get("equal")

    def __init__(self, value):
        self.value = value

    def led(self, left):
        right = expression(self.lbp)

        if isinstance(left, str):
            left = [left]
            print("left reconfig")

        if isinstance(right, (int, str)):
            right = [right]
            print("right reconfig")

        return ["bool tester", ["LS", left], self.value, ["RS", right], ";"]


class operator_int_type_token(object):
    lbp = LBP.get("variable_type")

    # def led(self, left):
    #     return expression(self.lbp)


class operator_end_of_line_token(object):
    lbp = LBP.get("end_of_line")

    def led(self, left):
        return ["EOL", left]
        # return ["instruction block", left, expression()]


class operator_association_token(object):
    lbp = LBP.get("association")

    def nud(self):
        return expression(100)

    def led(self, left):
        # print("left", left)
        print("t", left, token)

        if isinstance(left, str):
            left = [left]
            print("left reconfig")

        right = expression(self.lbp)
        print("resources", right)
        # print("right", right)

        # expects ";"
        match(operator_end_of_line_token)

        if isinstance(right, int):
            right = [right]
            print("right reconfig")

        instruction = ["instruction", ["LS", left], "=", ["RS", right], ";"]
        print("handle", instruction)

        return "xxx"
        # return instruction


class variable_token(object):
    lbp = LBP.get("variable")

    def __init__(self, value):
        self.value = str(value)

    def nud(self):
        ret = self.value
        return ret

    def led(self, left):
        # return str(left) + ", " + str(self.value)
        return [left, self.value]


# number
class literal_token(object):

    def __init__(self, value):
        self.value = int(value)

    def nud(self):
        return self.value


class operator_add_token(object):
    lbp = LBP.get("add")

    def nud(self):
        return expression(100)

    def led(self, left):
        right = expression(self.lbp)
        return ["+", left, right]


class operator_sub_token(object):
    lbp = LBP.get("sub")

    def nud(self):
        return - expression(100)

    def led(self, left):
        return ["-", left, expression(self.lbp)]


class operator_mul_token(object):
    lbp = LBP.get("mul")

    def led(self, left):
        return ["*", left, expression(self.lbp)]


class operator_div_token(object):
    lbp = LBP.get("div")

    def led(self, left):
        return ["/", left, expression(self.lbp)]


class operator_pow_token(object):
    lbp = LBP.get("pow")

    def led(self, left):
        return ["^", left, expression(self.lbp - 1)]


class end_token(object):
    lbp = LBP.get("EOF")


def test(test_input, correct_output):
    if parse(test_input) == correct_output:
        print("test passed")
    else:
        print("expect:", correct_output)
        print("test failed")
        import sys
        sys.exit()


def formated_print(data, s_c=0):
    if isinstance(data, (str, int)):
        print(s_c * 4 * " " + str(data))

    else:
        for i in data:
            formated_print(i, s_c + 1)


if __name__ == '__main__':
    # test("1 + 1", ["+", 1, 1])
    # test("3 * ( 2 + - 4 ) ^ 4", ['*', 3, ['^', ['+', 2, -4], 4]])
    # test("1 - 1 + 1", ['+', ['-', 1, 1], 1])
    # test("var + 3", ['+', 'var', 3])
    # test("var + 3 + 3", ['+', ['+', 'var', 3], 3])
    # test('3 * ( 2 + - 4 ) ^ var', ['*', 3, ['^', ['+', 2, -4], 'var']])
    # test("x = 100 ;", ["instruction", ["LS", ["x"]], "=", ["RS", [100]], ";"])
    # test("cijena = 1000 ;", ["instruction", ["LS", ["cijena"]], "=", ["RS", [1000]], ";"])
    # test("cijena = 100 + 2 * 3 ;", ["instruction", ["LS", ["cijena"]], "=", ["RS", ["+", 100, ["*", 2, 3]]], ";"])
    # test("int cijena = 1000 ;", ["instruction", ["LS", ["int", "cijena"]], "=", ["RS", [1000]], ";"])
    # test("cijena <= 20 + 20", ['bool tester', ['LS', ['cijena']], '<=', ['RS', ['+', 20, 20]], ';'])

    # formated_print(parse("1 + 2 * 3 / 7 + 1"))

    # t = parse("x = 2 ; y = 3 ;")
    # t = parse("- 1")
    t = parse("2 + 3 + 4 - 2 * ( - 2 + 3 )")
    print(t)
    #
    # formated_print(t)

    # t = parse("class className { public void methodName ( ) { int x = 1 ; int y = 2 ; }")

    formated_print(t)

    # formated_print("class className { public static void main ( String[] args ) { System.out.println ( Hello, World!)\n)

    # parse("x = 2 ; new_line y = 3 ;")

    # parse("( 1 )")
    # parse("( )")
    # parse("( 2 + 3 ) + 1")

    # test("imeFunkcije ( cijena ) { cijena = 1000 ; }",
    #      ["function", "(", ["args", ["cijena"]], ")", "{", ["body", ["instruction", ["LS", ["cijena"]], "=", ["RS", [1000]], ";"]], "}"])

    # test("imeFunkcije ( ) { cijena = 1000 ; }",
    #      [
    #          "function",
    #          "(",
    #          ["args", []],
    #          ")",
    #          "{",
    #          ["body", ["instruction", ["LS", ["cijena"]], "=", ["RS", [1000]], ";"]],
    #          "}"
    #      ]
    # )

    # test("imeFunkcije ( ) { cijena = 1000 ; int x = 3 ; }",
    #      ["function",
    #       "(",
    #       ["args", []],
    #       ")",
    #       "{",
    #       ["body",
    #        ["instruction", ["LS", ["cijena"]], "=", ["RS", [1000]], ";"],
    #        ["instruction", ["LS", ["int", "x"]], "=", ["RS", [3]], ";"]
    #       ],
    #       "}"
    #       ])

    print(80 * "=")
    print("all tests passed")
    print(80 * "=")

    # parse("1 + 1")
    # parse('3 * ( 2 + - 4 ) ^ 4')
    # parse("1 - 1 + 1")
    # parse("var + 3")
    # parse("var + 3 + 3")
    # parse('3 * ( 2 + - 4 ) ^ var')
    # parse("cijena = 1000 ;")
    # parse("int cijena = 1000 ;")
    # parse("int cijena = 1000 + 20 ;")
    # parse("cijena = 1000 ;")
    # print(parse("variable = value ;"))

    """
        izracunajCijenu() {
            ako ( kolicina > 20 )
                cijena = 1000 ;
            inace
                cijena = 1200 ;
            novaCijena = cijena ;
        }
        
        program 
            izracunajCijenu
            (
            )
            blokNaredbi
                {
                slijedNaredbi
                    naredba
                        ako
                        (
                        izraz
                            kolicina 
                            > 
                            20
                        )
                        naredba
                            cijena
                            = 
                            1000
                            ;
                        inace
                        naredba
                            cijena
                            =
                            1200
                            ;
                    naredba
                        novacijena
                        =
                        cijena
                        ;
                }
                
    """
