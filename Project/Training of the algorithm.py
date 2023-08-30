def train(self, epoch,stuck_ok=100):
        #hyperparameters used in Bellman equation for computing Qvalues
        epsilon = 0.01
        discount_factor = 0.99 
        learning_rate = 0.85
        
        maxlen = 500
        stuck = 0
        plots = 0
        stuck_plots = 0
        max_plots = 5

        for episode in range(epoch):
            if episode%500 == 0:
                print(f"Episode {episode}")
            
            stuck_count = 0
            
            this_stuck = False
            
            row_index, column_index = self.get_starting_location()            
                        
            current_path = [[row_index,column_index]]
            
            while not self.is_terminal_state(row_index, column_index) and not this_stuck:
                #while experimental run is not finished,update Qtable according to Bellman equation
                
                old_row_index, old_column_index = row_index, column_index 
                prev = None if len(current_path) < 2 else current_path[-2]
                
                if prev is None:
                
                    action_index = self.get_next_action(row_index, column_index, epsilon)
                    row_index, column_index = self.get_next_location(row_index, column_index, action_index)
            
                else:
                    found_valid = False
                    
                    while not found_valid:
                        
                        action_index = self.get_next_action(old_row_index, old_column_index, epsilon)
                        row_index, column_index = self.get_next_location(old_row_index, old_column_index, action_index)
                        
                        if abs(row_index-prev[0]) > 0 or abs(column_index-prev[1]) > 0:
                            found_valid = True
                
                reward = self.rewards[row_index, column_index]
                old_q_value = self.q_values[old_row_index, old_column_index, action_index]
                temporal_difference = reward + (discount_factor * np.max(self.q_values[row_index, column_index])) - old_q_value

                new_q_value = old_q_value + (learning_rate * temporal_difference)
                self.q_values[old_row_index, old_column_index, action_index] = new_q_value
                
                if [row_index,column_index] in current_path:
                    stuck_count = stuck_count+1
                    
                    if stuck_count > stuck_ok:
                        this_stuck = True
                        stuck = stuck+1
                
                current_path.append([row_index,column_index])
                
                
            if not this_stuck and plots < max_plots:
                plt.figure()
                plt.imshow(obstacles)
                plt.scatter([config["startLoc"][1]],[config["startLoc"][0]])
                plt.scatter([config["endLoc"][1]],[config["endLoc"][0]])
                plt.plot([p[1] for p in current_path],[p[0] for p in current_path],'k')
                plt.scatter([p[1] for p in current_path],[p[0] for p in current_path],c='w')
                plt.scatter(current_path[0][1],current_path[0][0],c='k')
                plt.scatter(current_path[-1][1],current_path[-1][0],c='g')
                plots = plots +1
                #print(current_path)
                
            if this_stuck and stuck_plots < max_plots:
                plt.figure()
                plt.imshow(obstacles)
                plt.scatter([config["startLoc"][1]],[config["startLoc"][0]])
                plt.scatter([config["endLoc"][1]],[config["endLoc"][0]])
                plt.plot([p[1] for p in current_path],[p[0] for p in current_path],'k')
                plt.scatter([p[1] for p in current_path],[p[0] for p in current_path],c='w')
                plt.scatter(current_path[0][1],current_path[0][0],c='k')
                plt.scatter(current_path[-1][1],current_path[-1][0],c='g')
                stuck_plots = stuck_plots +1
                
                    
        print(f"{stuck} stuck episodes.")

#Training outcome: q_values (preferred directions) is populated, to be picked up by get_shortest_path

start_time = time.time()

try:
    short = PathFinder(config)
    #trains for 10000 experimental runs(epochs)
    short.train(10000,stuck_ok=1000)
except AssertionError as e:
    print(e)
    
print(f"Training time: {time.time()-start_time} seconds.")