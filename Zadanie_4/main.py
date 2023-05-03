import numpy as np
import open3d as o3d


pts = o3d.io.read_point_cloud("output.pcd")
#pts = o3d.io.read_point_cloud("room.ply")
#o3d.io.write_point_cloud("myply.ply", pts, write_ascii=True)


pcd = o3d.io.read_point_cloud('myply.ply')
# visualize
o3d.visualization.draw_geometries([pts])

# #----- RANSAC -----
# #https://towardsdatascience.com/how-to-automate-3d-point-cloud-segmentation-and-clustering-with-python-343c9039e4f5
# #
#
# plane_model, inliers = pts.segment_plane(distance_threshold=0.1, ransac_n=5, num_iterations=2000)
#
# inlier_cloud = pts.select_by_index(inliers)
# outlier_cloud = pts.select_by_index(inliers, invert=True)
# o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])



