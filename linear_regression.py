import numpy as np

import pandas as pd 

import matplotlib.pyplot as plt 


height = np.array([5.9,5.10,5.7,5.8,5.8,5.5,5.1,5.3])

weight = np.array([70,80,65,64,59,78,64,62,61])

m,b = np.polyfit(height,weight,1)

new_height = 6.0

pred_weight = m*new_height +b

print(f"Predicted height : {pred_weight}")
