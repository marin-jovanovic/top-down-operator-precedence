import constants


# 1. line
# inputs separated by comma, input streams separated by "|"
# 2. line
# states separated by comma
# 3. line
# final states separated by comma
# 4. line
# initial state
# 5+ lines
# transition functions
def get_input():

    input_lists = input().split("|")
    for input_stream in input_lists:
        input_tokens = input_stream.split(",")
        constants.INPUT_LISTS.append(input_tokens)

    # constants.STATES.append(input().split(","))
    temp = input()
    constants.INPUT_SYMBOLS.append(input().split(","))
    constants.FINAL_STATES.append(input().split(","))
    constants.INITIAL_STATE = input()

    while True:
        try:
            transition_function = input()
            # x,y->z,f,d
            raw_data = transition_function.split("->")
            raw_data2 = raw_data[0].split(",")

            constants.TRANSITIONS.append(constants.Transition_function(raw_data2[0], raw_data2[1], raw_data[1]))

        except:
            break


# gets new states for current_state and current_input
# current_state, current_input -> list(new_states)
def get_new_states(current_state, current_input):
    new_states = set()

    for transition in constants.TRANSITIONS:
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
    new_states = set()

    for transition in constants.TRANSITIONS:
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
    current_states = set()
    current_states.add(constants.INITIAL_STATE)

    current_states = get_all_new_e_states(current_states)

    path = path_configure("", current_states)

    while len(input_list) != 0:

        current_input = input_list[0]
        input_list.pop(0)

        current_states = get_new_states_for_all_current_states(current_states, current_input)

        current_states = get_all_new_e_states(current_states)

        if len(current_states) == 0:
            for elem in range(len(input_list) + 1):
                path += "#|"
            return path[:-1]

        else:
            path = path_configure(path, current_states)

    return path[:-1]


def driver(data):
    input_lists = data[0].split("|")
    data.pop(0)

    for input_stream in input_lists:
        input_tokens = input_stream.split(",")
        constants.INPUT_LISTS.append(input_tokens)

    # constants.STATES.append(data[0].split(","))
    data.pop(0)

    constants.INPUT_SYMBOLS.append(data[0].split(","))
    data.pop(0)

    constants.FINAL_STATES.append(data[0].split(","))
    data.pop(0)

    constants.INITIAL_STATE = data[0]
    data.pop(0)

    while True:
        try:
            transition_function = data[0]
            data.pop(0)

            # x,y->z
            raw_data = transition_function.split("->")
            raw_data2 = raw_data[0].split(",")

            constants.TRANSITIONS.append(constants.Transition_function(raw_data2[0], raw_data2[1], raw_data[1]))

        except:
            break

    paths = list()
    for input_list in constants.INPUT_LISTS:
        paths.append(get_paths(input_list))

        print(get_paths(input_list))


F = list()

if __name__ == '__main__':
    #1 redak: Ulazni nizovi odvojeni znakom |. Simboli svakog pojedinog niza odvojeni su zarezom.
    #  2. redak: Leksikografski poredan skup stanja odvojenih zarezom.
    #  3. redak: Leksikografski poredan skup simbola abecede odvojenih zarezom.
    #  4. redak: Leksikografski poredan skup prihvatljivih stanja odvojenih zarezom.
    #  5. redak: Početno stanje.
    #  6. redak i svi ostali retci: Funkcija prijelaza u formatu

    t_in = list()
    t_in.append("a,pnp,a|pnp,lab2|pnp,a|pnp,lab2,utr,utr")
    t_in.append("p5,s3,s4,st6,stanje1,stanje2") #sva stanja
    t_in.append("a,lab2,pnp,utr") # svi inputi
    t_in.append("p5") # prihvatljivo
    t_in.append("stanje1") # pocetno
    t_in.append("s3,a->stanje2")
    t_in.append("s3,lab2->p5,s4")
    t_in.append("s4,$->st6")
    t_in.append("s4,utr->p5,s3")
    t_in.append("stanje1,a->stanje2")
    t_in.append("stanje1,pnp->s3")
    t_in.append("stanje2,$->st6")
    t_in.append("stanje2,a->#")

    driver(t_in)


    # ###################################################
    # get_input()
    #
    # for input_list in constants.INPUT_LISTS:
    #     print(get_paths(input_list))
#