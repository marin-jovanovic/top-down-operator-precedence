def print_green(data):
    print("\033[92m" + data + "\033[0m")


def print_blue(data):
    print("\33[34m" + data + "\033[0m")


def print_red(data):
    print("\33[31m" + data + "\033[0m")


def fn(items, level=0, result=[]):
    """printer"""
    for item in items:
        if isinstance(item, list):
            fn(item, level + 1, result)
        else:
            indentation = " " * level
            # print('%s%s' % (indentation, item))
            result.append('%s%s' % (indentation, item))

    return result


NAMESPACE_PREFIX = "NS__"
BASETYPE_PREFIX = "BT__"
IDENTIFIER_PREFIX = "ID__"
ENABLE_LOG = False
LBP = {
    "Literal": 1,
    "NamespaceScope": 1,
    "EOF": -1,
    "Identifier": 1,
    "BaseType": 1,
    "Keyword": 1
    }
HEADER_RBP = 0
DEFINITION_RBP = 0
err_message_not_same_type = "err: wrong type"
err_message_no_optional_t = "err: no optional token"
DEFINITION_STARTER_FLAG = False
DEFINITION_STARTERS = ["const", "typedef", "enum", "senum", "struct", "union",
                       "exception", "service"]
# test_prefix = "../tests/"
# test = "003 include2.in"
def printerr(msg):
    print_red(str(msg))
    import sys
    sys.exit()