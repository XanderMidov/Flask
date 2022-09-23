from flask import Flask, request, make_response, redirect, abort, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

class NameForm(Form):
    name = StringField('What is your fucking name?')
    submit = SubmitField('Submit')
    # radio = RadioField('Choose wisely', choices=['Dwarf', 'Human', 'Elf', 'Orc'])

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'hard to guess'
Bootstrap(app)
Moment(app)

@app.route('/')
def index():
    name = 'Jopin'
    return render_template('boot.html', name=name)

@app.route('/Form', methods=['GET', 'POST'])
def form_fun():
    name = None
    form = NameForm()
    # if form.validate():
    name = form.name.data
    form.name.data = ' '

    return render_template('form.html', form=form, name=name)

@app.route('/Moment')
def moment_fun():
    return render_template('moment.html', current_time=datetime.utcnow())

@app.route('/<name>')
def user_fun(name):
    form = NameForm()
    return render_template('boot.html', name=name, form=form)

@app.errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404

app.run(debug=True)

