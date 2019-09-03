from typing import List

from HeadFirstDesignPatterns.chapter_12.mvc_pattern.model import Person


def show_all_view(person_list: List[Person]):
    print(f'In our db we have {len(person_list)} users. Here they are:')
    for person in person_list:
        print(person.name)


def start_view():
    print('MVC - the simplest example')
    print('Do you want to see everyone in my db?[y/n]')


def end_view():
    print('Goodbye!')
