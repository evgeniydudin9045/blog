import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ADMINS = ['evgeniydudin9045@gmail.com']

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT= 587
    MAIL_USERNAME= 'evgeniydudin9045@gmail.com'
    MAIL_PASSWORD= 'Rmfc9045'
    MAIL_USE_TLS= True
    MAIL_USE_SSL= False
    ADMINS = ['evgeniydudin9045@gmail.com']

    POSTS_PER_PAGE = 25

    LANGUAGES = ['ru' , 'en']



    