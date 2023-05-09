import open3d as o3d

# Loading point cloud data
pcd = o3d.io.read_point_cloud("pcds/our_sample.ply")
o3d.visualization.draw_geometries([pcd])

voxel_down_pcd = pcd.voxel_down_sample(voxel_size=0.01)

#cl, ind = voxel_down_pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio= 1.5)
cl, ind = voxel_down_pcd.remove_radius_outlier(nb_points=25, radius=0.05)

inlier_cloud = voxel_down_pcd.select_by_index(ind)
outlier_cloud = voxel_down_pcd.select_by_index(ind, invert=True)

#inlier_cloud.paint_uniform_color([0.6, 0.6, 0.6])
#outlier_cloud.paint_uniform_color([1, 0, 0])

# Saving the new ply file
o3d.io.write_point_cloud("pcds/our_RADIUS_outlier.ply", inlier_cloud, write_ascii=True)

# Visualizing the new point cloud
o3d.visualization.draw_geometries([inlier_cloud])