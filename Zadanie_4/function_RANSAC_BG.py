import numpy as np
import open3d as o3d

pcd = o3d.io.read_point_cloud("conv_biro.ply")
o3d.visualization.draw_geometries([pcd])

# ------------------------------

iteration = 0

for x in range(3):

    if iteration == 0:
        plane_model, inliers = pcd.segment_plane(distance_threshold=0.08, ransac_n=5, num_iterations=1000)

        inlier_cloud = pcd.select_by_index(inliers)
        outlier_cloud = pcd.select_by_index(inliers, invert=True)

        # ------------------------------

        new_pcd = inlier_cloud
        iteration = 1

    else:
        plane_model, inliers = outlier_cloud.segment_plane(distance_threshold=0.08, ransac_n=5, num_iterations=1000)

        inlier_cloud = outlier_cloud.select_by_index(inliers)
        outlier_cloud = outlier_cloud.select_by_index(inliers, invert=True)

        # ------------------------------

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

    o3d.visualization.draw_geometries([new_pcd])