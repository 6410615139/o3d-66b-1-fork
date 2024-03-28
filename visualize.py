import open3d as o3d

# Load a point cloud file
# Replace 'point_cloud.ply' with the path to your point cloud file
point_cloud = o3d.io.read_point_cloud("data/kota-3.ply")

# Visualize the point cloud
o3d.visualization.draw_geometries([point_cloud])
