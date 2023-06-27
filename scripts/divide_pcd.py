import shutil
import os




if __name__ == '__main__':
    source_dir='/EXTERNAL/datasets/SLAM2023/XA_train/202210131557/PointClouds'
    target_dir='/EXTERNAL/datasets/SLAM2023/output/XA_train_pcd'
    pcd_files = os.listdir(source_dir)
    pcd_files.sort()
    #for i in range(pcd_files):
    i=0
    for pcd_file in pcd_files:
        if i<6000:
            shutil.copy(os.path.join(source_dir, pcd_file), os.path.join(target_dir,"0_6000", pcd_file))
            print("0->:",i)
        elif i<12000:
            shutil.copy(os.path.join(source_dir, pcd_file), os.path.join(target_dir,"6000_12000", pcd_file))
            print("6000->:",i)
        else:
            shutil.copy(os.path.join(source_dir, pcd_file), os.path.join(target_dir,"12000_18296", pcd_file))
            print("12000->:",i)
        i=i+1
