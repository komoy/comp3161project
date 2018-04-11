from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, DateField,SubmitField, ValidationError
from wtforms.validators import InputRequired, DataRequired, EqualTo


from ..models import UserProfile

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit=SubmitField('Login')

class UserForm(FlaskForm):
    
    """ For users to create new account """
    
    first_name= StringField("FirstName",validators=[InputRequired()])
    last_name= StringField("LastName",validators=[InputRequired()])
    username= StringField("UserName",validators=[InputRequired()])
    DOB= DateField('DOB', format='%m-%d-%Y')
    gender=SelectField('Gender', choices=[('Male', 'Male'),('Female','Female'),('PREFER NOT DISCLOSE',' None')])
    meal_preference= StringField("Meal Preference",validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(),EqualTo('confirm_password')],)
    confirm_password=PasswordField('Confirm Password')
    submit= SubmitField('Register')
    
    
    def validate_username(self, field):
        if UserProfile.query.filter_by(username=field.data).first():
            raise ValidationError('Username has already been taken.')