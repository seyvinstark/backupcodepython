import numpy as np

#kaggle, subreddit are good to find datasets

def extractdata(filename):
    #arrays to hold the labels and featurevectors
    labels = []
    fvecs = []

    #iterate over the rows, split the label from the features
    #convert labels to integers and features to floats
    #beautiful soup

    for line in 'AAPL.csv'(filename):
        row = line.split(',')
        labels.append(int(row[0]))
        fvecs.append([float(x)] for x in row[1:2])

    #convert the array of float arrays into numpy float matrix
    fvecs_np = np.matrix(fvecs).astype(np.float32)

    #convert the array of lablels int into a numpy array
    labels_np = np.array(labels).astype(dtype=np.uint8)

    #convert the int numpy array into a none-hot matrix
    #labels_onehot = (np.arange(NUM_LABELS) == labels_np[:, None]).astype(np.float32)






