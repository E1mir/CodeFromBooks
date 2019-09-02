from HeadFirstDesignPatterns.chapter_12.compound_patterns.adapters import GooseAdapter
from HeadFirstDesignPatterns.chapter_12.compound_patterns.composites import Flock
from HeadFirstDesignPatterns.chapter_12.compound_patterns.decorators import QuackCounter
from HeadFirstDesignPatterns.chapter_12.compound_patterns.factories import AbstractDuckFactory, CountingDuckFactory
from HeadFirstDesignPatterns.chapter_12.compound_patterns.interfaces import Quackable
from HeadFirstDesignPatterns.chapter_12.compound_patterns.models import Goose
from HeadFirstDesignPatterns.chapter_12.compound_patterns.observables import Quackologist


def simulate(duck: Quackable):
    duck.quack()


def simulation(duck_factory: AbstractDuckFactory):
    # Defining ducks
    redhead_duck: Quackable = duck_factory.create_redhead_duck()
    duck_call: Quackable = duck_factory.create_duck_call()
    rubber_duck: Quackable = duck_factory.create_rubber_duck()
    goose_duck: Quackable = GooseAdapter(Goose())

    # Create flock of ducks
    flock_of_ducks: Flock = Flock()

    flock_of_ducks.add(redhead_duck)
    flock_of_ducks.add(duck_call)
    flock_of_ducks.add(rubber_duck)
    flock_of_ducks.add(goose_duck)

    # Create flock of mallards
    flock_of_mallards: Flock = Flock()

    mallard_one = duck_factory.create_mallard_duck()
    mallard_two = duck_factory.create_mallard_duck()
    mallard_three = duck_factory.create_mallard_duck()
    mallard_four = duck_factory.create_mallard_duck()

    flock_of_mallards.add(mallard_one)
    flock_of_mallards.add(mallard_two)
    flock_of_mallards.add(mallard_three)
    flock_of_mallards.add(mallard_four)

    flock_of_ducks.add(flock_of_mallards)

    print('\nDuck Simulator: With Observer')
    quackologist: Quackologist = Quackologist()
    flock_of_ducks.register_observer(quackologist)

    simulate(flock_of_ducks)

    print(f'The ducks quacked {QuackCounter.number_of_quacks} times')


def main():
    duck_factory: AbstractDuckFactory = CountingDuckFactory()
    simulation(duck_factory)


if __name__ == '__main__':
    main()
