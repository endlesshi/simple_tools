import numpy as np

# 读取xyzrpy.txt文件并将其存储为numpy数组
arr = np.loadtxt('./dataset/Poses.txt')
print(arr.shape)
pose_array = arr[:, 1:]
print(pose_array.shape)

# 将弧度转换为角度
#pose_array[:, 3:] = np.rad2deg(pose_array[:, 3:])

# 将roll、pitch、yaw转换为旋转矩阵
#rotation_matrices = np.empty((len(pose_array), 3, 3))
with open('./dataset/Poses_KITTI.txt', 'w') as fw:
    for i, (roll, pitch, yaw) in enumerate(pose_array[:, 3:]):
        cr, sr = np.cos(np.deg2rad(roll)), np.sin(np.deg2rad(roll))
        cp, sp = np.cos(np.deg2rad(pitch)), np.sin(np.deg2rad(pitch))
        cy, sy = np.cos(np.deg2rad(yaw)), np.sin(np.deg2rad(yaw))
        R = np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
                    [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
                    [-sp, cp*sr, cp*cr]])
        #rotation_matrices[i] = R
        T=np.empty((3, 4))
        T[:3,:3]=R
        T[:3,3]=pose_array[i,:3]
        T_row=T.reshape(1,-1)
        np.savetxt(fw, T_row, delimiter=' ', fmt='%.6e')
        #print(T_row)
