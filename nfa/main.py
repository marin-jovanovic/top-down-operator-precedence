# import nfa.constants
# impoa.constants

INPUT_LIST = list()
STATES = list()
INPUT_SYMBOLS = list()
FINAL_STATES = list()
INITIAL_STATE = list()
TRANSITIONS = list()

# ID = 0

class Transition_function:
    def __init__(self, curr_state, input_data, new_states):
        # global ID
        # self.by_id = ID
        # ID += 1
        self.curr_state = str(curr_state)
        self.input_data = str(input_data)
        self.new_states = list()
        self.new_states = str(new_states).split(",")

    def __iter__(self):
        return self.by_id.iteritems()

    def __str__(self):
        return self.curr_state + ": " + self.input_data + " -> " + str(self.new_states)


# gets new states for current_state and current_input
# current_state, current_input -> list(new_states)
def get_new_states(current_state, current_input):
    global TRANSITIONS
    new_states = set()

    for transition in TRANSITIONS:
        if current_state == transition.curr_state and current_input == transition.input_data:
            for state in transition.new_states:
                if state != "#":
                    new_states.add(state)

    return new_states


# gets new states for current_states
# current_state, current_input -> list(new_states)
def get_new_states_for_all_current_states(current_states, current_input):
    new_states_buffer = set()

    for current_state in current_states:

        new_states = get_new_states(current_state, current_input)

        for new_state in new_states:
            if new_state not in new_states_buffer:
                new_states_buffer.add(new_state)
    return new_states_buffer


# returns list of new states for only ONE state
def get_new_e_states(current_state):
    global TRANSITIONS
    new_states = set()

    for transition in TRANSITIONS:
        if current_state == transition.curr_state and transition.input_data == "$":
            for state in transition.new_states:
                if state != "#":
                    new_states.add(state)
    return new_states


# returns list of new states for ALL current states
def get_all_new_e_states(current_states):
    old_states = set()
    new_states = current_states

    while old_states != new_states:
        for state in new_states:
            old_states.add(state)

        for current_state in old_states:

            new_states_buffer = get_new_e_states(current_state)

            for new_state in new_states_buffer:
                new_states.add(new_state)

    return current_states


def path_configure(path, current_states):
    for current_state in sorted(current_states):
        path += current_state + ","

    return path[:-1] + "|"


def get_paths(input_list):
    global INITIAL_STATE
    current_states = set()
    current_states.add(INITIAL_STATE)

    current_states = get_all_new_e_states(current_states)

    path = path_configure("", current_states)

    while len(input_list) != 0:

        current_input = input_list.pop(0)

        current_states = get_new_states_for_all_current_states(current_states, current_input)

        current_states = get_all_new_e_states(current_states)

        if len(current_states) == 0:
            # for elem in range(len(input_list) + 1):
            #     path += "#|"
            return path[:-1]

        else:
            path = path_configure(path, current_states)

    return path[:-1]


def driver(data):
    global INPUT_LIST, INPUT_SYMBOLS, FINAL_STATES, INITIAL_STATE, TRANSITIONS, Transition_function, STATES

    INPUT_LIST = list(data.pop(0))

    FINAL_STATES.append(data[0].split(","))
    data.pop(0)

    INITIAL_STATE = data[0]
    data.pop(0)

    while True:
        try:
            transition_function = data.pop(0)

            TRANSITIONS.append(Transition_function(transition_function[0],
                                                   transition_function[1],
                                                   transition_function[2]))

        except:
            break

    ret = get_paths(INPUT_LIST)
    print(ret)
    print("i have eaten " + str(ret.count("|")) + " token" + ("s" if ret.count("|") > 1 else ""))


if __name__ == '__main__':

    # #| ovo je primjer |#
    # 3 -  -0x12 - ( #| ovdje ce doci grupirane
    # 		operacije |#
    # 3- -
    # --076) #| 3 - ---076 = 3 - -076 = 3 + 076 |#

    # accept state
    # start state

    t_in = [
        "#|ovo je primjer",
        "S_2",
        "S_0",
        ["S_0", "#", "S_1"],
        ["S_1", "|", "S_2"]
    ]

    # # ['S_pocetno', '-(\\t|\\n|\\_)*-', ['OP_MINUS', 'UDJI_U_STANJE S_unarni', 'VRATI_SE 1']]
    # if current_state == "S_pocetno":
    #     pass
    # # ['S_0', '-', 'S_1']
    # # ['S_1', '$', 'S_2']
    # # ['S_2', '\\t', 'S_3']
    # # ['S_1', '$', 'S_4']
    # # ['S_4', '\\n', 'S_5']
    # # ['S_1', '$', 'S_6']
    # # ['S_6', '\\_', 'S_7']
    # # ['S_3', '$', 'S_8']
    # # ['S_5', '$', 'S_8']
    # # ['S_7', '$', 'S_8']
    # # ['S_3', '$', 'S_1']
    # # ['S_5', '$', 'S_1']
    # # ['S_7', '$', 'S_1']
    # # ['S_1', '$', 'S_8']
    # # ['S_8', '-', 'S_9']

    t_in = [
        "-\t\t\t\t- lalalal",
        "S_9",
        "S_0",
        ['S_0', '-', 'S_1'],
        ['S_1', '$', 'S_2'],
        ['S_2', '\t', 'S_3'],
        ['S_1', '$', 'S_4'],
        ['S_4', '\n', 'S_5'],
        ['S_1', '$', 'S_6'],
        ['S_6', ' ', 'S_7'],
        ['S_3', '$', 'S_8'],
        ['S_5', '$', 'S_8'],
        ['S_7', '$', 'S_8'],
        ['S_3', '$', 'S_1'],
        ['S_5', '$', 'S_1'],
        ['S_7', '$', 'S_1'],
        ['S_1', '$', 'S_8'],
        ['S_8', '-', 'S_9']
    ]

    driver(t_in)

    # #####################################################################

    # t_in = []
    #
    # while True:
    #     try:
    #         t_in.append(input())
    #     except EOFError:
    #         break
    #
    # driver(t_in)
