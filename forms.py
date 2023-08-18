from wtforms import Form, StringField, DecimalField, IntegerField, TextAreaField, PasswordField, validators 

class RegisterForm(Form):
    name= StringField('Full Name', [validators.Length(min=1,max=50)])
    username= StringField('Username', [validators.Length(min=4,max=25)])
    email= PasswordField('Password', [validators.Length(min=6,max=50)])
    password= StringField('Full Name', [validators.DataRequired(),validators.EqualTo('confirm',message='Password do not match')])
    confirm=PasswordField('Confirm Password')
