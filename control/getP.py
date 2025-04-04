from frankapy import FrankaArm
from scipy.spatial.transform import Rotation as R
import numpy as np

""" get end-effect 6 Dof pose """

def main():
    print('Get end-effect 6 Dof pose')
    fa = FrankaArm()
    
    T_ee_world = fa.get_pose()
    print('pose: ', T_ee_world)
    
if __name__ == "__main__":
    main()