if __name__ == '__main__':

    current_state = "S_pocetno"

    source_code = "".join([i for i in open("test_cases/minusLang.in").readlines()])

    print(list(source_code))

    # ['S_pocetno', '\\t|\\_', ['-']]

    if current_state == "S_pocetno":

        if source_code.startswith("\t"):
            print(1)

        # todo
        if source_code.startswith(" "):
            print(2)

    # ['S_pocetno', '\\n', ['-', 'NOVI_REDAK']]
    if current_state == "S_pocetno":

        if source_code.startswith("\n"):
            print(3)

    # ['S_pocetno', '#\\|', ['-', 'UDJI_U_STANJE S_komentar']]
    if current_state == "S_pocetno":

        # todo
        if source_code.startswith("#|"):
            print(4)

    # ['S_komentar', '\\|#', ['-', 'UDJI_U_STANJE S_pocetno']]
    if current_state == "S_komentar":

        if source_code.startswith("|#"):
            print(5)

    # ['S_komentar', '\\n', ['-', 'NOVI_REDAK']]
    if current_state == "S_komentar":

        if source_code.startswith("\n"):
            print(6)

    # ['S_komentar', '(\\(|\\)|\\{|\\}|\\||\\*|\\\\|\\$|\\t|\\n|\\_|!|"|#|%|&|\'|+|,|-|.|/|0|1|2|3|4|5|6|7|8|9|:|;|<|=|>|?|@|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|[|]|^|_|`|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|~)', ['-']]
    if current_state == "S_komentar":

        if source_code.startswith("."):
            print(7)

    # ['S_pocetno', '((0|1|2|3|4|5|6|7|8|9)(0|1|2|3|4|5|6|7|8|9)*|0x((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D|E|F)((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D|E|F)*)', ['OPERAND']]
    if current_state == "S_pocetno":
        if source_code.startswith(r"[0-9]"):
            print(8)


    if current_state == "S_pocetno":
        if
    source_code.startswith("
    if current_state == "S_pocetno":
        if
    source_code.startswith("
    if current_state == "S_pocetno":
        if
    source_code.startswith("
    if current_state == "S_pocetno":
        if
    source_code.startswith("
    if current_state == "S_pocetno":
        if
    source_code.startswith("
                           ['S_1, \\t -> S_2', 'S_1, \\_ -> S_2']
    if current_state == "S_unarni":
        if
    source_code.startswith("
    if current_state == "S_unarni":
        if
    source_code.startswith("
    if current_state == "S_unarni":
        if
    source_code.startswith("
    if current_state == "S_unarni":
        if
    source_code.startswith("




# ['S_pocetno', '\\(', ['LIJEVA_ZAGRADA']]
# ['S_pocetno', '\\)', ['DESNA_ZAGRADA']]
# ['S_pocetno', '-', ['OP_MINUS']]
# ['S_pocetno', '-(\\t|\\n|\\_)*-', ['OP_MINUS', 'UDJI_U_STANJE S_unarni', 'VRATI_SE 1']]
# ['S_pocetno', '\\((\\t|\\n|\\_)*-', ['LIJEVA_ZAGRADA', 'UDJI_U_STANJE S_unarni', 'VRATI_SE 1']]
# ['S_unarni', '\\t|\\_', ['-']]
# ['S_unarni', '\\n', ['-', 'NOVI_REDAK']]
# ['S_unarni', '-', ['UMINUS', 'UDJI_U_STANJE S_pocetno']]
# ['S_unarni', '-(\\t|\\n|\\_)*-', ['UMINUS', 'VRATI_SE 1']]
