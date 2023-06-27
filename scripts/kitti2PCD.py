import open3d as o3d
import numpy as np
def kitti2PCD(filename):
# read XYZ file
    poses = np.loadtxt("/EXTERNAL/datasets/SLAM2023/output/"+filename+".txt")
    xyz=poses[:,[3,7,11]]
    xyz[:,2]=0
    #pcd_ = o3d.io.read_point_cloud("input.xyz")
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    # save as PCD file
    o3d.io.write_point_cloud("/EXTERNAL/datasets/SLAM2023/output/"+filename+"_zeroz.pcd", pcd)

#kitti2PCD("path_XA_202210131557_92f301c_2023_06_21_17_29_trans")
kitti2PCD("path_XA_202210131557_92f301c_2023_06_21_17_29_trans")
#kitti2PCD("path_XA_202210131557_92f301c_2023_06_21_17_29_trans")
#kitti2PCD("path_XA_202210131557_92f301c_2023_06_21_17_29_trans")