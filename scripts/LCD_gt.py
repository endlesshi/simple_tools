import numpy as np
import math

def Verify(pose_data):
    # filepath="/media/nas/RIClShare/DataSets/KITTI_ODOMETRY_LIDAR/gt/00.txt"
    # pose_data=np.load(filepath)
    # pose_data=pose_data[:, [3, 7, 11]]
    # print(len(pose_data))
    # print(len(pose_data)-50)
    with open("/EXTERNAL/homes/mengshj/new_catkin_ws/src/SC-A-LOAM/save_data/LCD_gt.txt", "w") as f:
    #array=[]
        for i in range(len(pose_data)):
            pose_curr=pose_data[i]
            if i>50:
                index=-1
                mindis=1000000
                for j in range(i-50):
                    pose_pre=pose_data[j]
                    distance= math.sqrt((pose_pre[0] - pose_curr[0]) ** 2 + (pose_pre[1] - pose_curr[1]) ** 2 + (pose_pre[2] - pose_curr[2]) ** 2)
                    if mindis>distance:
                        index=j
                        mindis=distance
                if mindis < 0.5 :
                    
                    #array.append(j,i)
                    f.write(str(i)+' '+str(j)+' '+str(mindis)+'\n')
    #np.savetxt('/EXTERNAL/homes/mengshj/new_catkin_ws/src/SC-A-LOAM/save_data/LCD_gt.txt', array, delimiter=' ')

def ReadVeri():
    with open('/media/nas/RIClShare/DataSets/KITTI_ODOMETRY_LIDAR/gt/00.txt', 'r') as f:
        lines = f.readlines()
        data = []
        for line in lines:
            line_data = line.split()
            float_data = [float(x) for x in line_data]
            data.append(float_data)
        np_data = np.array(data)
        pose_data=np_data[:, [3, 7, 11]]
        #print(pose_data)
        Verify(pose_data)

ReadVeri()




