def get_all_input_symbols(s):
    symbols = list()
    symbols.append("ignore")

    for i_0, token_0 in enumerate(s):

        symbol = token_0[1]

        if not symbols.__contains__(symbol) and symbol != "$":
            symbols.append(symbol)

    # symbols.sort()
    symbols.append("$")

    return symbols


def converter_driver(s):

    input_symbols = get_all_input_symbols(s)
    print("input_symbols", input_symbols)
    print()

    state_table = list()

    for i_0, transition in enumerate(s):
        print(i_0, transition)

        source_state = transition[0]
        input_symbol = transition[1]
        destination_state = transition[2]

        is_match_found_in_state_table = False

        for i_1, t_1 in enumerate(state_table):

            if t_1[0] == source_state:
                is_match_found_in_state_table = True
                break

        if is_match_found_in_state_table:
            print("match found")
            print(i_1, t_1)



        else:
            print("match not found")
            t_0 = [source_state]

            for i_2, t_2 in enumerate(input_symbols):

                if t_2 == input_symbol:
                    t_0.append(destination_state)
                else:
                    t_0.append([])

            print("adding new line to table", t_0)

            state_table.append(t_0)

        print()



    #
    # # first elem
    # token_0 = s[0]
    # source_state = token_0[0]
    # input_symbol = token_0[1]
    # destination_state = token_0[2]
    # t_0 = list()
    #
    # t_0.append(source_state)
    #
    # for i_2, token_2 in enumerate(input_symbols):
    #
    #     if input_symbol == token_2:
    #         print("match for " + token_2)
    #         t_0.append(destination_state)
    #
    #     else:
    #         print("no match for " + token_2)
    #         t_0.append([])
    #
    # state_table.append(t_0)
    # print("state_table", state_table)
    #
    # # other
    # for i_0, token_0 in enumerate(s[1:]):
    #
    #     source_state = token_0[0]
    #     input_symbol = token_0[1]
    #     destination_state = token_0[2]
    #
    #     is_in_table = False
    #
    #     index_to_remove = -1
    #
    #     for i_1, token_1 in enumerate(state_table):
    #         print("token_1", token_1)
    #         if token_1[0] == source_state:
    #             print("exists in state_table")
    #
    #             # line in table
    #             t_0 = token_1
    #             index_to_remove = i_1
    #
    #             for i_2, token_2 in enumerate(input_symbols):
    #
    #                 if input_symbol == token_2:
    #                     print("match for " + token_2)
    #
    #                     break
    #
    #             is_in_table = True
    #             break
    #
    #     if is_in_table:
    #         print("new val for table")
    #         print(t_0)
    #
    #         state_table[index_to_remove] = state_table[index_to_remove].append(destination_state)
    #         # remove and add
    #
    #         pass
    #
    #     else:
    #         print("does not exist in state_table")
    #         t_0 = list()
    #
    #         t_0.append(source_state)
    #
    #         for i_2, token_2 in enumerate(input_symbols):
    #
    #             if input_symbol == token_2:
    #                 print("match for " + token_2)
    #                 t_0.append(destination_state)
    #
    #             else:
    #                 print("no match for " + token_2)
    #                 t_0.append([])
    #
    #         state_table.append(t_0)

    return state_table


if __name__ == '__main__':
    s = [
        ["A", "1", "A"],
        ["A", "$", "B"],
        ["A", "0", "B"],
        ["A", "0", "C"],

        ["B", "1", "B"],
        ["B", "$", "C"],

        ["C", "0", "C"],
        ["C", "1", "C"],
    ]

    [print(i) for i in s]
    print("*******************************************************")

    [print(i) for i in converter_driver(s)]
