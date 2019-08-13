import random

from HeadFirstDesignPatterns.chapter_7.adapter.birds import Duck, Turkey


class TurkeyAdapter(Duck):
    """
    Turkey adapter
    """

    def __init__(self, turkey: Turkey):
        self.turkey: Turkey = turkey

    def quack(self) -> None:
        self.turkey.gobble()

    def fly(self) -> None:
        for i in range(5):
            self.turkey.fly()


class DuckAdapter(Turkey):
    """
    Duck adapter
    """

    def __init__(self, duck: Duck):
        self.duck: Duck = duck

    def gobble(self) -> None:
        self.duck.quack()

    def fly(self) -> None:
        # Flies every 3d time
        if random.randrange(3) == 0:
            self.duck.fly()
