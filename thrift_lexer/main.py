import re

# todo check this statement
# keywords and reserved words are treated as the same
from resources.resource_constants import KEYWORDS_PREFIX, TOKENS




class Token:

    def __init__(self, identifier, row, value):
        self.identifier = identifier
        self.row = row
        self.value = value

    def __str__(self):
        return self.identifier + " " + str(self.row) + " " + self.value


def get_tokens(source_code_path):
    source_code = "".join([line for line in open(source_code_path).readlines()])
    output = []

    row_number = 1

    have_i_eaten = False

    while True:

        if source_code == "":
            print("lexer; ok")
            # import sys
            # sys.exit()
            break

        for keyword, keyword_id in TOKENS.items():
            if len(keyword.split(" ")) == 1:
                # direct match
                if source_code.startswith(keyword):
                    output.append(Token(KEYWORDS_PREFIX + keyword_id, row_number, keyword))
                    source_code = source_code[len(keyword):]

                    have_i_eaten = True
                    break

            else:
                # regex match
                regex = keyword[2:]
                if re.match(regex, source_code):
                    output.append(Token(keyword_id, row_number, source_code[:re.match(regex, source_code).end()]))
                    source_code = regex_cropper(regex, source_code)

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

        elif source_code.startswith("#") or source_code.startswith("//"):
            while not source_code.startswith("\n"):
                source_code = source_code[1:]

            source_code = source_code[1:]
            row_number += 1
            have_i_eaten = True

        # multiline comment
        elif source_code.startswith("/*"):

            source_code = source_code[2:]
            # todo check if row starts with "*"
            while not source_code.startswith("*/"):
                if source_code.startswith("\n"):
                    row_number += 1
                source_code = source_code[1:]

            # handles */
            source_code = source_code[2:]

            have_i_eaten = True

        if not have_i_eaten:
            print("error while lexing?")
            break

        have_i_eaten = False

    # print("\n*** output ***")
    #
    # [print(i) for i in output]
    #
    # print("\n*** source code ***")
    # print(source_code)

    return output


def regex_cropper(regex, string):
    return string[re.match(regex, string).end():] if re.match(regex, string) else string


if __name__ == '__main__':
    # print("*** tokens ***")
    # [print(k + " -> " + v) for k, v in TOKENS.items()]
    #
    # print("\n*** source code ***")
    # print(SOURCE_CODE)

    [print(i) for i in get_tokens("../resources/thrift_source_code_samples\\code4.thrift")]
