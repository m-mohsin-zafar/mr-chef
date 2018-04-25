import getch as gc
import Stepper as stepper
if __name__ == '__main__':
    both_stepper = stepper.Stepper('B', '+', 0);
    left_stepper = stepper.LeftStepper('L', '+', 0);
    right_stepper = stepper.RightStepper('R', '+', 0);
    left_stepper.move("-",0)
    right_stepper.move("-",0)
    print("Go")
    while True:
        key = ord(gc.getch())

        if key == 49: #1
            print("Left")
            key = ord(gc.getch())
            while (key==43 or key==45):
                if key==43:
                    if 0<= left_stepper.current_steps <=62:
                        step=input("how much steps to increase: ")
                        step=int(step)
                        left_stepper.move("+",step)
                        left_stepper.current_steps+=step
                    print("Left Stepper : ",left_stepper.current_steps)
                elif key == 45:
                    if 0<= left_stepper.current_steps <=62:
                        step=input("how much steps to decrease: ")
                        step=int(step)
                        left_stepper.move("-",step)
                        left_stepper.current_steps-=step
                    print("Left Stepper : ",left_stepper.current_steps)
                key = ord(gc.getch())
        elif key == 50: #2
            print("Right")
            key = ord(gc.getch())
            while (key==43 or key==45):
                if key==43:
                    if 0<= right_stepper.current_steps <=62:
                        step=input("how much steps to increase: ")
                        step=int(step)
                        right_stepper.move("+",step)
                        right_stepper.current_steps+=step
                    print("Right Stepper : ",right_stepper.current_steps)
                elif key==45:
                    if 0<= right_stepper.current_steps <=62:
                        step=input("how much steps to decrease: ")
                        step=int(step)
                        right_stepper.move("-",step)
                        right_stepper.current_steps-=step
                    print("Right Stepper : ",right_stepper.current_steps)
                key = ord(gc.getch())

    # right_stepper.move("+", 62)
    # left_stepper.move("-", 10)
    # right_stepper.move("-", 62)
    # both_stepper.move("+", 50);
    # both_stepper.move("-", 50);
