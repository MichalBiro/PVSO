import numpy as np
import open3d as o3d
from sklearn.cluster import Birch

# Loading point cloud data
pcd = o3d.io.read_point_cloud("pcds/our_RADIUS_outlier.ply")
o3d.visualization.draw_geometries([pcd])

# Converting point cloud to numpy array
points = np.asarray(pcd.points)

# Creating BIRCH model
birch = Birch(n_clusters=5)

# Training the BIRCH algorithm
birch.fit(points)

# Setting labels
labels = birch.labels_

# Setting the label colors
colors = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [1, 0, 1]]  # blue, green, red, cyan, magenta
pcd_colors = np.zeros_like(points)
for i in range(len(labels)):
   pcd_colors[i] = colors[labels[i] % len(colors)]

# Assigning the cluster colors to the point cloud
pcd.colors = o3d.utility.Vector3dVector(pcd_colors)

# Saving the new ply file
o3d.io.write_point_cloud("pcds/our_BIRCH.ply", pcd, write_ascii=True)

# Visualizing the point cloud with colors representing the clusters
o3d.visualization.draw_geometries([pcd])