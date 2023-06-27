import numpy as np
#from scipy.spatial.transform import Rotation

def pose_to_transform(pose):
    """
    将pose转化为齐次变换矩阵
    :param pose: 6x1向量，[x, y, z, roll, pitch, yaw]
    :return: 齐次变换矩阵
    """
    a,b,c,d,e,f,g,h,i,j,k,l = pose
    T = np.identity(4)
    T=[[a,b,c,d],[e,f,g,h],[i,j,k,l],[0,0,0,1]]
    return np.array(T)

def pose_diff(T1, T2):
    """
    计算两个pose之间的相对变换矩阵
    :param T1: 齐次变换矩阵
    :param T2: 齐次变换矩阵
    :return: 齐次变换矩阵
    """
    T_rel = np.dot(np.linalg.inv(T1),T2)
    return T_rel

def divide_gt(pose,start_index,end_index,filename):
    flag=0
    pose1=[]
    pose2=[]
    T1 = np.identity(4)
    T2 = np.identity(4)
    with open(filename+"_divided_"+str(start_index)+"_"+str(end_index)+"_gt.txt", 'w') as fw:
        for i in range(start_index,end_index):
            if flag==0:
                T1=pose_to_transform(pose[i])
                flag=1
                T = np.identity(4)
                np.savetxt(fw, T[:3, :].reshape(1,-1), delimiter=' ', fmt='%lf')
            else:
                T2=pose_to_transform(pose[i])
                #print(T1)
                T=pose_diff(T1,T2)
                np.savetxt(fw, T[:3, :].reshape(1,-1), delimiter=' ', fmt='%lf')


if __name__ == '__main__':
    inputFileName="/EXTERNAL/datasets/SLAM2023/gt/XA_202210131557_relative"
    outputFileName="/EXTERNAL/datasets/SLAM2023/output/gt/XA_202210131557_relative"
    poses = np.loadtxt(inputFileName+".txt")
    #print(poses.shape[0])
    divide_gt(poses,0,6000,outputFileName)
    divide_gt(poses,6000,12000,outputFileName)
    divide_gt(poses,12000,poses.shape[0],outputFileName)

