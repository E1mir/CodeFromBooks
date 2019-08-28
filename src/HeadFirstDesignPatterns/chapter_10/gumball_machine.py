from HeadFirstDesignPatterns.chapter_10.states import (
    State,
    SoldOutState,
    NoQuarterState,
    HasQuarterState,
    SoldState,
    WinnerState
)


class GumballMachine(object):
    """
    Gumball machine
    """

    def __init__(self, number_gumballs: int):
        self.sold_out_state: State = SoldOutState(self)
        self.no_quarter_state: State = NoQuarterState(self)
        self.has_quarter_state: State = HasQuarterState(self)
        self.winner_state: State = WinnerState(self)
        self.sold_state: State = SoldState(self)

        self.count: int = number_gumballs

        if number_gumballs > 0:
            self.state = self.no_quarter_state
        else:
            self.state = self.sold_out_state

    def insert_quarter(self) -> None:
        self.state.insert_quarter()

    def eject_quarter(self) -> None:
        self.state.eject_quarter()

    def turn_crank(self) -> None:
        self.state.turn_crank()
        self.state.dispense()

    def release_ball(self) -> None:
        print('A gumball comes rolling out the slot...')

        if self.count != 0:
            self.count -= 1

    def refill(self, count: int) -> None:
        self.count += count
        print('The gumball machine was just refilled; it\'s new count is:', self.count)
        self.state.refill()

    def __str__(self) -> str:
        result = '\nMighty Gumball, Inc.'
        result += '\nPython-enabled Standing Gumball Model #3000'
        result += f'\nInventory: {self.count} gumball'
        if self.count != 1:
            result += 's'
        result += '\n'
        result += f'Machine is {self.state}\n'
        return result
