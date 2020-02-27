from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,  SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User
from flask_babel import lazy_gettext as _l


class LoginForm(FlaskForm):
    username = StringField(_l('Логин'), validators = [DataRequired()])
    password = PasswordField(_l('Пароль'), validators = [DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class RegistrationForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегестрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError('Используйте другое имя пользователя')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Этот e-mail уже занят.') 

class EditProfileForm(FlaskForm):
    username = StringField('Имя пользователя', validators = [DataRequired()])
    about_me = TextAreaField('О себе', validators=[Length(min=0, max=140)])
    submit = SubmitField('Изменить')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.') 
class PostForm(FlaskForm):
    post = TextAreaField('Расскажи что-нибудь', validators= [DataRequired(), Length(min = 1, max = 140)])
    submit = SubmitField('Отправить')

class ResetPaswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Восстановить пароль')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Введите новый пароль', validators=[DataRequired()])
    password2 = PasswordField(
        'Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Сброс пароля')