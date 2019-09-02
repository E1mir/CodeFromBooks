from HeadFirstDesignPatterns.chapter_12.mvc_pattern import view
from HeadFirstDesignPatterns.chapter_12.mvc_pattern.model import Person


def show_all():
    # gets list of all Person objects
    people_in_db = Person.get_all()
    # calls view
    return view.show_all_view(people_in_db)


def start():
    view.start_view()
    user_input = input()
    if user_input == 'y':
        return show_all()
    else:
        return view.end_view()


if __name__ == '__main__':
    # running controller function
    start()
