from HeadFirstDesignPatterns.chapter_8.template_method import Tea, Coffee
from HeadFirstDesignPatterns.chapter_8.template_method_with_hook import TeaWithHook, CoffeeWithHook

if __name__ == '__main__':
    tea = Tea()
    coffee = Coffee()

    print('\nMaking tea...')
    tea.prepare_recipe()

    print('\nMaking coffee...')
    coffee.prepare_recipe()

    tea_hook = TeaWithHook()
    coffee_hook = CoffeeWithHook()

    print('\nMaking tea...')
    tea_hook.prepare_recipe()

    print('\nMaking coffee...')
    coffee_hook.prepare_recipe()
