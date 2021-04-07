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
            print('%s%s' % (indentation, item))
            result.append('%s%s' % (indentation, item))

    return result