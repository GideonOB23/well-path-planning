 #stop conditions 1.crushed into hard obstacle
                   # 2.reached endLoc
def is_terminal_state(self, current_row_index, current_column_index):
    return (self.rewards[current_row_index, current_column_index] == config["hardWeight"]) or ((self.rewards[current_row_index, current_column_index] == config['reward']))