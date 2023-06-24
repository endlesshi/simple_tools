import numpy as np


def trans(filename):
    # 读取pose.txt文件
    pose_file = filename+'.txt'
    poses = np.loadtxt(pose_file)

    # 变换矩阵绕x轴转180度，再绕z轴转90度
    R = np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])
    poses_new = np.zeros_like(poses)
    for i in range(len(poses)):
        pose = poses[i].reshape(3, 4)
        pose_new = np.hstack([R.dot(pose[:, :3].T).T, R.dot(pose[:, 3].reshape(3, 1))])
        poses_new[i] = pose_new.reshape(-1)

    # 保存变换矩阵到新的pose_new.txt文件
    pose_new_file = filename+'_trans.txt'
    np.savetxt(pose_new_file, poses_new, fmt='%.6f')


trans("/EXTERNAL/datasets/SLAM2023/output/path_XA_202210131557_92f301c_2023_06_21_17_29")
# trans("/EXTERNAL/datasets/SLAM2023/output/path_dlo_202306241228")
# trans("/EXTERNAL/datasets/SLAM2023/output/path_XA_202210131557_92f301c_2023_06_21_17_29")
# trans("/EXTERNAL/datasets/SLAM2023/output/path_XA_202210131557_92f301c_2023_06_21_17_29")
# trans("/EXTERNAL/datasets/SLAM2023/output/path_XA_202210131557_92f301c_2023_06_21_17_29")
# trans("/EXTERNAL/datasets/SLAM2023/output/path_XA_202210131557_92f301c_2023_06_21_17_29")
# trans("/EXTERNAL/datasets/SLAM2023/output/path_XA_202210131557_92f301c_2023_06_21_17_29")