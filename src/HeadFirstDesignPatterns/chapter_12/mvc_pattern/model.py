import json


class Person(object):
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def get_all(cls) -> list:
        filename = 'data/db.txt'
        try:
            database = open(filename, 'r')
        except FileNotFoundError:
            print(f'File {filename} not found!')
            return []
        except PermissionError:
            print('Access denied! You do not have permissions.')
            return []
        except Exception as err:
            print('Something went wrong:', str(err))
            return []
        result = []
        json_list = json.loads(database.read())
        for item in json_list:
            person = Person(item['first_name'], item['last_name'])
            result.append(person)
        return result

    def __str__(self) -> str:
        return f'{self.first_name} - {self.last_name}'
