from abc import abstractmethod, ABC


class Duck(ABC):
    @staticmethod
    def quack():
        pass


class MovingDuck(Duck, ABC):

    @staticmethod
    def walk():
        pass

    @abstractmethod
    def fly(self):
        pass


class RubberDuck(Duck):
    @staticmethod
    def quack():
        return "Squeek"


class RobotDuck(MovingDuck):
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
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0
