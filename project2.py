import pandas as pd
import math

data = pd.read_csv('smaller.txt', header = None, delim_whitespace=True)
df = pd.DataFrame(data)
number_correctly_classified = 0
y = len(df[1])

dataLength = len(df[1]) #How many rows there are? 

current_set_of_features = []

best_so_far_accuracy = 0


def leave_one_out_cross_validation(data, current_set, feature_to_add):
    number_correctly_classified = 0
    for i in range(y):
    #object_to_classify = df2.iloc[i]
        object_to_classify = 0
        label_object_to_classify = df[0].values[i]

        nearest_neighbor_distance = math.inf
        nearest_neighbor_location = math.inf
        nearest_neighbor_label = 0
        for k in range(y):
        #print("Ask if " + str(i) + " is nearest neighbors with " + str(k))
            if k != i:
                distance = 0
                for index, row in df.iterrows():
                    distance = math.sqrt(sum((row[0] - row[1:k])**2))
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = df[0].values[nearest_neighbor_location]
           
    #print("Object " + str(i) + " is class " + str(label_object_to_classify))    
        if (label_object_to_classify == nearest_neighbor_label):
            number_correctly_classified += 1

    accuracy = number_correctly_classified/y 
    return accuracy 


for i in range(10):
    print("On the " + str(i) + "th level of the search tree")
    feature_to_add_at_this_level = 0
    for k in range(len(df.columns)- 1):
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











