from typing import Iterator

from HeadFirstDesignPatterns.chapter_9.composite.custom_exception import UnsupportedOperationException
from HeadFirstDesignPatterns.chapter_9.composite.models import MenuComponent


class Waitress(object):
    def __init__(self, all_menus: MenuComponent):
        self.all_menus = all_menus

    def print_menu(self):
        self.all_menus.print()

    # TODO: Fix problem with CompositeIterator
    def print_vegetarian_menu(self):
        iterator: Iterator[MenuComponent] = self.all_menus.create_iterator()
        print('\nVEGETARIAN MENU\n----')

        # print(list(iterator))
        for component in iterator:
            try:
                if component.is_vegetarian:
                    component.print()
            except UnsupportedOperationException:
                pass
