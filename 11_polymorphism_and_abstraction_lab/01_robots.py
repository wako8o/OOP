class Robot:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 1


class MedicalRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 4


class WarRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 12

class SuperRobot(Robot):

    @staticmethod
    def sensors_amount():
        return 7


robot = [
        Robot('Robo'),
        MedicalRobot('Da Vinci'),
        ChefRobot('Moley'),
        WarRobot('Griffin'),
        SuperRobot('Emil')
        ]

for c in robot:
    print(f"sensors: {c.sensors_amount()} -> {c.name}")

