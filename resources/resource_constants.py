# todo check this statement
# keywords and reserved words are treated as the same
KEYWORDS_PREFIX = "KW__"

TOKENS = {(line[:-1] if line.count(" ") == 0 else (line[:-1].split(" ", 1))[1]):
          (line[:-1] if line.count(" ") == 0 else ((line[:-1].split(" "))[0]))
          for line in open("../resources/TOKENS.txt").readlines()}

# BNF_PATH = "..\\resources\\thrift_BNF.txt"

if __name__ == '__main__':
    pass


