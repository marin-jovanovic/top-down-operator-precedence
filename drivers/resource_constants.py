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
TOKENS = {(line[:-1] if line.count(" ") == 0 else (line[:-1].split(" ", 1))[1]):
              (line[:-1] if line.count(" ") == 0 else ((line[:-1].split(" "))[0]))
          for line in open("../resources/TOKENS.txt").readlines() if not line.startswith("comment:") and not line.isspace()}

'''bnf grammar'''
# BNF_PATH = "..\\resources\\thrift_BNF.txt"

'''synchronization tokens'''
synchronization_tokens_path = "../resources/synchronization_tokens.txt"
SYNCHRONIZATION_TOKENS = []

for i in open(synchronization_tokens_path).readlines():
    if not (i.startswith("comment:") or i.isspace()):
        SYNCHRONIZATION_TOKENS.append(i[:-1])

if __name__ == '__main__':
    import re
    t = "\"bkakbjaj\" dad ad d as s "
    # t = ""

    for keyword, keyword_id in TOKENS.items():
        print(keyword, "->", keyword_id)
    #     # print(len(keyword.split(" ")))
    #
    #     if not len(keyword.split(" ")) == 1:
    #         print(keyword[2:], keyword_id)
    #
    #         if re.match(re.compile(keyword[2:]), t):
    #             print("match")
    #             m = re.search(re.compile(keyword[2:]), t).group()
    #             print(m)
    # # [print(k, "->", v) for k, v in TOKENS.items()]
    #
    # # for keyword, keyword_id in TOKENS.items():
    # #     print(keyword, keyword_id)

