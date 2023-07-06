import numpy as np

def random_centroids(img_1d, k_clusters):
    centroids = [img_1d[np.random.randint(0, img_1d.shape[0])] for _ in range(k_clusters)]
    return centroids if len(np.unique(centroids, axis=0)) == len(centroids) else random_centroids(img_1d, k_clusters)
    

def kmeans(img_1d, k_clusters, max_iter, init_centroids):
    '''
        K-Means algorithm
        
        Inputs:
            img_1d : np.ndarray with shape=(height * width, num_channels)
                Original image in 1d array
            
            k_clusters : int
                Number of clusters
                
            max_iter : int
                Max iterator
                
            init_cluster : str
                The way which use to init centroids
                'random' --> centroid has `c` channels, with `c` is initial random in [0,255]
                'in_pixels' --> centroid is a random pixels of original image
                
        Outputs:
            centroids : np.ndarray with shape=(k_clusters, num_channels)
                Store color centroids
                
            labels : np.ndarray with shape=(height * width, )
                Store label for pixels (cluster's index on which the pixel belongs)
    '''
    centroids = []
    
    # if init_centroids = 'random' then random k_clusters centroids with c channels
    # else if init_centroids = 'in_pixels' then random k_clusters pixels of original image
    
    # Random value must be unique, which means that each centroid must be different (mask array)
    # else raise error
    
    labels = []
    return centroids, labels

print(np.random.randint(0, 256, (3, 3)))