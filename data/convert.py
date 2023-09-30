from loader import load_data_points
from glob import glob
from tqdm import tqdm
import numpy as np
import struct
import sys
import open3d as o3d
import os

def get_files(dir_pattern: str) -> list:
    return glob(dir_pattern)


def convert(input_path, save_dir):
    # sensor, intensity = load_data_points(input_path)
    size_float = 4
    list_pcd = []
    name = ""
    with open(input_path, "rb") as f:
        name = os.path.basename(input_path).split(".")[0]
        while byte := f.read(size_float * 4):
            x, y, z, intensity = struct.unpack("ffff", byte)
            list_pcd.append([x, y, z])
    np_pcd = np.asarray(list_pcd)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np_pcd)
    # save
    pcdFileName = f"{save_dir}/{name}.pcd"
    o3d.io.write_point_cloud(pcdFileName, pcd)


if __name__ == "__main__":
    pattern = "C:/Users/Diana/Desktop/DATA/SemanticKitti/data_odometry_velodyne/dataset/sequences/00/velodyne/*.bin"
    files = get_files(pattern)
    for f in tqdm(files):
        convert(f, "C:/Users/Diana/Desktop/DATA/SemanticKitti/data_odometry_velodyne/dataset/converted")

