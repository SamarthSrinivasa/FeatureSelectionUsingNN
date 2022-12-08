import pandas as pd
import random

data = pd.read_csv('CS170_Small_Data__123.txt', header = None, delim_whitespace=True)
df = pd.DataFrame(data)

dataLength = len(df[1]) #How many rows there are? 


def leave_one_out_cross_validation(data, current_set, feature_to_add):

    accuracy = random.randint(0, 100000)
    return accuracy 

current_set_of_features = []

best_so_far_accuracy = 0

for i in range(20):
    print("On the " + str(i) + "th level of the search tree")
    feature_to_add_at_this_level = 0
    for k in range(len(df.columns)- 1):
        if k not in current_set_of_features:
            print("--Considering adding the " + str(k) + " feature")
            accuracy = leave_one_out_cross_validation(data, current_set_of_features, k+1)
        
            if accuracy > best_so_far_accuracy:
                best_so_far_accuracy = accuracy
                feature_to_add_at_this_level = k
            print(best_so_far_accuracy) 
            print(current_set_of_features)           

    #current_set_of_features[i] = feature_to_add_at_this_level
    if feature_to_add_at_this_level != 0:
        current_set_of_features.append(feature_to_add_at_this_level)
    print("On level " + str(i) + " I added feature " + str(feature_to_add_at_this_level) + " to current set")    



