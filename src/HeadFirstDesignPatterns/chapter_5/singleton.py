class Singleton(type):
    """
    Singleton metaclass
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class ChocolateBoiler(metaclass=Singleton):

    def __init__(self):
        self._empty: bool = True
        self._boiled: bool = False

    @property
    def is_empty(self) -> bool:
        return self._empty

    @property
    def is_boiled(self) -> bool:
        return self._boiled

    def fill(self) -> None:
        if self.is_empty:
            self._empty = False
            self._boiled = False

    def drain(self) -> None:
        if not self.is_empty and self.is_boiled:
            self._empty = True

    def boil(self) -> None:
        if not self.is_empty and not self.is_boiled:
            self._boiled = True

    def __str__(self) -> str:
        return f'Empty: {self.is_empty}\nBoiled: {self.is_boiled}'


if __name__ == '__main__':
    boiler_1 = ChocolateBoiler()
    boiler_1.fill()
    boiler_1.boil()
    boiler_1.drain()

    boiler_2 = ChocolateBoiler()

    assert boiler_1 is boiler_2
