import Communication as serial_comm


class Stepper:
    current_steps=0;
    def __init__(self, name, direction, distance):
        self.com = serial_comm.Communication()
        self.name = name
        self.direction = direction
        self.distance = distance

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_distance(self):
        return self.distance

    def get_direction(self):
        return self.direction

    def move(self, direction, distance):
        self.direction = direction
        self.distance = distance
        message = "{} {} {}".format(self.name, self.direction, self.distance)
        self.com.send(message)


class LeftStepper(Stepper):

    def __init__(self, name, direction, distance):
        super().__init__(name, direction, distance)

    def move(self, direction, distance):
        self.direction = direction
        self.distance = distance
        message = "{} {} {}".format(self.name, self.direction, self.distance)
        self.com.send(message)


class RightStepper(Stepper):

    def __init__(self, name, direction, distance):
        super().__init__(name, direction, distance)

    def move(self, direction, distance):
        self.direction = direction
        self.distance = distance
        message = "{} {} {}".format(self.name, self.direction, self.distance)
        self.com.send(message)
