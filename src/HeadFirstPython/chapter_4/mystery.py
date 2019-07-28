def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After:', arg)


def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)


def my_custom(arg: int):
    arg = arg.to_bytes(2, byteorder='little')
    print(arg)


if __name__ == '__main__':
    a = 5
    my_custom(a)
    print(a)
