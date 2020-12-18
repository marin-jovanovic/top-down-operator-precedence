INPUT_LISTS = list(list())
STATES = list()
INPUT_SYMBOLS = list()
FINAL_STATES = list()
INITIAL_STATE = list()
TRANSITIONS = list()


class Transition_function:
  def __init__(self, curr_state, input_data, new_states):
    self.curr_state = str(curr_state)
    self.input_data = str(input_data)
    self.new_states = list()
    self.new_states = str(new_states).split(",")

  def __iter__(self):
    return self.by_id.iteritems()

  def __str__(self):
    return self.curr_state + ": " + self.input_data + " -> " + str(self.new_states)
