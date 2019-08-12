from flask import Flask, render_template, request, escape

from HeadFirstPython.chapter_4.vsearch import search4letters

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    import mysql.connector
    DB_CONF = {
        'host': '127.0.0.1',
        'user': 'vsearch',
        'password': 'vsearchpasswd',
        'database': 'vsearchlogDB',
    }
    connection = mysql.connector.connect(**DB_CONF)
    _SQL = """INSERT INTO log
                (phrase, letters, ip, browser_string, results) VALUES 
                (%s, %s, %s, %s, %s)"""
    cursor = connection.cursor()
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res,))
    connection.commit()
    cursor.close()
    connection.close()


# @app.route('/')
# def hello() -> '302':
#     return redirect('/entry')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results, )


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results',)
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents, )


# @app.route('/viewlog')
# def view_the_log() -> str:
#     contents = []
#     with open('vsearch.log') as log:
#         for line in log:
#             contents.append([])
#             for item in line.split('|'):
#                 contents[-1].append(escape(item))
#     return str(contents)


@app.route('/')
@app.route('/entry')
def entry() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!'
                           )


if __name__ == '__main__':
    app.run(debug=True)
