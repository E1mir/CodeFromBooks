from HeadFirstDesignPatterns.chapter_10.gumball_machine import GumballMachine


def test_gumball_machine(machine: GumballMachine) -> None:
    for i in range(10):
        print(machine)
        machine.insert_quarter()
        machine.turn_crank()


if __name__ == '__main__':
    gumball_machine = GumballMachine(10)
    test_gumball_machine(gumball_machine)
