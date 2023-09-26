import os

basedir = os.environ.get('FLASK_APP')


class Config():
  FLASK_APP = os.environ.get('FLASK_APP')
  FLASK_DEBUG = os.environ.get('FLASK_DEBUG')