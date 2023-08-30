#configuration parameters
#startLoc should be changed from here
scale = 1
config = {
    "height": 32*scale,
    "width": 32*scale,
    "startLoc": [11*scale, 4*scale],
    "endLoc": [25*scale, 28*scale],
    #if you want to add new obstacles,then just add another topLeft and bottomRight corner dictionary to list
    #weight for the semi soft obstacle
    "ultraSoftWeight": -50*scale,
    "ultraSoftObstacles": [
        {"topLeft": [7*scale, 5*scale], "bottomRight": [12*scale, 10*scale]},
        {"topLeft": [13*scale, 6*scale], "bottomRight": [14*scale, 9*scale]},
        {"topLeft": [15*scale, 9*scale], "bottomRight": [16*scale, 11*scale]},
        {"topLeft": [8*scale, 11*scale], "bottomRight": [10*scale, 12*scale]},
        {"topLeft": [17*scale, 9*scale], "bottomRight": [18*scale, 17*scale]},
        {"topLeft": [10*scale, 13*scale], "bottomRight": [12*scale, 14*scale]},
        {"topLeft": [12*scale, 14*scale], "bottomRight": [16*scale, 17*scale]},    ],
    #weight for the semi soft obstacle 
    "semiSoftWeight": -390*scale,
    "semiSoftObstacles": [
        {"topLeft": [8*scale, 6*scale], "bottomRight": [11*scale, 9*scale]},
        {"topLeft": [12*scale, 7*scale], "bottomRight": [13*scale, 10*scale]},
        {"topLeft": [9*scale, 10*scale], "bottomRight": [10*scale, 11*scale]},
        {"topLeft": [14*scale, 10*scale], "bottomRight": [15*scale, 11*scale]},
        {"topLeft": [16*scale, 12*scale], "bottomRight": [17*scale, 16*scale]},
        {"topLeft": [11*scale, 12*scale], "bottomRight": [12*scale, 13*scale]},
        {"topLeft": [13*scale, 14*scale], "bottomRight": [15*scale, 16*scale]},
        
        {"topLeft": [11*scale, 25*scale], "bottomRight": [15*scale, 27*scale]},
        {"topLeft": [12*scale, 23*scale], "bottomRight": [19*scale, 25*scale]},
        {"topLeft": [13*scale, 21*scale], "bottomRight": [24*scale, 24*scale]},
        {"topLeft": [18*scale, 20*scale], "bottomRight": [24*scale, 21*scale]},
        {"topLeft": [20*scale, 18*scale], "bottomRight": [24*scale, 19*scale]},
    ],
    "softObstacles": [
        {"topLeft": [9*scale, 7*scale], "bottomRight": [10*scale, 9*scale]},
        {"topLeft": [11*scale, 8*scale], "bottomRight": [12*scale, 9*scale]}, 
        {"topLeft": [12*scale, 9*scale], "bottomRight": [13*scale,10*scale]},
        {"topLeft": [10*scale, 10*scale], "bottomRight": [11*scale, 11*scale]},
        {"topLeft": [11*scale, 11*scale], "bottomRight": [14*scale, 12*scale]},
        {"topLeft": [12*scale, 12*scale], "bottomRight": [15*scale, 13*scale]},
        {"topLeft": [13*scale, 13*scale], "bottomRight": [16*scale, 14*scale]},
        {"topLeft": [14*scale, 14*scale], "bottomRight": [16*scale, 15*scale]},
        
        {"topLeft": [12*scale, 25*scale], "bottomRight": [14*scale, 26*scale]},
        {"topLeft": [13*scale, 23*scale], "bottomRight": [14*scale, 24*scale]},
        {"topLeft": [14*scale, 22*scale], "bottomRight": [18*scale, 24*scale]},
        {"topLeft": [18*scale, 21*scale], "bottomRight": [23*scale, 23*scale]},
        {"topLeft": [21*scale, 19*scale], "bottomRight": [23*scale, 20*scale]},
    ],
    #weight for the soft obstacle
    "softWeight": -550*scale,
    "hardObstacles": [
        {"topLeft": [9*scale, 8*scale], "bottomRight": [10*scale, 9*scale]},
        
        {"topLeft": [11*scale, 9*scale], "bottomRight": [12*scale, 10*scale]},
        {"topLeft": [12*scale, 11*scale], "bottomRight": [13*scale, 12*scale]},
        
        {"topLeft": [13*scale, 12*scale], "bottomRight": [14*scale, 13*scale]},
        
        {"topLeft": [15*scale, 13*scale], "bottomRight": [16*scale, 14*scale]},
        {"topLeft": [13*scale, 25*scale], "bottomRight": [14*scale, 26*scale]}, 
        
        {"topLeft": [14*scale, 23*scale], "bottomRight": [15*scale, 24*scale]},
        {"topLeft": [14*scale, 23*scale], "bottomRight": [17*scale, 24*scale]},
        
        {"topLeft": [18*scale, 22*scale], "bottomRight": [19*scale, 23*scale]},
        {"topLeft": [19*scale, 22*scale], "bottomRight": [22*scale, 23*scale]},
        
        {"topLeft": [22*scale, 20*scale], "bottomRight": [23*scale, 22*scale]},
#         {"topLeft": [15, 24], "bottomRight": [14, 25]}
        
    ],
    #weight for the hard obstacle
    "hardWeight": -1000*scale,
    "reward": 1000000       
}