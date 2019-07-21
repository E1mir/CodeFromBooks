def countdown(i):
    print(i)
    if i <= 1:
        return
    countdown(i - 1)


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


countdown(5)

print(fact(10))
