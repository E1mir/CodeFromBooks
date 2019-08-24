from HeadFirstDesignPatterns.chapter_9.iterator.menus import PancakeHouseMenu, DinerMenu, CafeMenu
from HeadFirstDesignPatterns.chapter_9.iterator.waitress import Waitress

if __name__ == '__main__':
    pancake_house_menu = PancakeHouseMenu()
    diner_menu = DinerMenu()
    cafe_menu = CafeMenu()

    waitress = Waitress(pancake_house_menu, diner_menu, cafe_menu)

    waitress.print_all_menus()
    waitress.print_all_vegetarian_menu()

    print('\nCustomer asks, is the Hotdog vegetarian?')
    print('Waitress says: ', end='')
    if waitress.is_item_vegetarian('Hotdog'):
        print('Yes')
    else:
        print('No')

    print('\nCustomer asks, is the Waffles vegetarian?')
    print('Waitress says: ', end='')
    if waitress.is_item_vegetarian('Waffles'):
        print('Yes')
    else:
        print('No')
