from abc import abstractmethod, ABC


class Duck(ABC):

    @staticmethod
    def quack():
        pass

    @staticmethod
    def walk():
        pass

    @staticmethod
    def fly():
        pass

class SoundDuck(ABC):

    @abstractmethod
    def make_sound(self):
        pass

class RubberDuck(SoundDuck):

    def make_sound(self):
        return "Squeek"

class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):

        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0

