word = "bottles"
for beer_num in range(99, 00, -1):
    print("{} {} of beer on the wall".format(beer_num, word))
    print("{} {} of beer.".format(beer_num, word))
    print("Take one down.")
    print("Pass it around.")
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print("{} {} of beer on the wall".format(new_num, word))
    print()
