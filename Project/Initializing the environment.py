 #initializing the environment
def __init__(self, config):        
    self.environment_rows = config['height']
    self.environment_columns = config['width'] 
    #initializing qValues
    #our goal is to learn this values from many experimental runs
    self.q_values = np.zeros((self.environment_rows, self.environment_columns, 4))
    #set of possible actions
    self.actions = ['up', 'right', 'down', 'left']
    #rewards matrix(set to -1 at start)
    self.rewards = np.full((self.environment_rows, self.environment_columns), -1)
    #initializing ultraSoftObstacle with ultraSoftWeights
    for i in config["ultraSoftObstacles"]:
        self.rewards[i["topLeft"][0]:i["bottomRight"][0]+1, i["topLeft"][1]:i["bottomRight"][1]+1] = config["ultraSoftWeight"]
    #initializing semiSoftObstacle with semiSoftWeights
    for i in config["semiSoftObstacles"]:
        self.rewards[i["topLeft"][0]:i["bottomRight"][0]+1, i["topLeft"][1]:i["bottomRight"][1]+1] = config["semiSoftWeight"]
    #initializing softObstacle with softWeights
    for i in config["softObstacles"]:
        self.rewards[i["topLeft"][0]:i["bottomRight"][0]+1, i["topLeft"][1]:i["bottomRight"][1]+1] = config["softWeight"]
    #initializing hardObstacles with hardWeights
    for i in config["hardObstacles"]:
        self.rewards[i["topLeft"][0]:i["bottomRight"][0]+1, i["topLeft"][1]:i["bottomRight"][1]+1] = config["hardWeight"]  
    #will raise an error if startpoint is on hard obstacle
    assert self.rewards[config["startLoc"][0],config["startLoc"][1]] != config["hardWeight"], "Start point cannot be inside hard obstacles!"