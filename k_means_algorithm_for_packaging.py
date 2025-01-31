# -*- coding: utf-8 -*-
"""K means algorithm for packaging

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B_fK28pKt3o8aBK1f_14-jHq3zQj0Cpj
"""

import numpy as np
import pandas as pd
import random
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.metrics import pairwise_distances

data = pd.read_excel("/content/Analisis avanzado empaques (1).xlsx")

data_2 =pd.DataFrame(data['Etiqueta']).dropna()

random.seed(119)

random.seed(119)
inertia_values = []
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(data_2)
    inertia_values.append(kmeans.inertia_)

# Plot the elbow curve
plt.plot(range(1, 10), inertia_values, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()

random.seed(119)

kmeans = KMeans(n_clusters=3, init='k-means++')

kmeans.fit(data_2)

centroids = kmeans.cluster_centers_

labels = kmeans.labels_

data_2['Cluster'] = labels

print(data_2)

centroids

#The silhouette score measures how similar a data point is to its own cluster compared to other clusters. It ranges from -1 to 1.
#A score closer to 1 indicates that the points are well-clustered.
random.seed(119)

score = silhouette_score(data_2, kmeans.labels_)
print(f"Silhouette Score: {score}")

#The distance between the centroids of different clusters. Greater separation between clusters indicates better-defined clusters.
#Larger distances between cluster centroids suggest that the clusters are distinct and well-separated.
random.seed(119)

inter_cluster_distances = pairwise_distances(centroids)
between_cluster_variance = np.mean(inter_cluster_distances**2)

print(between_cluster_variance)

random.seed(119)

unique, counts = np.unique(kmeans.labels_, return_counts=True)
cluster_sizes = dict(zip(unique, counts))
print(f"Cluster Sizes: {cluster_sizes}")