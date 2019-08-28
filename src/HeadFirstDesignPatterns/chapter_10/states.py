import abc
import random


class State(metaclass=abc.ABCMeta):
    """
    State interface
    """

    @abc.abstractmethod
    def insert_quarter(self) -> None:
        pass

    @abc.abstractmethod
    def eject_quarter(self) -> None:
        pass

    @abc.abstractmethod
    def turn_crank(self) -> None:
        pass

    @abc.abstractmethod
    def dispense(self) -> None:
        pass

    @abc.abstractmethod
    def refill(self) -> None:
        pass


class NoQuarterState(State):
    """
    No quarter state for gumball machine
    """

    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print('You inserted a quarter')
        self.gumball_machine.state = self.gumball_machine.has_quarter_state

    def eject_quarter(self) -> None:
        print('You haven\'t inserted a quarter')

    def turn_crank(self) -> None:
        print('You turned, bu there\'s no quarter')

    def dispense(self) -> None:
        print('You need to pay first')

    def refill(self) -> None:
        pass

    def __str__(self) -> str:
        return 'waiting for quarter'


class HasQuarterState(State):
    """
    Has quarter state for gumball machine
    """

    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print('You can\'t insert another quarter')

    def eject_quarter(self) -> None:
        print('Quarter returned')
        self.gumball_machine.state = self.gumball_machine.no_quarter_state

    def turn_crank(self) -> None:
        print('You turned...')
        winner = random.randint(0, 10)
        if winner == 0 and self.gumball_machine.count > 1:
            self.gumball_machine.state = self.gumball_machine.winner_state
        else:
            self.gumball_machine.state = self.gumball_machine.sold_state

    def dispense(self) -> None:
        print('No gumball dispensed')

    def refill(self) -> None:
        pass

    def __str__(self) -> str:
        return 'waiting for turn of crank'


class SoldState(State):
    """
    Sold state for gumball machine
    """

    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print('Please wait, we are already giving you a gumball')

    def eject_quarter(self) -> None:
        print('Sorry, you already turned the crank')

    def turn_crank(self) -> None:
        print('Turning twice does not get you another gumball!')

    def dispense(self) -> None:
        self.gumball_machine.release_ball()
        if self.gumball_machine.count > 0:
            self.gumball_machine.state = self.gumball_machine.no_quarter_state
        else:
            print('Oops, out of gumballs!')
            self.gumball_machine.state = self.gumball_machine.sold_out_state

    def refill(self) -> None:
        pass

    def __str__(self) -> str:
        return 'dispensing a gumball'


class SoldOutState(State):
    """
    Sold out state for gumball machine
    """

    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print('You can\'t insert a quarter, the machine is sold out')

    def eject_quarter(self) -> None:
        print('You can\'t eject, you haven\'t inserted a quarter yet')

    def turn_crank(self) -> None:
        print('You turned, but there are no gumballs')

    def dispense(self) -> None:
        print('No gumball dispensed')

    def refill(self) -> None:
        self.gumball_machine.state = self.gumball_machine.no_quarter_state

    def __str__(self) -> str:
        return 'sold out'


class WinnerState(State):
    """
    Winner stater for gumball machine
    """

    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print('Please wait, we are already giving you a Gumball')

    def eject_quarter(self) -> None:
        print('Please wait, we are already giving you a Gumball')

    def turn_crank(self) -> None:
        print('Turning again does not get you another gumball!')

    def dispense(self) -> None:
        self.gumball_machine.release_ball()
        if self.gumball_machine.count == 0:
            self.gumball_machine.state = self.gumball_machine.sold_out_state
        else:
            self.gumball_machine.release_ball()
            print('YOU ARE A WINNER! You got two gumballs for your quarter')
            if self.gumball_machine.count > 0:
                self.gumball_machine.state = self.gumball_machine.no_quarter_state
            else:
                print('Oops, out of gumballs!')
                self.gumball_machine.state = self.gumball_machine.sold_out_state

    def refill(self) -> None:
        pass

    def __str__(self) -> str:
        return 'dispensing two gumballs for your quarter, because YOU ARE A WINNER!'
