from HeadFirstPython.chapter_9.DBcm import UseDatabase

if __name__ == '__main__':
    db_conf = {
        'host': '127.0.0.1',
        'user': 'vsearch',
        'password': 'vsearchpasswd',
        'database': 'vsearchlogDB',
    }

    with UseDatabase(db_conf) as cursor:
        _SQL = """show tables"""
        cursor.execute(_SQL)
        data = cursor.fetchall()
        print(data)
