from frankapy import FrankaArm

""" Get the joint position in radians """

def main():
    print('Get the joint position in radians')
    fa = FrankaArm() 
    print(fa.get_joints()) # radians more details see franka_arm.py in get_joints function

if __name__ == "__main__":
    main()