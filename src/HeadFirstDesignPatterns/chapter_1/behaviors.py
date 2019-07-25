import abc


class FlyBehavior(metaclass=abc.ABCMeta):
    """
    Fly behavior interface
    """
    @abc.abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):

    def fly(self):
        print("I'm flying!")


class FlyNoWay(FlyBehavior):

    def fly(self):
        print("I can't fly..")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket")


class QuackBehavior(metaclass=abc.ABCMeta):
    """
    Quack behavior interface
    """
    @abc.abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):

    def quack(self):
        print("Quack!")


class MuteQuack(QuackBehavior):

    def quack(self):
        print("<< S I L E N C E >>")


class Squeak(QuackBehavior):

    def quack(self):
        print("Squeak!")
