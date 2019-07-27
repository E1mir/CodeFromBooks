from HeadFirstDesignPatterns.chapter_3.beverages import Espresso, DarkRoast, HouseBlend
from HeadFirstDesignPatterns.chapter_3.decorators import Mocha, Whip, Soy

if __name__ == '__main__':
    beverage = Espresso()
    beverage.display()

    beverage = Mocha(beverage)
    beverage = Soy(beverage)
    beverage.display()

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    beverage2.display()

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    beverage3.display()
