import numpy as np
import matplotlib.pyplot as plt

def ReadVeri():
    with open('/EXTERNAL/datasets/SLAM2023/output/XA_202210131557_relative.txt', 'r') as f:
        lines = f.readlines()
        data = []
        for line in lines:
            line_data = line.split()
            float_data = [float(x) for x in line_data]
            data.append(float_data)
        np_data = np.array(data)
        pose_data=np_data[:, [3, 7, 11]]
        #print(pose_data)
        return pose_data

def ReadGT():
    with open('/EXTERNAL/homes/mengshj/new_catkin_ws/src/LCD/save_data/LCD_pairs.txt', 'r') as f:
        lines = f.readlines()
        data = []
        for line in lines:
            line_data = line.split()
            float_data = [float(x) for x in line_data]
            data.append(float_data)
        #print(data)
        np_data = np.array(data)
        #print(pose_data)
        return np_data    

def DrawLCD():
    points = ReadVeri()
    gt=ReadGT()

    # 绘制点云图
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(points[:,0], points[:,1], points[:,2], s=1,color='b')
    ax.scatter(points[:,0], points[:,1], points[:,2]-300, s=1)

    for i in range(len(gt)):
        curr=gt[i]
        s=int(curr[0])
        t=int(curr[1])
        # if abs(s-t)<1000:
        #     continue
        #print(s,' ',t)
        ax.plot([points[s,0],points[t,0]],[points[s,1],points[t,1]],[points[s,2],points[t,2]-300],color='r')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

DrawLCD()