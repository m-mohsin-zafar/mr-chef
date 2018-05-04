from Arms import Communication as serial_comm


class Arms:
    # Joint Angle Variables
    base = 0
    shoulder = 90
    elbow = 110
    wrist_rot = 110
    wrist_pitch = 110
    wrist_roll = 90
    gripper = 40

    # Speed Variables LIMIT: (5<= speed <= 15)
    baseSpeed = 15
    shoulderSpeed = 15
    elbowSpeed = 15
    wrist_rotSpeed = 15
    wrist_pitchSpeed = 15
    wrist_rollSpeed = 15
    gripperSpeed = 15

    def __init__(self, arm, mode):
        self.com = serial_comm.Communication()
        self.arm = arm
        self.mode = mode

    # Getters
    def get_arm(self):
        return self.arm

    def get_mode(self):
        return self.mode

    def get_base(self):
        return "{} {}".format(self.base, self.baseSpeed)

    def get_shoulder(self):
        return "{} {}".format(self.shoulder, self.shoulderSpeed)

    def get_elbow(self):
        return "{} {}".format(self.elbow, self.elbowSpeed)

    def get_wrist_rot(self):
        return "{} {}".format(self.wrist_rot, self.wrist_rotSpeed)

    def get_wrist_pitch(self):
        return "{} {}".format(self.wrist_pitch, self.wrist_pitchSpeed)

    def get_wrist_roll(self):
        return "{} {}".format(self.wrist_roll, self.wrist_rollSpeed)

    def get_gripper(self):
        return "{} {}".format(self.gripper, self.gripperSpeed)

    # Setters
    def set_base(self, base, speed):
        self.base = base
        self.baseSpeed = speed

    def set_shoulder(self, shoulder, speed):
        self.shoulder = shoulder
        self.shoulderSpeed = speed

    def set_elbow(self, elbow, speed):
        self.elbow = elbow
        self.elbowSpeed = speed

    def set_wrist_rot(self, wrist_rot, speed):
        self.wrist_rot = wrist_rot
        self.wrist_rotSpeed = speed

    def set_wrist_pitch(self, wrist_pitch, speed):
        self.wrist_pitch = wrist_pitch
        self.wrist_pitchSpeed = speed

    def set_wrist_roll(self, wrist_roll, speed):
        self.wrist_roll = wrist_roll
        self.wrist_rollSpeed = speed

    def set_gripper(self, gripper, speed):
        self.gripper = gripper
        self.gripperSpeed = speed

    # Homing
    def home(self):
        self.com.send_homing(self.get_arm())

    # Send Message
    def send_angles(self, delay):
        self.com.send(self.generate_message(), delay)

    # Generate Message for communicating Arduino
    def generate_message(self):
        return '{} {} {} {} {} {} {} {} {}'.format(self.get_mode(), self.get_arm(), self.get_base(), self.get_shoulder(), self.get_elbow(), self.get_wrist_rot(), self.get_wrist_pitch(), self.get_wrist_roll(), self.get_gripper())


class LeftArm(Arms):
    def __init__(self, arm, mode):
        super().__init__(arm, mode)


class RightArm(Arms):
    def __init__(self, arm, mode):
        super().__init__(arm, mode)
