import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, fcluster
from datetime import timedelta

def get_time_of_year(time):
    """
    gives the time as a float in months (from 0 to 12)
    """
    return timedelta(days=time.day, hours=time.hour, minutes=time.minute, seconds=time.second).total_seconds()/3600


def optimize(df, kind="arrival", max_time_difference = 0.5, max_people_per_car = 3): 
    """ 
    This function uses a kmeans clustering algorithm to group participants into shared rides based on airport arrival
    or departures times. 
    
    ----- INPUT ------
    Takes a pandas dataframe as its argument
    
    ----- OUTPUT ----- 
    It returns a pandas dataframe with a new coloumn indicating the ride groups
    """

    assert kind in ["arrival", "departure"], "kind must be either 'arrival' or 'departure'"
    if(kind=="arrival"):
        times = df["date_time_of_airport_arrival"].apply(get_time_of_year)
    else:
        times = df["date_time_of_hotel_departure"].apply(get_time_of_year)

    # Reshape the data to the format needed for the linkage function
    data = np.array(times).reshape(-1, 1)

    # Create a dendrogram using the 'ward' method to minimize variance in each cluster
    Z = linkage(data, 'ward')

    # Set a maximum time difference (let's say 15 minutes) for each group
    clusters = fcluster(Z, max_time_difference, criterion='distance')

    counts = np.bincount(clusters)

    too_many_people = np.where(counts > max_people_per_car)[0]

    for idx in too_many_people:
        # Find the people in the cluster
        people = np.where(clusters == idx)[0]
        # Sort the people by their time
        people = people[np.argsort(times[people])]
        # Split the people into groups of 3
        new_clusters = np.array_split(people, len(people) // 3 + 1)
        for cluster_idx,new_cluster in enumerate(new_clusters[1:]):
            # Update the clusters
            clusters[new_cluster] = clusters.max() + 1
    df[f"{kind}_group"] = clusters
    return df

