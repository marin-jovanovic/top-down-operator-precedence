import re

# todo check this statement
# keywords and reserved words are treated as the same
KEYWORDS_PREFIX = "KW__"
# TOKENS = {(line[:-1] if line.count(" ") == 0 else (line[:-1].split(" ", 1))[1]):
#               (line[:-1].upper() if line.count(" ") == 0 else ((line[:-1].split(" "))[0]).upper())
#           for line in open("..\\resources\\TOKENS.txt").readlines()}
TOKENS = {(line[:-1] if line.count(" ") == 0 else (line[:-1].split(" ", 1))[1]):
              (line[:-1] if line.count(" ") == 0 else ((line[:-1].split(" "))[0]))
          for line in open("..\\resources\\TOKENS.txt").readlines()}
# print(KEYWORDS)

BNF_PATH = "..\\resources\\thrift_BNF.txt"
SOURCE_CODE = "".join([line for line in open("..\\resources\\thrift_source_code_samples\\code4.thrift").readlines()])


class Token:

    def __init__(self, identifier, row, value):
        self.identifier = identifier
        self.row = row
        self.value = value

    def __str__(self):
        return self.identifier + " " + str(self.row) + " " + self.value


# todo delete this
def extractor():

    # print("\n*** source code ***")
    # print(raw_data)

    have_i_eaten = False

    new_rules = []

    while True:

        for rule in open(BNF_PATH).readlines():

            # print()
            # print(rule)
            rule = rule[:-1]
            raw = rule.split("::=  ")
            t = raw[0].index(" ")

            name = ((raw[0].strip())[t + 1:]).replace(" ", "")

            transition = raw[1]

            # print(name)
            # print(transition)

            is_ok = True

            if not transition.count("?") == transition.count("\?"):
                is_ok = False

            elif bool(re.search('[a-zA-Z]+ ', transition)):
                is_ok = False

            elif bool(re.search('[a-zA-Z]+\*', transition)):
                is_ok = False

            # elif bool(re.search('[a-zA-Z]+', transition)):
            #     print(rule)
            #
            #     is_ok = False

            if is_ok:
                new_rules.append(rule)

        if not have_i_eaten:
            break

        have_i_eaten = True

    print("\n*** new rules ***")
    [print(i) for i in new_rules]


def lex_driver():
    source_code = SOURCE_CODE
    output = []
    row_number = 1

    have_i_eaten = False

    while True:

        for keyword, keyword_id in TOKENS.items():
            if len(keyword.split(" ")) == 2:
                # regex
                regex = (keyword.split(" "))[1]
                if re.match(regex, source_code):

                    output.append(Token(keyword_id, row_number, source_code[:re.match(regex, source_code).end()]))

                    # output.append(Token(keyword_id, row_number, str(re.match(regex, source_code).end())))

                    source_code = regex_cropper((keyword.split(" "))[1], source_code)

                    have_i_eaten = True
                    break

            else:
                # match
                if source_code.startswith(keyword):
                    output.append(Token(KEYWORDS_PREFIX + keyword_id, row_number, keyword))
                    source_code = source_code[len(keyword):]
                    have_i_eaten = True
                    break

        # space
        if source_code.startswith(" "):
            source_code = source_code[1:]

            have_i_eaten = True

        # new row
        elif source_code.startswith("\n"):
            source_code = source_code[1:]
            row_number += 1

            have_i_eaten = True

        # multiline comment
        elif source_code.startswith("/**"):

            source_code = source_code[3:]

            while not source_code.startswith("*/"):
                if source_code.startswith("\n"):
                    row_number += 1
                source_code = source_code[1:]

            source_code = source_code[2:]

            have_i_eaten = True

        # elif re.match(r"([a-z]|[A-Z]|_)([a-z]|[A-Z]|[0-9]|\.|_)*", source_code):
        #
        #     end = re.match(r"([a-z]|[A-Z]|_)([a-z]|[A-Z]|[0-9]|\.|_)*", source_code).end()
        #     token = source_code[:end]
        #     output.append(Token("IDENTIFIER", row_number, token))
        #     source_code = source_code[end:]
        #
        #     have_i_eaten = True

        if not have_i_eaten:
            print("error while lexing?")
            break

        have_i_eaten = False

    print("\n*** output ***")

    [print(i) for i in output]

    print("\n*** source code ***")
    print(source_code)


def regex_cropper(regex, string):
    return string[re.match(regex, string).end():] if re.match(regex, string) else string


if __name__ == '__main__':

    [print(k + " -> " + v) for k, v in TOKENS.items()]

    print("\n*** source code ***")
    print(SOURCE_CODE)
    # reg = "\" [^\"]* \""
    # print(reg)
    #
    # testni = "\" blabla \"jfainowan"
    # print(testni)
    # print("01234567890123456")
    # if re.match(reg, testni):
    #     print("da")
    #     end = re.match(reg, testni).end()
    #     print(end)
    #     testni = testni[end:]
    #     print(testni)
    #

    # print(regex_cropper(reg, "\" blabla \"jfainowan"))
    lex_driver()
