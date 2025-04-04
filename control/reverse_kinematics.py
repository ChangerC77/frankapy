from frankapy import FrankaArm

""" Get the joint position in radians """

def main():
    print('Get the joint position in radians')
    fr3 = FrankaArm() 
    print(fr3.get_joints()) # radians more details see franka_arm.py in get_joints function

if __name__ == "__main__":
    main()