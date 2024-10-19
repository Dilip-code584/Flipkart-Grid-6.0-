import open3d as o3d
import numpy as np
import cv2

def convert_to_point_cloud(image_path):
    # Load the image (assuming it's a depth map for simplicity)
    depth_image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    # Ensure the image is loaded correctly
    if depth_image is None:
        raise ValueError("Image not loaded correctly.")
    
    # Ensure image is in grayscale (depth maps typically are)
    if len(depth_image.shape) != 2:
        raise ValueError("Expected a single-channel (grayscale) depth image.")
    
    # Parameters for depth scaling
    fx = 1.0  # Focal length in terms of pixel dimensions, can vary depending on your camera
    fy = 1.0  # Focal length in terms of pixel dimensions, can vary depending on your camera
    cx = depth_image.shape[1] // 2  # Principal point (usually center of the image)
    cy = depth_image.shape[0] // 2  # Principal point (usually center of the image)
    
    # Create a point cloud
    points = []
    for v in range(depth_image.shape[0]):
        for u in range(depth_image.shape[1]):
            z = depth_image[v, u]
            if z == 0:
                continue
            x = (u - cx) * z / fx
            y = (v - cy) * z / fy
            points.append([x, y, z])
    
    # Convert to Open3D PointCloud
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np.array(points))
    
    return pcd

def reconstruct_3d(images):
    pcd = o3d.geometry.PointCloud()
    for image_path in images:
        new_pcd = convert_to_point_cloud(image_path)
        pcd += new_pcd
    o3d.visualization.draw_geometries([pcd])

if __name__ == "__main__":
    # Sample images list, assuming they are depth maps or stereo images
    images = ['image1.jpg', 'image2.jpg', 'image3.jpg']
    reconstruct_3d(images)

