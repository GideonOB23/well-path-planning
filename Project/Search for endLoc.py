#this function initializes the agent in valid place
def get_starting_location(self):
    current_row_index = np.random.randint(self.environment_rows)
    current_column_index = np.random.randint(self.environment_columns)
    while self.is_terminal_state(current_row_index, current_column_index):
        current_row_index = np.random.randint(self.environment_rows)
        current_column_index = np.random.randint(self.environment_columns)
    return current_row_index, current_column_index


def get_next_action(self, current_row_index, current_column_index, epsilon):
        if np.random.random() < epsilon and np.var(self.q_values[current_row_index, current_column_index]) > 0:
            return np.argmax(self.q_values[current_row_index, current_column_index])
        else:
            return np.random.randint(4)
        

#once the action is chosen,you need to know the location after making that action
def get_next_location(self, current_row_index, current_column_index, action_index):
    new_row_index = current_row_index
    new_column_index = current_column_index
    if self.actions[action_index] == 'up' and current_row_index > 0:
        new_row_index -= 1
    elif self.actions[action_index] == 'right' and current_column_index < self.environment_columns - 1:
        new_column_index += 1
    elif self.actions[action_index] == 'down' and current_row_index < self.environment_rows - 1:
        new_row_index += 1
    elif self.actions[action_index] == 'left' and current_column_index > 0:
        new_column_index -= 1
    return new_row_index, new_column_index