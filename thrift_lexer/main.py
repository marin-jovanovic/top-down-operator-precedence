import re

# todo check this statement
# keywords and reserved words are treated as the same
KEYWORDS_PREFIX = "KW__"
KEYWORDS = [line[:-1] for line in open("..\\resources\\KEYWORDS_AND_RESERVED_WORDS.txt").readlines()]
print(KEYWORDS)


class Token:

    def __init__(self, identifier, row, value):
        self.identifier = identifier
        self.row = row
        self.value = value

    def __str__(self):
        return self.identifier + " " + str(self.row) + " " + self.value + "|"


if __name__ == '__main__':
    raw_data = "".join([line for line in open("..\\resources\\thrift_source_code_samples\\code4.thrift").readlines()])

    output = []
    row_number = 1


    print("\n*** source code ***")
    print(raw_data)

    have_i_eaten = False

    while True:

        for keyword in KEYWORDS:
            if raw_data.startswith(keyword):
                output.append(Token(KEYWORDS_PREFIX + keyword.upper(), row_number, keyword))
                raw_data = raw_data[len(keyword):]

                have_i_eaten = True

        if raw_data.startswith(" "):
            raw_data = raw_data[1:]

            have_i_eaten = True

        elif raw_data.startswith("\n"):
            raw_data = raw_data[1:]
            row_number += 1

            have_i_eaten = True

        elif raw_data.startswith("/**"):
            raw_data = raw_data[3:]

            while not raw_data.startswith("*/"):
                raw_data = raw_data[1:]

            raw_data = raw_data[2:]

            have_i_eaten = True

        elif re.match(r"([a-z]|[A-Z]|_)([a-z]|[A-Z]|[0-9]|\.|_)*", raw_data):

            end = re.match(r"([a-z]|[A-Z]|_)([a-z]|[A-Z]|[0-9]|\.|_)*", raw_data).end()
            token = raw_data[:end]
            output.append(Token("IDENTIFIER", row_number, token))
            raw_data = raw_data[end:]

            have_i_eaten = True

        if not have_i_eaten:
            print("error while lexing?")
            break

        have_i_eaten = False

    print("\n*** output ***")

    [print(i) for i in output]

    print("\n*** source code ***")
    print(raw_data)


