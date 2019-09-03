from HeadFirstDesignPatterns.chapter_12.mvc_pattern import view
from HeadFirstDesignPatterns.chapter_12.mvc_pattern.model import Person


def show_all() -> None:
    people_in_db = Person.get_all()
    return view.show_all_view(people_in_db)


def start() -> None:
    view.start_view()
    user_input = input()
    if user_input == 'y':
        return show_all()
    else:
        return view.end_view()


if __name__ == '__main__':
    # running controller function
    start()
