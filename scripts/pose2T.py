import numpy as np
from scipy.spatial.transform import Rotation

def pose_to_transform(pose):
    """
    将pose转化为齐次变换矩阵
    :param pose: 6x1向量，[x, y, z, roll, pitch, yaw]
    :return: 齐次变换矩阵
    """
    a,b,c,d,e,f,g,h,i,j,k,l = pose
    T = np.identity(4)
    T=[[a,b,c,d],[e,f,g,h],[i,j,k,l],[0,0,0,1]]
    return T

def pose_diff(T1, T2):
    """
    计算两个pose之间的相对变换矩阵
    :param T1: 齐次变换矩阵
    :param T2: 齐次变换矩阵
    :return: 齐次变换矩阵
    """
    T_rel = np.dot(T2, np.linalg.inv(T1))
    return T_rel

def transform_matrix(T_rel):
    """
    将相对变换矩阵转化为变换矩阵
    :param T_rel: 齐次变换矩阵
    :return: 变换矩阵
    """
    R = T_rel[:3, :3]
    t = T_rel[:3, 3]
    T = np.identity(4)
    T[:3, :3] = R
    T[:3, 3] = t
    return T

def pose2T(pose1,pose2):
    T1 = pose_to_transform(pose1)
    T2 = pose_to_transform(pose2)
    T_rel = pose_diff(T1, T2)
    return T_rel

def read_save(pathread,pathwrite,filename):
    with open(pathread+filename, 'r') as fr:
        poses = fr.readlines()
    with open(pathwrite+'transformations_'+filename, 'w') as fw:
        
        flag=0
        pose1=[]
        pose2=[]
        for pose in poses:
            pose = [float(i) for i in pose.strip().split()]
            if flag==0:
                pose1=pose
                flag=1
                continue
            else:
                pose2=pose
                T=pose2T(pose1,pose2)
            
            T_row=T.reshape(1,-1)
            # 将变换矩阵保存到文件中
            np.savetxt(fw, T_row, delimiter=' ', fmt='%lf')
            #fw.write('\n')
            pose1=pose2

def transAllfiles():
    indexs=["00","01","02","03","04","05","06","07","08","09","10"]
    pathread="/home/mengshj/docs/SI231/python-registration/data/groundtruth/"
    pathwrite="/home/mengshj/docs/SI231/python-registration/data/transform_rel/"
    for ind in indexs:
        filename=ind+".txt"
        read_save(pathread,pathwrite,filename)
        print(pathwrite+'transformations_'+filename+" is saved.")


transAllfiles()




