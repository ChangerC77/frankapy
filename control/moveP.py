from frankapy import FrankaArm
from autolab_core import RigidTransform
import numpy as np

""" move FR3 with the 6 Dof position control """

def main():
    print('mmove FR3 with the 6 Dof position control')
    fa = FrankaArm() 
    # franka_pose = fa.get_pose()
    # franka_pose = np.concatenate(franka_pose.translation, franka_pose.rol)
    # pose1 = franka_pose_to_rigid_transform(franka_pose, from_frame='franka_tool_base', to_frame='world')
    # print("pose1 :", pose1)
    pose = RigidTransform(  # tool -> base
            rotation = np.array([[9.99999969e-01, 1.64463609e-04, -2.96952606e-05],
                                [1.64477685e-04, -9.99999857e-01, 4.74613219e-04],
                                [-2.96171997e-05, -4.74618089e-04, -9.99999887e-01]]),
            translation=np.array([3.07066339e-01, 1.49129146e-04, 4.86966103e-01]),
            from_frame='franka_tool',
            to_frame='world',
        )
    # print("pose1 :", pose)
    fa.goto_pose(pose)
    
    print("motion finished!")
    
def franka_pose_to_rigid_transform(franka_pose, from_frame='franka_tool_base', to_frame='world'):
    np_franka_pose = np.array(franka_pose).reshape(4, 4).T
    pose = RigidTransform(
            rotation=np_franka_pose[:3, :3], 
            translation=np_franka_pose[:3, 3],
            from_frame=from_frame,
            to_frame=to_frame
        )
    return pose
    
if __name__ == "__main__":
    main()