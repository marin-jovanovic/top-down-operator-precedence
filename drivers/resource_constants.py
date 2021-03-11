# todo check this statement
# keywords and reserved words are treated as the same

KEYWORDS_PREFIX = "KW__"

'''
dict of tokens

example
TOKENS.txt
    include
    NamespaceScope *
    Literal r \"[^\"]*\"

TOKENS = {
    include : include
    * : NamespaceScope
    r \"[^\"]*\" : Literal
}

'''
# TOKENS = {(line[:-1] if line.count(" ") == 0 else (line[:-1].split(" ", 1))[1]):
#               (line[:-1] if line.count(" ") == 0 else ((line[:-1].split(" "))[0]))
#           for line in open("../resources/TOKENS.txt").readlines() if
#           not line.startswith("comment:") and not line.isspace()}

'''bnf grammar'''
# BNF_PATH = "..\\resources\\thrift_BNF.txt"

'''synchronization tokens'''
synchronization_tokens_path = "../resources/synchronization_tokens.txt"
SYNCHRONIZATION_TOKENS = []

for i in open(synchronization_tokens_path).readlines():
    if not (i.startswith("comment:") or i.isspace()):
        SYNCHRONIZATION_TOKENS.append(i[:-1])


def get_tokens():
    di = {}
    lines = open("../resources/TOKENS_2.txt").readlines()

    i = 0
    while True:
        i += 1
        try:
            line = lines[i]
        except IndexError:
            break

        if line.startswith("comment:") or line.isspace():
            continue

        key = str(line).strip()
        i += 1

        line = lines[i]

        temp = ""
        while line.startswith("\t"):
            if not (line.startswith("comment:") or line.isspace()):
                temp += str(line).strip() + "|"

            i += 1

            try:
                line = lines[i]
            except IndexError:
                break

        i -= 1
        di[key] = temp[:-1]

    return di


TOKENS = get_tokens()

if __name__ == '__main__':
    [print(k + " -> " + v) for k, v in TOKENS.items()]
