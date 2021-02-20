from thrift_lexer.main import get_tokens
from resources.token_classes import Token

TOKENS = get_tokens("../resources/thrift_source_code_samples//test_code.thrift")
TOKEN = Token("", 0, "")

TOKEN_POINTER = 0


def get_next_token():
    global TOKEN_POINTER

    curr_token = TOKENS[TOKEN_POINTER]
    TOKEN_POINTER += 1
    return curr_token


def match(tok=None):
    global TOKEN
    if tok and tok != type(TOKEN):
        raise SyntaxError('Expected %s' % tok)
    TOKEN = get_next_token()


def parse():
    print("\n*** lbp ***")
    lbp = {((line.split(" "))[0]): ((line[:-1].split(" "))[1]) for line in open("left_binding_power.txt").readlines()}
    for k, v in lbp.items():
        print(k + " -> " + v)

    print("\n*** tokens ***")
    [print(i) for i in TOKENS]

    print(80 * "=")

    global TOKEN

    TOKEN = get_next_token()
    ret = expression()

    print("output:", ret)

    return ret


def expression(rbp=0):
    global TOKEN
    t = TOKEN
    TOKEN = get_next_token()
    left = t.nud()
    while rbp < TOKEN.lbp:
        t = TOKEN
        TOKEN = get_next_token()
        left = t.led(left)
    return left


if __name__ == '__main__':

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
