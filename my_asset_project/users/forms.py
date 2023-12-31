from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError


from flask_login import current_user
from my_asset_project.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    office = StringField('Office', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired()])
    employee_id = StringField('Employee_Id', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Password must match!')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("Your email has been registered already!")
    

    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError("Your username has been registered already!")
        
    
