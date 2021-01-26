from thrift_parser.main import expression
from thrift_parser.main import match

class VariableToken(object):

    def __init__(self, name):
        self.name = name

    def nud(self):
        pass

    def led(self, left):
        pass


class NamespaceScopeToken(object):

    def __init__(self, name):
        self.name = name

    def nud(self):

        match()

        return ["namespace"]


class KeywordToken(object):

    def __init__(self, name):
        self.name = name



# fixme lbp, expression
class EqualToken():
    lbp = "todo"

    def led(self, left):

        return [left, "=", expression(self.lbp)]