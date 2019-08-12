class CountFromBy:
    def __init__(self, v: int = 0, i: int = 1):
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)

    def __str__(self) -> str:
        return f'Value: {self.val}, Increment: {self.incr}'


if __name__ == '__main__':
    a = CountFromBy(100, 15)
    print(a)
    a.increase()
    a.increase()
    print(a)
