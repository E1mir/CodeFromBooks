def show_all_view(lst):
    print('In our db we have %i users. Here they are:' % len(lst))
    for item in lst:
        print(item.name)


def start_view():
    print('MVC - the simplest example')
    print('Do you want to see everyone in my db?[y/n]')


def end_view():
    print('Goodbye!')
