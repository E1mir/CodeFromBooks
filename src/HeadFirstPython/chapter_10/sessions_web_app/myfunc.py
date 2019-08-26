def myfunc(*args) -> None:
    for a in args:
        print(a, end=' ')
    if args:
        print()


def myfunc2(**kwargs) -> None:
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()


def myfunc3(*args, **kwargs) -> None:
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()


if __name__ == '__main__':
    print('---- myfunc f-on ----')
    myfunc(10)
    myfunc()
    myfunc(10, 20, 30, 40, 50, 60, 70)
    myfunc(1, 'two', 3, 'four', 5, 'six', 7)

    values = [1, 2, 3, 5, 7, 11]
    myfunc(values)
    myfunc(*values)
    print('---- myfunc2 f-on ----')
    myfunc2(a=10, b=20)
    myfunc2()
    myfunc2(a=10, b=20, c=30, d=40, e=50, f=60)
    print('---- myfunc3 f-on ----')
    myfunc3()
    myfunc3(1, 2, 3)
    myfunc3(a=10, b=20, c=30)
    myfunc3(1, 2, 3, a=10, b=20, c=30)
