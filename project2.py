import math
import random
import numpy as np

# data = pd.read_csv('smaller.txt', header = None, delim_whitespace=True)
# df = pd.DataFrame(data)
# df2 = df.iloc[: , 1:]
# y = len(df[1])
# x = len(df2.columns)

data1 = []
with open("smaller.txt", "r") as file:
    for line in file:
        data1.append(line.split())

data2 = np.array(data1)
data = data2.astype(float)
#data = data1.astype(np.float)

columnLength = len(data)
rowLength = len(data[0])

current_set_of_features = []


def leave_one_out_cross_validation(data, current_set, feature_to_add):
    number_correctly_classified = 0
    for i in range(columnLength):
    #object_to_classify = df2.iloc[i]
        object_to_classify = 0
        label_object_to_classify = data[i][0]
        #print(label_object_to_classify)

        nearest_neighbor_distance = math.inf
        nearest_neighbor_location = math.inf
        nearest_neighbor_label = 0
        for k in range(columnLength):
        #print("Ask if " + str(i) + " is nearest neighbors with " + str(k))
            if k != i:
                distance = math.sqrt(sum((data[i][1:] - data[k][1:])**2))
                    #print(distance)
                if distance <= nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = data[nearest_neighbor_location][0]
                    #print(nearest_neighbor_label)
           
    #print("Object " + str(i) + " is class " + str(label_object_to_classify))    
        if (label_object_to_classify == nearest_neighbor_label):
            number_correctly_classified += 1

    accuracy = number_correctly_classified/columnLength 
    #print(y)
    return accuracy 


for i in range(columnLength):
    print("On the " + str(i) + "th level of the search tree")
    feature_to_add_at_this_level = 0
    for k in range(rowLength - 1):
        if k not in current_set_of_features:
            print("--Considering adding the " + str(k) + " feature")
            accuracy = leave_one_out_cross_validation(data, current_set_of_features, k+1)
            
            if accuracy >= best_so_far_accuracy:
                best_so_far_accuracy = accuracy
                feature_to_add_at_this_level = k
            print(best_so_far_accuracy) 
            print(current_set_of_features)           

    #current_set_of_features[i] = feature_to_add_at_this_level
    if feature_to_add_at_this_level != 0:
        current_set_of_features.append(feature_to_add_at_this_level)
    print("On level " + str(i) + " I added feature " + str(feature_to_add_at_this_level) + " to current set")    



