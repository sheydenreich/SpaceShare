from scipy.cluster.vq import kmeans2
import numpy as np
import matplotlib.pyplot as plt
from reader import read_google_sheet

df = read_google_sheet()


def optimize(df): 
    """ 
    This function uses a kmeans clustering algorithm to group participants into shared rides based on airport arrival
    or departures times. 
    
    ----- INPUT ------
    Takes a pandas dataframe as its argument
    
    ----- OUTPUT ----- 
    It returns a pandas dataframe with a new coloumn indicating the ride groups
    """

# Get the preferred departure times from the dataframe
#times = df['Preferred_departure_time'] 
times = np.array([1.30, 1.15, 3.45, 5.00, 10, 12, 2, 2.30, 2, 2.05])
features = np.reshape(times, (-1,1)) # appropriate dimensions for kmeans

# Turn the 1d times into 2d features (requred by scipy) by adding a column of zeros
#features = np.vstack((times, np.zeros(np.size(times))))
#input_data = whiten(features) # whiten rescales the data by it's variance, I don't think that's useful for this project.

ngroups = int(len(times)/3)
centroids, labels = kmeans2(features, k = ngroups)

# get the number of persons in each group:
counts = np.bincount(labels)

colors = ['red', 'blue', 'black', 'green', 'orange']

plt.figure()
#plt.plot(features[:, 0], features[:, 1], '*')
#plt.plot(codebook[:, 0], codebook[:, 1], 'x')
for i in range(ngroups):
    plt.plot(features[labels == i], 'o', color = colors[i])
    plt.plot(centroids[i], 'x', color = colors[i])
plt.show()