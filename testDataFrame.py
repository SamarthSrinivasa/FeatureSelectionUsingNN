import math 
import random
import numpy as np


data1 = []
with open("CS170_Small_Data__123.txt", "r") as file:
    for line in file:
        data1.append(line.split())

data2 = np.array(data1)
data = data2.astype(float)
#data = data1.astype(np.float)

columnLength = len(data)
rowLength = len(data[0])

current_set_of_features = []
best_set = [1,2,3,4,5,6,23,423,4]

best_set = np.square(best_set)
distance = np.sqrt(sum((best_set)))

print(distance)