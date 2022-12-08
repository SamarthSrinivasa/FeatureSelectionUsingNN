import pandas as pd
import math

data = pd.read_csv('smaller.txt', header = None, delim_whitespace=True)
df = pd.DataFrame(data)
df2 = df.iloc[: , 1:]
y = len(df[1])
x = len(df2.columns)

#for row in df.itertuples():
    #print(math.sqrt(sum((row[0] - row[1:6])**2)))
    #print(row[1] - row[2:3])

#for row in df.itertuples():
    #distance = math.sqrt(sum((row[0] - row[1:index])**2))
    #print(distance)

distance = math.sqrt(sum((row[0] - row[1:k])**2))


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