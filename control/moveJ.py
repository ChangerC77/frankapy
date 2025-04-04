from frankapy import FrankaArm

""" move FR3 with the joint position control """

def main():
    print('move FR3 with the joint position control')
    fa = FrankaArm() 
    
    desired_joint = [-5.30563281e-04, -7.85650762e-01, 3.78420727e-04, -2.35655981e+00, 5.68448066e-04, 1.57095379e+00, 7.85057444e-01]
    
    fa.goto_joints(desired_joint)
    
    print("motion finished!")
    
if __name__ == "__main__":
    main()