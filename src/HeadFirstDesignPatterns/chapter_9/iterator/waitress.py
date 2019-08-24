from typing import Iterator

from HeadFirstDesignPatterns.chapter_9.iterator.menus import Menu
from HeadFirstDesignPatterns.chapter_9.iterator.models import MenuItem


class Waitress(object):
    def __init__(self, pancake_house_menu: Menu, diner_menu: Menu, cafe_menu: Menu):
        self.pancake_house_menu = pancake_house_menu
        self.diner_menu = diner_menu
        self.cafe_menu = cafe_menu

    def print_all_menus(self) -> None:
        pancake_iterator: Iterator[MenuItem] = self.pancake_house_menu.create_iterator()
        diner_iterator: Iterator[MenuItem] = self.diner_menu.create_iterator()
        cafe_iterator: Iterator[MenuItem] = self.cafe_menu.create_iterator()
        print("MENU\n----\nBREAKFAST")
        self.print_menu(pancake_iterator)
        print("\nLUNCH")
        self.print_menu(diner_iterator)
        print("\nDINNER")
        self.print_menu(cafe_iterator)

    def print_all_vegetarian_menu(self) -> None:
        print("\nVEGETARIAN MENU\n---------------")
        self.print_vegetarian_menu(self.pancake_house_menu.create_iterator())
        self.print_vegetarian_menu(self.diner_menu.create_iterator())
        self.print_vegetarian_menu(self.cafe_menu.create_iterator())

    def is_item_vegetarian(self, name: str) -> bool:
        pancake_iterator = self.pancake_house_menu.create_iterator()
        if self.is_vegetarian(name, pancake_iterator):
            return True

        diner_iterator = self.diner_menu.create_iterator()
        if self.is_vegetarian(name, diner_iterator):
            return True

        cafe_iterator = self.cafe_menu.create_iterator()
        if self.is_vegetarian(name, cafe_iterator):
            return True

    @staticmethod
    def print_menu(iterator: Iterator[MenuItem]) -> None:
        for item in iterator:
            print(item)

    @staticmethod
    def print_vegetarian_menu(iterator: Iterator[MenuItem]) -> None:
        for item in iterator:
            if item.is_vegetarian:
                print(item)

    @staticmethod
    def is_vegetarian(name: str, iterator: Iterator[MenuItem]) -> bool:
        for item in iterator:
            if item.name == name and item.is_vegetarian:
                return True
        return False
