import collections.abc
from collections import deque
from typing import Iterator, Deque


class CompositeIterator(collections.abc.Iterator):

    def __init__(self, iterator: Iterator):
        self.stack: Deque[Iterator] = deque()
        # iterator with menu items
        self.stack.append(iterator)

    def __next__(self):
        if len(self.stack) == 0:
            raise StopIteration
        iterator: Iterator = self.stack.pop()
        # component = iterator
        for component in iterator:
            if component:
                c_i = component.create_iterator()
                print(c_i)
                self.stack.append(c_i)
        pass
        # if component:
        #     c_iter = component.create_iterator()
        #     print(c_iter)
        #     self.stack.append(c_iter)
        #     return component
        # else:
        #     self.stack.pop()
        #     return next(self)


class NoneIterator(collections.abc.Iterator):
    def __next__(self):
        return None
