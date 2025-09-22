from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'G&$^FWfbweg79b4'
bootstrap = Bootstrap(app)
moment = Moment(app)

def uoft_email_check(form, field):
    if field.errors:
        return
    if 'utoronto' not in field.data.lower():
        raise ValidationError('Please enter your UofT email')
class Form(FlaskForm):
    name = StringField('What is your name?', validators=[InputRequired()])
    email = StringField('What is your UofT email?', validators=[InputRequired(), Email(), uoft_email_check])
    submit = SubmitField('Submit')
    
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    email = None
    form = Form()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        form.name.data = ''
        form.email.data = ''
    return render_template('index.html', form=form, name=name, email=email, current_time=datetime.now())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)