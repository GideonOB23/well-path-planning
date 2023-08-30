#AFTER TRAINING
    #accepts the endLocation,and returns the shortest path to that location from startLoc
    #once you train the agent,you can call this function(without training again),with different end point
    #if you want to change the startLocation,you must train agent again
def get_shortest_path(self, start_row_index, start_column_index,epsilon=1,stuck_ok = 100):
        
        shortest_path = []
        if self.is_terminal_state(start_row_index, start_column_index):
            return shortest_path
        else:
            current_row_index, current_column_index = start_row_index, start_column_index
            shortest_path.append([current_row_index, current_column_index])
            
        counter = 0
        stuck_count = 0
        got_stuck = False        
            
        while not self.is_terminal_state(current_row_index, current_column_index) and not got_stuck:
                        
            old_row_index, old_column_index = current_row_index, current_column_index 
            prev = None if len(shortest_path) < 2 else shortest_path[-2]

            if prev is None:

                action_index = self.get_next_action(old_row_index, old_column_index, epsilon)
                current_row_index, current_column_index = self.get_next_location(old_row_index, old_column_index, action_index)

            else:
                found_valid = False
                
                current_epsilon = epsilon

                while not found_valid:

                    action_index = self.get_next_action(old_row_index, old_column_index, current_epsilon)
                    current_row_index, current_column_index = self.get_next_location(old_row_index, old_column_index, action_index)

                    if abs(current_row_index-prev[0]) > 0 or abs(current_column_index-prev[1]) > 0:
                        found_valid = True
                        
                    current_epsilon = min(0.1,current_epsilon-0.1)
            
            if [current_row_index, current_column_index] in shortest_path:
                stuck_count = stuck_count+1
                
                if stuck_count > stuck_ok:
                    got_stuck = True
                
            shortest_path.append([current_row_index, current_column_index])
            counter = counter+1
            
        print(f"Path found in {counter} steps")
        
        return shortest_path