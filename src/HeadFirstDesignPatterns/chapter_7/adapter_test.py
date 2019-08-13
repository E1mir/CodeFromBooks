from HeadFirstDesignPatterns.chapter_7.adapter.adapters import TurkeyAdapter, DuckAdapter
from HeadFirstDesignPatterns.chapter_7.adapter.birds import MallardDuck, WildTurkey, Duck, Turkey


def test_duck(target_duck: Duck):
    target_duck.quack()
    target_duck.fly()


def test_turkey(target_turkey: Turkey):
    target_turkey.gobble()
    target_turkey.fly()


if __name__ == '__main__':
    duck: Duck = MallardDuck()
    turkey: Turkey = WildTurkey()
    turkey_adapter: Duck = TurkeyAdapter(turkey)
    duck_adapter: Turkey = DuckAdapter(duck)

    print('The Turkey says...')
    test_turkey(turkey)
    print('\nThe Duck says...')
    test_duck(duck)
    print('\nThe TurkeyAdapter says...')
    test_duck(turkey_adapter)
    print('\nThe DuckAdapter says...')
    test_turkey(duck_adapter)
