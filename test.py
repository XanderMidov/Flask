from flask import Flask, request, make_response, redirect, abort, render_template
from flask_script import Manager
import random
app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    weaponry = {'sword': 'Dark Blade',
                'dagger': 'Pirate Dirk',
                'staff': 'Light Rod',
                'hammer': 'Holy Crusher'}
    return render_template('user.html', name=name, weaponry=weaponry)

@app.route('/<param>')
def test(param):
    if param == 'Jopa':
        body = '''<ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            </ul>'''
    elif param == 'UserAgent':
            agent = request.headers.get('User-Agent')
            some_shit = 'Some shit'
            body = '''
            <h1>%s</h1>
            <h1>%s</h1>
            ''' % (agent, some_shit)
    body2 = 'Jopas'
    return body, 400

@app.route('/Res')
def response_test():
    response = make_response('<h1>This document carries a cookie</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/Red')
def redirect_test():
    return redirect('http://yandex.ru')

@app.route('/abort/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user['name']

def load_user(id):
    id = random.randint(1, 10)
    if id == 5:
        user = {'name': 'Rednaskel'}
    else:
        user = False
    return user

if __name__ == '__main__':
    app.run(debug=True)
    # manager.run()