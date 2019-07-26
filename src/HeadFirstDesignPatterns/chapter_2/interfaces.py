import abc


class Observer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update(self, temperature, humidity, pressure):
        pass


class DisplayElement(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def display(self):
        pass


class Subject(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def register_observer(self, observer):
        pass

    @abc.abstractmethod
    def remove_observer(self, observer):
        pass

    @abc.abstractmethod
    def notify_observers(self):
        pass
