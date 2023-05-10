import numpy as np
import open3d as o3d

# Loading point cloud data
pcd = o3d.io.read_point_cloud("pcds/our_sample.ply")
o3d.visualization.draw_geometries([pcd])

# ------------------------------

# Iterating through the ply file, searching for planes
iteration = 0
for x in range(3):

    if iteration == 0:
        # Using the BIRCH algorithm to find planes in the point cloud
        plane_model, inliers = pcd.segment_plane(distance_threshold=0.08, ransac_n=5, num_iterations=1000)

        inlier_cloud = pcd.select_by_index(inliers)
        outlier_cloud = pcd.select_by_index(inliers, invert=True)

        # ------------------------------

        # In case of the first plane found adding it to the new point cloud with corresponding coloring
        new_pcd = inlier_cloud
        iteration = 1
    else:
        # Using the BIRCH algorithm to find planes in the point cloud
        plane_model, inliers = outlier_cloud.segment_plane(distance_threshold=0.08, ransac_n=5, num_iterations=1000)

        inlier_cloud = outlier_cloud.select_by_index(inliers)
        outlier_cloud = outlier_cloud.select_by_index(inliers, invert=True)

        # ------------------------------

        # In case of new plane found adding it to the new point cloud with corresponding coloring
        next_pcd = inlier_cloud

        p1_load = np.asarray(new_pcd.points)
        p1_color = np.asarray(new_pcd.colors)

        p2_load = np.asarray(next_pcd.points)
        p2_color = np.asarray(next_pcd.colors)

        p3_load = np.concatenate((p1_load, p2_load), axis=0)
        p3_color = np.concatenate((p1_color, p2_color), axis=0)

        new_pcd = o3d.geometry.PointCloud()

        new_pcd.points = o3d.utility.Vector3dVector(p3_load)
        new_pcd.colors = o3d.utility.Vector3dVector(p3_color)

# Saving the new ply file
o3d.io.write_point_cloud("pcds/our_RANSAC.ply", new_pcd, write_ascii=True)

# Visualizing the new point cloud
o3d.visualization.draw_geometries([new_pcd])