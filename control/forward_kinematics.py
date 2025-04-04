from frankapy import FrankaArm
import numpy as np
from autolab_core import RigidTransform
from scipy.spatial.transform import Rotation as R


""" Get the joint position in radians """

def main():
    print('Get the joint position in radians')
    fa = FrankaArm() 
    joint = fa.get_joints()
    pose = fa.get_pose()
    
    # transforms_matrices = fa.get_links_transforms(joint, use_rigid_transforms=False) # radians more details see franka_arm.py in get_joints function

    # 调用正向运动学函数
    transforms = fa.get_links_transforms(joint, use_rigid_transforms=False)

    # 获取末端执行器的位姿
    franka_tool_transform = transforms[-1]  # 获取 franka_tool 的齐次变换矩阵

    # 提取位置和方向
    position = franka_tool_transform[:3, 3]  # 提取平移向量
    rotation = franka_tool_transform[:3, :3]  # 提取旋转矩阵

    print("End-effector Position:", position)
    print("End-effector Rotation Matrix:\n", rotation)
    
    r = R.from_matrix(rotation)
    quaternion = r.as_quat()
    print(quaternion)
    # # 获取 franka_tool_base 的变换矩阵
    # franka_tool_base_matrix = transforms_matrices[10]  # 从 world 到 franka_tool_base 的变换

    # # 获取工具偏移矩阵（tool_delta_pose）
    # tool_delta_matrix = RigidTransform(from_frame='franka_tool', 
    #                                            to_frame='franka_tool_base')  # 从 franka_tool_base 到 franka_tool 的偏移

    # # 计算 franka_tool 的变换矩阵
    # franka_tool_matrix = franka_tool_base_matrix @ tool_delta_matrix

    # # 输出结果
    # print("franka_tool transform matrix:\n", franka_tool_matrix)
    print("franka pose: ", pose)
    
if __name__ == "__main__":
    main()