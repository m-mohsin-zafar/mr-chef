from Arms import Arms
from Steppers import Steppers
from RecipeLoader import Loader
import time as t


class chef:


    def __init__(self):
        self.recipe = Loader.Recipe_Loader()
        self.left_arm = Arms.LeftArm("Left", "I")
        self.right_arm = Arms.RightArm("Right", "I")
        self.both_arms = Arms.Arms("Both", "S")
        self.left_stepper = Steppers.LeftStepper('L', '+', 0)
        self.right_stepper = Steppers.RightStepper('R', '+', 0)
        self.both_stepper = Steppers.Stepper('B', '+', 0)
        self.initArms()
        self.initSteppers()

    def cook(self, recipe_name):
        self.recipe.load_recipe(recipe_name)
        instructions = self.recipe.instructions[0].split(",")
        for x in range(instructions.__len__()):
            if instructions[x].split(" ")[0] == "add":
                self.performAcrions(self.recipe.ing_angles[instructions[x].split(" ")[1]].split(":"))
            elif instructions[x].split(" ")[0] == "switch" or instructions[x].split(" ")[0] == "place" or instructions[x].split(" ")[0] == "stir":
                self.performAcrions(self.recipe.utn_angles[instructions[x].split(" ")[1]].split(":"))

    def initArms(self):
        print("Initializing Arms...")
        self.both_arms.send_angles(2)
        self.left_arm.send_angles(2)
        self.right_arm.send_angles(2)
        t.sleep(3)
        self.both_arms.synchronize("SYNC")
    def initSteppers(self):
        print("Initializing Steppers...")
        self.left_stepper.move("+", 0, 2)
        self.right_stepper.move("+", 0, 2)
        self.both_stepper.move("-", 0, 2)
        self.right_stepper.home(3)
        self.left_stepper.home(3)
        t.sleep(6)
        self.both_stepper.synchronize("SYNC")
    def performAcrions(self, angles):
        for x in range(angles.__len__()):
            if angles[x] == 'PICK':
                continue
            elif angles[x] == 'POUR':
                continue
            elif angles[x] == 'PLACE':
                continue
            elif angles[x] == 'off':
                continue
            elif angles[x] == 'on':
                continue
            elif angles[x] == 'STIR':
                continue
            elif angles[x] == 'SYNC':
                message = "SYNC"
                self.both_arms.synchronize(message)
                self.both_stepper.synchronize(message)
                print("Synchronized!")
                continue
            else:
                if(angles[x].split(' ').__len__()==2):
                    if(angles[x].split(' ')[0]=="Home_Left"):
                        self.left_stepper.home(int(angles[x].split(' ')[1]))
                    elif(angles[x].split(' ')[0]=="Home_Right"):
                        self.right_stepper.home(int(angles[x].split(' ')[1]))
                    t.sleep(2)
                if(angles[x].split(' ').__len__())==4:
                    print("{} Stepper to move: {}{}".format(angles[x].split(' ')[0], angles[x].split(' ')[1], int(angles[x].split(' ')[2])))
                    if angles[x].split(' ')[0] == 'Left' :
                        self.left_stepper.move(angles[x].split(' ')[1], angles[x].split(' ')[2], int(angles[x].split(' ')[3]))
                    elif angles[x].split(' ')[0] == 'Right':
                        self.right_stepper.move(angles[x].split(' ')[1], angles[x].split(' ')[2], int(angles[x].split(' ')[3]))
                    elif angles[x].split(' ')[0] == 'Both' :
                        self.both_stepper.move(angles[x].split(' ')[1], angles[x].split(' ')[2], int(angles[x].split(' ')[3]))
                    t.sleep(2)
                if(angles[x].split(' ').__len__()) == 16:
                    print("Left Arm to move :{}".format(angles[x]))
                    if(angles[x].split(' ')[0]=="Right"):
                        self.right_arm.set_base(angles[x].split(' ')[1], int(angles[x].split(' ')[2]))
                        self.right_arm.set_shoulder(angles[x].split(' ')[3], int(angles[x].split(' ')[4]))
                        self.right_arm.set_elbow(angles[x].split(' ')[5], int(angles[x].split(' ')[6]))
                        self.right_arm.set_wrist_rot(angles[x].split(' ')[7], int(angles[x].split(' ')[8]))
                        self.right_arm.set_wrist_pitch(angles[x].split(' ')[9], int(angles[x].split(' ')[10]))
                        self.right_arm.set_wrist_roll(angles[x].split(' ')[11], int(angles[x].split(' ')[12]))
                        self.right_arm.set_gripper(angles[x].split(' ')[13], int(angles[x].split(' ')[14]))
                        self.right_arm.send_angles(int(angles[x].split(' ')[15]))
                    if(angles[x].split(' ')[0]=="Left"):
                        self.left_arm.set_base(angles[x].split(' ')[1], int(angles[x].split(' ')[2]))
                        self.left_arm.set_shoulder(angles[x].split(' ')[3], int(angles[x].split(' ')[4]))
                        self.left_arm.set_elbow(angles[x].split(' ')[5], int(angles[x].split(' ')[6]))
                        self.left_arm.set_wrist_rot(angles[x].split(' ')[7], int(angles[x].split(' ')[8]))
                        self.left_arm.set_wrist_pitch(angles[x].split(' ')[9], int(angles[x].split(' ')[10]))
                        self.left_arm.set_wrist_roll(angles[x].split(' ')[11], int(angles[x].split(' ')[12]))
                        self.left_arm.set_gripper(angles[x].split(' ')[13], int(angles[x].split(' ')[14]))
                        self.left_arm.send_angles(int(angles[x].split(' ')[15]))
                    if(angles[x].split(' ')[0]=="Both"):
                        self.both_arms.set_base(angles[x].split(' ')[1], int(angles[x].split(' ')[2]))
                        self.both_arms.set_shoulder(angles[x].split(' ')[3], int(angles[x].split(' ')[4]))
                        self.both_arms.set_elbow(angles[x].split(' ')[5], int(angles[x].split(' ')[6]))
                        self.both_arms.set_wrist_rot(angles[x].split(' ')[7], int(angles[x].split(' ')[8]))
                        self.both_arms.set_wrist_pitch(angles[x].split(' ')[9], int(angles[x].split(' ')[10]))
                        self.both_arms.set_wrist_roll(angles[x].split(' ')[11], int(angles[x].split(' ')[12]))
                        self.both_arms.set_gripper(angles[x].split(' ')[13], int(angles[x].split(' ')[14]))
                        self.both_arms.send_angles(int(angles[x].split(' ')[15]))
