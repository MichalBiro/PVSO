import open3d as o3d
from enum import Enum


# Defining switch statement for python for our specific use
def switch(room):
    if room == 1:
        # Loading point cloud and visualising it
        pcd = o3d.io.read_point_cloud("pcds/our_sample.ply")
        o3d.visualization.draw_geometries([pcd])

        # Loading RANSAC pcd data and visualising it
        ransac_pcd = o3d.io.read_point_cloud("pcds/our_RANSAC.ply")
        o3d.visualization.draw_geometries([ransac_pcd])

        # Loading radius outlier pcd data and visualising it
        radius_pcd = o3d.io.read_point_cloud('pcds/our_RADIUS_outlier.ply')
        o3d.visualization.draw_geometries([radius_pcd])

        # Loading BIRCH algorithm pcd data and visualising it
        birch_pcd = o3d.io.read_point_cloud("pcds/our_BIRCH.ply")
        o3d.visualization.draw_geometries([birch_pcd])

        # Loading DBSCAN algorithm pcd data and visualising it
        dbscan_pcd = o3d.io.read_point_cloud("pcds/our_DBSCAN.ply")
        o3d.visualization.draw_geometries([dbscan_pcd])
        return
    elif room == 2:
        # Loading point cloud and visualising it
        pcd = o3d.io.read_point_cloud("pcds/room.ply")
        o3d.visualization.draw_geometries([pcd])

        # Loading RANSAC pcd data and visualising it
        ransac_pcd = o3d.io.read_point_cloud("pcds/room_RANSAC.ply")
        o3d.visualization.draw_geometries([ransac_pcd])

        # Loading radius outlier pcd data and visualising it
        radius_pcd = o3d.io.read_point_cloud("pcds/room_RADIUS_outlier.ply")
        o3d.visualization.draw_geometries([radius_pcd])

        # Loading BIRCH algorithm pcd data and visualising it
        birch_pcd = o3d.io.read_point_cloud("pcds/room_BIRCH.ply")
        o3d.visualization.draw_geometries([birch_pcd])

        # Loading DBSCAN algorithm pcd data and visualising it
        dbscan_pcd = o3d.io.read_point_cloud("pcds/room_DBSCAN.ply")
        o3d.visualization.draw_geometries([dbscan_pcd])
        return
    elif room == 3:
        # Loading point cloud and visualising it
        pcd = o3d.io.read_point_cloud("pcds/rainbow_room.ply")
        o3d.visualization.draw_geometries([pcd])

        # Loading RANSAC pcd data and visualising it
        ransac_pcd = o3d.io.read_point_cloud("pcds/rainbow_RANSAC.ply")
        o3d.visualization.draw_geometries([ransac_pcd])

        # Loading radius outlier pcd data and visualising it
        radius_pcd = o3d.io.read_point_cloud("pcds/rainbow_RADIUS_outlier.ply")
        o3d.visualization.draw_geometries([radius_pcd])

        # Loading BIRCH algorithm pcd data and visualising it
        birch_pcd = o3d.io.read_point_cloud("pcds/rainbow_BIRCH.ply")
        o3d.visualization.draw_geometries([birch_pcd])

        # Loading DBSCAN algorithm pcd data and visualising it
        dbscan_pcd = o3d.io.read_point_cloud("pcds/rainbow_DBSCAN.ply")
        o3d.visualization.draw_geometries([dbscan_pcd])
        return
    elif room == 4:
        # Loading point cloud and visualising it
        pcd = o3d.io.read_point_cloud("pcds/TLS_kitchen.ply")
        o3d.visualization.draw_geometries([pcd])

        # Loading DBSCAN algorithm pcd data and visualising it
        dbscan_pcd = o3d.io.read_point_cloud("pcds/TLS_kitchen_DBSCAN.ply")
        o3d.visualization.draw_geometries([dbscan_pcd])
        return
    elif room == 5:
        # Loading point cloud and visualising it
        pcd = o3d.io.read_point_cloud("pcds/TLS_kitchen_sample.ply")
        o3d.visualization.draw_geometries([pcd])

        # Loading DBSCAN algorithm pcd data and visualising it
        dbscan_pcd = o3d.io.read_point_cloud("pcds/TLS_kitchen_sample_DBSCAN.ply")
        o3d.visualization.draw_geometries([dbscan_pcd])
        return


OUR = 1  # Our sample
LIVING = 2  # Living room
RAINBOW = 3  # Small room without colors
KITCHEN = 4  # Kitchen sample
KITCHEN_S = 5  # Kitchen sample without walls

# Choosing room to show all available pcd-s for
switch(OUR)

