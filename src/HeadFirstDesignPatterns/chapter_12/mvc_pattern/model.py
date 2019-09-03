import json
from typing import List


class Person(object):
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def get_all(cls) -> List['Person']:
        filename = 'data/db.txt'
        try:
            with open(filename, 'r') as database:
                result: List[Person] = []
                json_list = json.loads(database.read())
                for item in json_list:
                    person = Person(item['first_name'], item['last_name'])
                    result.append(person)
                return result
        except FileNotFoundError:
            print(f'File {filename} not found!')
        except PermissionError:
            print('Access denied! You do not have permissions.')
        except Exception as err:
            print('Something went wrong:', str(err))
        return []

    def __str__(self) -> str:
        return f'{self.first_name} - {self.last_name}'
