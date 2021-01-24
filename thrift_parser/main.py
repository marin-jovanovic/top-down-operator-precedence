from thrift_lexer.main import get_tokens
from thrift_lexer.main import Token

TOKENS = get_tokens("..//resources//thrift_source_code_samples//test_code.thrift")
token = Token("", 0, "")

token_pointer = 0


def get_next_token():
    global token_pointer

    curr_token = TOKENS[token_pointer]
    token_pointer += 1
    return curr_token


def match(tok=None):
    global token
    if tok and tok != type(token):
        raise SyntaxError('Expected %s' % tok)
    token = get_next_token()


def parse():
    print(80 * "=")

    global token

    token = get_next_token()
    ret = expression()

    print("output:", ret)

    return ret


def expression(rbp=0):
    global token
    t = token
    token = get_next_token()
    left = t.nud()
    while rbp < token.lbp:
        t = token
        token = get_next_token()
        left = t.led(left)
    return left


if __name__ == '__main__':

    print("\n*** lbp ***")
    lbp = {((line.split(" "))[0]): ((line[:-1].split(" "))[1]) for line in open("left_binding_power.txt").readlines()}
    for k, v in lbp.items():
        print(k + " -> " + v)

    print("\n*** tokens ***")
    [print(i) for i in TOKENS]

    ast = parse()

    # parse(tokens)
    # [5]  Namespace       ::=  ( 'namespace' ( NamespaceScope Identifier ) )


# class Token:
#
#     def __init__(self, identifier, row, value):
#         self.identifier = identifier
#         self.row = row
#         self.value = value
#
#     def __str__(self):
#         return self.identifier + " " + str(self.row) + " " + self.value
