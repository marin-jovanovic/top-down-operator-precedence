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
    return expression()


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


class variable_token(object):
    def __init__(self, value):
        self.value = str(value)

    lbp = 10

    def nud(self):
        return "( " + str(expression(100)) + " )"

    def led(self, left):
        right = expression(10)
        return "( " + str(left) + " + " + str(right) + " )"


class operator_sub_token(object):
    lbp = 10

    def nud(self):
        # return str(expression(100))
        return "( - " + str(expression(100)) + " )"

    def led(self, left):
        # alt enter
        return "( {0} - {1} )".format(str(left), str(expression(10)))


class operator_mul_token(object):
    lbp = 20

    def led(self, left):
        return "( " + str(left) + " * " + str(expression(20)) + " )"


class operator_div_token(object):
    lbp = 20

    def led(self, left):
        return "( " + str(left) + " / " + str(expression(20)) + " )"


class operator_pow_token(object):
    lbp = 30

    def led(self, left):
        return "( " + str(left) + " ^ " + str(expression(30 - 1)) + " )"


class operator_lparen_token(object):
    lbp = 0

    def nud(self):
        expr = expression()
        match(operator_rparen_token)
        return "( " + str(expr) + " )"


class operator_rparen_token(object):
    lbp = 0


class end_token(object):
    lbp = 0


if __name__ == '__main__':
    print(parse('3 * ( 2 + - 4 ) ^ 4'))
    # print(parse("1-1+1"))

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