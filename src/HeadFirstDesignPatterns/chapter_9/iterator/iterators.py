import collections.abc
from typing import List

from HeadFirstDesignPatterns.chapter_9.iterator.models import MenuItem


class DinerMenuIterator(collections.abc.Iterator):

    def __init__(self, menu_items_list: List[MenuItem]):
        self.list = menu_items_list
        self.position = 0

    def __next__(self) -> MenuItem:
        if self.position >= len(self.list) or self.list[self.position] is None:
            raise StopIteration
        else:
            menu_item = self.list[self.position]
            self.position += 1
            return menu_item
