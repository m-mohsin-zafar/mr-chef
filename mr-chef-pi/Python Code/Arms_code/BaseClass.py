import getch as gc
import Arms as arms

if __name__ == '__main__':
    both_arm = arms.Arms("Both", "S")
    left_arm = arms.LeftArm("Left", "I")
    right_arm = arms.RightArm("Right", "I")
    # left_arm.set_elbow(120, 10)
    # left_arm.send_angles()
    # both_arm.set_elbow(90, 10)
    # both_arm.set_shoulder(120, 10)
    # both_arm.set_wrist_pitch(20, 10)
    # both_arm.send_angles()
    # right_arm.set_shoulder(90, 10)
    # right_arm.send_angles()
    # left_arm.home()
    # both_arm.home()
    # right_arm.home()


    while True:
        key = ord(gc.getch())

        if key == 49: #1
            print("1")
            key = ord(gc.getch())
            while (key==43 or key==45):
                if key==43:
                    ang=input("How much to increase: ")
                    ang=int(ang)
                    left_arm.set_base(left_arm.base+ang,10)
                    left_arm.send_angles()
                    print("DOF_1 -> ",left_arm.base)
                elif key == 45:
                    ang=input("How much to decrease: ")
                    ang=int(ang)
                    left_arm.set_base(left_arm.base-ang,10)
                    left_arm.send_angles()
                    print("DOF_1 -> ",left_arm.base)
                key = ord(gc.getch())
        elif key == 50: #2
            print("2")
            key = ord(gc.getch())
            while (key==43 or key==45):
                if key==43:
                    ang=input("How much to increase: ")
                    ang=int(ang)
                    left_arm.set_shoulder(left_arm.shoulder+ang,10)
                    left_arm.send_angles()
                    print("DOF_2 -> ",left_arm.shoulder)
                elif key==45:
                    ang=input("How much to decrease: ")
                    ang=int(ang)
                    left_arm.set_shoulder(left_arm.shoulder-ang,10)
                    left_arm.send_angles()
                    print("DOF_2 -> ",left_arm.shoulder)
                key = ord(gc.getch())
        elif key == 51: #3
            print("3")
            key = ord(gc.getch())
            while (key==43 or key==45):
                if key==43:
                    ang=input("How much to increase: ")
                    ang=int(ang)
                    left_arm.set_elbow(left_arm.elbow+ang,10)
                    left_arm.send_angles()
                    print("DOF_3 -> ",left_arm.elbow)
                elif key==45:
                    ang=input("How much to decrease: ")
                    ang=int(ang)
                    left_arm.set_elbow(left_arm.elbow-ang,10)
                    left_arm.send_angles()
                    print("DOF_3 -> ",left_arm.elbow)
                key = ord(gc.getch())
        elif key == 52: #4
            print("4")
            key = ord(gc.getch())
            while (key==43 or key==45):
                if key==43:
                    ang=input("How much to increase: ")
                    ang=int(ang)
                    left_arm.set_wrist_rot(left_arm.wrist_rot+ang,10)
                    left_arm.send_angles()
                    print("DOF_4 -> ",left_arm.wrist_rot)
                elif key==45:
                    ang=input("How much to decrease: ")
                    ang=int(ang)
                    left_arm.set_wrist_rot(left_arm.wrist_rot-ang,10)
                    left_arm.send_angles()
                    print("DOF_4 -> ",left_arm.wrist_rot)
                key = ord(gc.getch())
        elif key == 53: #5
            print("5")
            key = ord(gc.getch())
            while (key==43 or key==45):
                if key==43:
                    ang=input("How much to increase: ")
                    ang=int(ang)
                    left_arm.set_wrist_pitch(left_arm.wrist_pitch+ang,10)
                    left_arm.send_angles()
                    print("DOF_5 -> ",left_arm.wrist_pitch)
                elif key==45:
                    ang=input("How much to decrease: ")
                    ang=int(ang)
                    left_arm.set_wrist_pitch(left_arm.wrist_pitch-ang,10)
                    left_arm.send_angles()
                    print("DOF_5 -> ",left_arm.wrist_pitch)
                key = ord(gc.getch())
        elif key == 54: #6
            print("6")
            key = ord(gc.getch())
            while (key==43 or key==45):
                if key==43:
                    ang=input("How much to increase: ")
                    ang=int(ang)
                    left_arm.set_wrist_roll(left_arm.wrist_roll+ang,10)
                    left_arm.send_angles()
                    print("DOF_6 -> ",left_arm.wrist_roll)
                elif key==45:
                    ang=input("How much to decrease: ")
                    ang=int(ang)
                    left_arm.set_wrist_roll(left_arm.wrist_roll-ang,10)
                    left_arm.send_angles()
                    print("DOF_6 -> ",left_arm.wrist_roll)
                key = ord(gc.getch())
        elif key == 55: #7
            print("7")
            key = ord(gc.getch())
            while (key==43 or key==45):
                if key==43:
                    if 40 <= left_arm.gripper <= 95:
                        ang=input("How much to increase: ")
                        ang=int(ang)
                        left_arm.set_gripper(left_arm.gripper+ang,0)
                        left_arm.send_angles()
                    print("DOF_7 -> ",left_arm.gripper)
                elif key==45:
                    if 40 <= left_arm.gripper <= 95:
                        ang=input("How much to decrease: ")
                        ang=int(ang)
                        left_arm.set_gripper(left_arm.gripper-ang,0)
                        left_arm.send_angles()
                    print("DOF_7 -> ",left_arm.gripper)
                key = ord(gc.getch())
        elif key == 112: #P
            print("\n---------------: ","1","\t"
          ,"2","\t"
          ,"3","\t"
          ,"4","\t"
          ,"5","\t"
          ,"6","\t"
          ,"7","\t")
            print("\nCurrent Angles : ",left_arm.base,"\t"
          ,left_arm.shoulder,"\t"
          ,left_arm.elbow,"\t"
          ,left_arm.wrist_rot,"\t"
          ,left_arm.wrist_pitch,"\t"
          ,left_arm.wrist_roll,"\t"
          ,left_arm.gripper,"\t")
