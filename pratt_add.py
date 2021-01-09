def tokenize(program):
    for operator in program.split(" "):
    # for number, operator in token_pat.findall(program):
        if operator.isnumeric():
            yield literal_token(operator)
        elif operator == "+":
            yield operator_add_token()
        else:
            raise SyntaxError('unknown operator: %s', operator)
    yield end_token()


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
    return left


class literal_token(object):
    def __init__(self, value):
        self.value = int(value)

    def nud(self):
        return str(self.value)


class operator_add_token(object):
    lbp = 10

    def nud(self):
        return expression(100)

    def led(self, left):
        right = expression(10)

        return "( " + left + " + " + right + " )"


class end_token(object):
    lbp = 0


if __name__ == '__main__':
    print(parse('1 + 2 + 3 + 4 + 5 + 6'))
    # print(parse("1-1+1"))

