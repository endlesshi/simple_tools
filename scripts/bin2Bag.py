#!./simple_tools/scripts/env/bin/python3.9
import argparse
import os
import logging
import math
import sys

import numpy as np
import rosbag
import rospy
import ros_numpy
from tqdm import tqdm


from sensor_msgs.msg import PointCloud2

def load_and_create_pc_msg(filepath: str, frame_id: str):
    pc = np.fromfile(filepath, dtype=np.float32).reshape(-1, 4)

    pc_array = np.zeros(len(pc), dtype=[
        ('x', np.float32),
        ('y', np.float32),
        ('z', np.float32),
        ('intensity', np.float32),
    ])

    pc_array['x'] = pc[:, 0]
    pc_array['y'] = pc[:, 1]
    pc_array['z'] = pc[:, 2]
    pc_array['intensity'] = pc[:, 3]
    
    timestamp = float(filepath.split("/")[-1][:-4])
    timestamp_sec = math.floor(timestamp / 1.0e6)
    timestamp_nsec = (timestamp - timestamp_sec * 1e6) * 1e3
    
    ros_time = rospy.Time(timestamp_sec, timestamp_nsec)

    pc_msg = ros_numpy.msgify(PointCloud2, pc_array, stamp=ros_time, frame_id='hesai')
    return pc_msg, ros_time

if __name__ == '__main__':
    
    argparser = argparse.ArgumentParser(description='Convert bin files to rosbag')
    
    argparser.add_argument("-i", "--input-dir", type=str, required=True, help="input directory")
    argparser.add_argument("-o", "--output-bag", type=str, required=True, help="output directory")
    argparser.add_argument("-t", "--topic", type=str, default="/scan", help="pointcloud topic")
    argparser.add_argument("-f", "--frame-id", type=str, default="hesai", help="pointcloud frame id")
    
    args = argparser.parse_args()
    
    if not os.path.exists(args.input_dir) or not os.path.isdir(args.input_dir):
        logging.error(f"Output directory {args.input_dir} does not exist or is not a directory")
        sys.exit(1)
        
    bin_files = os.listdir(args.input_dir)
    bin_files.sort()
    
    with rosbag.Bag(args.output_bag, 'w') as bag:
        for bin_file in tqdm(bin_files):
            pc_msg, ros_time = load_and_create_pc_msg(os.path.join(args.input_dir, bin_file), args.frame_id)
            bag.write(args.topic, pc_msg, ros_time)
