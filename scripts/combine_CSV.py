import os
import pandas as pd
from datetime import datetime

current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
#print(current_time)

# 设置文件夹路径和输出文件路径
folder_path = '/EXTERNAL/homes/mengshj/docs/SLAM2023/result/XA_train'
output_file = '/EXTERNAL/homes/mengshj/docs/SLAM2023/result/data/XA'+current_time+'.txt'

# 获取文件夹中所有CSV文件的路径
csv_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]

# 读取所有CSV文件并合并到一个DataFrame中
df = pd.concat((pd.read_csv(f) for f in csv_files))
df_12_cols = df.iloc[:, :12]
# 将合并后的DataFrame写入输出文件
df_12_cols.to_csv(output_file, sep=' ' ,index=False)