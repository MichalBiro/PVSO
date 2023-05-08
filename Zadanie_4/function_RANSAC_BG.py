import numpy as np
import open3d as o3d
from sklearn.cluster import Birch
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# pcd = o3d.io.read_point_cloud("rainbow_room.ply")
# o3d.visualization.draw_geometries([pcd])

# ------------------------------

# iteration = 0
#
# for x in range(3):
#
#     if iteration == 0:
#         plane_model, inliers = pcd.segment_plane(distance_threshold=0.08, ransac_n=5, num_iterations=1000)
#
#         inlier_cloud = pcd.select_by_index(inliers)
#         outlier_cloud = pcd.select_by_index(inliers, invert=True)
#
#         # ------------------------------
#
#         new_pcd = inlier_cloud
#         iteration = 1
#
#     else:
#         plane_model, inliers = outlier_cloud.segment_plane(distance_threshold=0.08, ransac_n=5, num_iterations=1000)
#
#         inlier_cloud = outlier_cloud.select_by_index(inliers)
#         outlier_cloud = outlier_cloud.select_by_index(inliers, invert=True)
#
#         # ------------------------------
#
#         next_pcd = inlier_cloud
#
#         p1_load = np.asarray(new_pcd.points)
#         p1_color = np.asarray(new_pcd.colors)
#
#         p2_load = np.asarray(next_pcd.points)
#         p2_color = np.asarray(next_pcd.colors)
#
#         p3_load = np.concatenate((p1_load, p2_load), axis=0)
#         p3_color = np.concatenate((p1_color, p2_color), axis=0)
#
#         new_pcd = o3d.geometry.PointCloud()
#
#         new_pcd.points = o3d.utility.Vector3dVector(p3_load)
#         new_pcd.colors = o3d.utility.Vector3dVector(p3_color)
#
#     #o3d.visualization.draw_geometries([new_pcd])
#     o3d.io.write_point_cloud("rainbow_RANSAC.ply", new_pcd, write_ascii=True)

# voxel_down_pcd = pcd.voxel_down_sample(voxel_size=0.01)
#
# #cl, ind = voxel_down_pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio= 1.5)
# cl, ind = voxel_down_pcd.remove_radius_outlier(nb_points=25, radius=0.05)
#
# inlier_cloud = voxel_down_pcd.select_by_index(ind)
# outlier_cloud = voxel_down_pcd.select_by_index(ind, invert=True)
#
# #inlier_cloud.paint_uniform_color([0.6, 0.6, 0.6])
# #outlier_cloud.paint_uniform_color([1, 0, 0])
#
# o3d.visualization.draw_geometries([inlier_cloud,outlier_cloud])
#
# o3d.io.write_point_cloud("rainbow_RADIUS_outlier.ply", inlier_cloud, write_ascii=True)

# ----------------------------------------------------------------------------------------

# Load point cloud data
pcd = o3d.io.read_point_cloud("our_RADIUS_outlier.ply")


# Convert point cloud to numpy array
points = np.asarray(pcd.points)


# vytvorenie BIRCH model s počtom klastrov = 5
birch = Birch(n_clusters=4)


#BIRCH algoritmus trénuje na základe vstupných dát (points)
birch.fit(points)


# priraduje do ktorého klastra patrí
labels = birch.labels_


# priradenie mu farby podla príslušného klastra
colors = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1]]#, [1, 0, 1]]  # blue, green, red, cyan, magenta
pcd_colors = np.zeros_like(points)
for i in range(len(labels)):
   pcd_colors[i] = colors[labels[i] % len(colors)]


# Assign the cluster labels to the point cloud
#ytvára nový vektor farieb "pcd_colors", ktorý má rovnaký počet prvkov ako vektor bodov pcd.points
#farby sa priraduju podla zhluku doktoreho patria
pcd.colors = o3d.utility.Vector3dVector(pcd_colors)

o3d.io.write_point_cloud("our_BIRCH.ply", pcd, write_ascii=True)

# Visualize the point cloud with colors representing the clusters
o3d.visualization.draw_geometries([pcd])

# ----------------------------------------------------------------------------------------

# Load point cloud data
pcd = o3d.io.read_point_cloud("TLS_kitchen_sample.ply")
o3d.visualization.draw_geometries([pcd])
#aplikacia DBSCAN algoritmu pomocou funkcie pcd.cluster_dbscan s 2ma parametrami epsilon a minpocet bodov v klastri
#labels je vysledok dbscan alg - obsahuje označenie každého bodu podľa toho, do ktoreho klastra patrí
labels = np.array(pcd.cluster_dbscan(eps=0.05, min_points=10))
#vracia najvacsi priradeni klaster
max_label = labels.max()


#Používa sa funkcia plt.get_cmap, ktorá priradí každému klasteru inú farbu z farebného spektra "tab20".
# Tieto farby sa potom priradia k bodom pomocou vektoru farieb colors.
colors = plt.get_cmap("tab20")(labels / (max_label  #tab20 je farebna mapa
if max_label > 0 else 1))  #potrebujeme rozsah 0-1 aby to fungovalo v pripade 1 klustera
#normalizovana hodnota sa pouziva na generovanie unikatnej farby pre kazdy kluster
colors[labels < 0] = 0


#pcd.colors, ktorá je typu Vector3dVector. Táto premenná sa potom použije na vizualizáciu
pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])

o3d.io.write_point_cloud("TLS_kitchen_sample_DBSCAN.ply", pcd, write_ascii=True)

#vizualizacia
o3d.visualization.draw_geometries([pcd])
