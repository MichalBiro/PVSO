import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

# Loading point cloud data
pcd = o3d.io.read_point_cloud("pcds/our_sample.ply")
o3d.visualization.draw_geometries([pcd])

# Segmenting and labeling data
labels = np.array(pcd.cluster_dbscan(eps=0.05, min_points=10))
max_label = labels.max()

# Setting the label colors - based on normalised values
colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
colors[labels < 0] = 0

# Assigning the cluster colors to the point cloud
pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])

# Saving the new ply file
o3d.io.write_point_cloud("pcds/our_DBSCAN.ply", pcd, write_ascii=True)

# Visualizing the point cloud with colors representing the clusters
o3d.visualization.draw_geometries([pcd])