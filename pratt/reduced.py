SPACE_COUNT = 0
MAX_OFFSET = 0

LBP = {
    "variable_type": -1,
    "variable": None,
    "literal": None,
    "lparen": 0,
    "rparen": 0,
    "EOF": 0,
    "end_of_line": 0,
    "association": 5,
    "add": 10,
    "sub": 10,
    "mul": 20,
    "div": 20,
    "pow": 30

}
AST = []

def format_print(data):
    print((MAX_OFFSET + SPACE_COUNT) * " " + str(data))

def add_to_AST(data):
    AST.append((MAX_OFFSET + SPACE_COUNT) * " " + str(data))

def tokenize(program):
    for operator in program.split(" "):
        if operator.isnumeric():
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
            yield operator_lparen_token()
        elif operator == ')':
            yield operator_rparen_token()
        elif operator[0].isalpha():
            yield variable_token(operator)
        elif operator == "=":
            yield operator_association_token()
        elif operator == ";":
            yield operator_end_of_line_token()
        elif operator == "int":
            yield
        else:
            raise SyntaxError('unknown operator: %s', operator)
    yield end_token()


def match(tok=None):
    global token
    if tok and tok != type(token):
        raise SyntaxError('Expected %s' % tok)
    token = next.__next__()


def parse(program):
    global token, next

    next = tokenize(program)

    token = next.__next__()

    print(80 * "=")
    print("source:", program)

    ret = expression()
    print("output:", ret)
    # print("AST:")
    # for i in AST:
    #     print(i)
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
    return str(left)


class operator_int_type_token(object):
    lbp = LBP.get("variable_type")

    def nud(self):
        return

class operator_end_of_line_token(object):
    lbp = LBP.get("end_of_line")

    def led(self, left):
        return "(" + str(left) + ") (;)"


class operator_association_token(object):
    lbp = LBP.get("association")

    def nud(self):

        return expression(100)

    def led(self, left):
        right = expression(self.lbp)
        return "( ({0}) (=) {1} )".format(str(left), str(right))


class variable_token(object):
    def __init__(self, value):
        self.value = str(value)

    def nud(self):
        ret = "(" + self.value + ")"
        return ret

    def lbp(self):
        return "(" + self.value + ")"


# number
class literal_token(object):

    def __init__(self, value):
        self.value = int(value)

    def nud(self):
        return "(" + str(self.value) + ")"


class operator_add_token(object):
    lbp = LBP.get("add")

    def nud(self):
        return expression(100)

    def led(self, left):

        right = expression(self.lbp)
        return "( {0} (+) {1} )".format(str(left), str(right))
        # return left + right


class operator_sub_token(object):
    lbp = LBP.get("sub")

    def nud(self):
        return "( (-) " + str(expression(100)) + " )"

    def led(self, left):
        # alt enter
        return "( {0} - {1} )".format(str(left), str(expression(self.lbp)))


class operator_mul_token(object):
    lbp = LBP.get("mul")

    def led(self, left):
        return "( " + str(left) + " (*) " + str(expression(self.lbp)) + " )"


class operator_div_token(object):
    lbp = LBP.get("div")

    def led(self, left):
        return "( " + str(left) + " / " + str(expression(self.lbp)) + " )"


class operator_pow_token(object):
    lbp = LBP.get("pow")

    def led(self, left):
        return [left, "^",expression(self.lbp - 1)]
        return "( " + str(left) + " (^) " + str(expression(self.lbp - 1)) + " )"


class operator_lparen_token(object):
    lbp = LBP.get("lparen")

    def nud(self):
        expr = expression(self.lbp)
        match(operator_rparen_token)
        return "( " + str(expr) + " )"


class operator_rparen_token(object):
    lbp = LBP.get("rparen")


class end_token(object):
    lbp = LBP.get("EOF")


if __name__ == '__main__':
    t = parse('3 * ( 2 + - 4 ) ^ 4')

    print(parse("1 - 1 + 1"))

    print(parse("var + 3"))
    print(parse("var + 3 + 3"))
    print(parse('3 * ( 2 + - 4 ) ^ var'))
    print(parse("cijena = 1000 ;"))
    parse("int cijena = 1000 ;")
    parse("int cijena = 1000 + 20 ;")
    parse("cijena = 1000 ;")
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