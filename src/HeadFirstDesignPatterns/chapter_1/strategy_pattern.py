from HeadFirstDesignPatterns.chapter_1.behaviors import FlyRocketPowered
from HeadFirstDesignPatterns.chapter_1.models import Duck, MallardDuck, ModelDuck


def main():
    mallard_duck: Duck = MallardDuck()
    mallard_duck.display()
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()

    duck: Duck = ModelDuck()
    duck.perform_fly()
    duck.fly_behavior = FlyRocketPowered()
    duck.perform_fly()


if __name__ == "__main__":
    main()
