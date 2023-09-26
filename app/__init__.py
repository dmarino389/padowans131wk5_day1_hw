from flask import Flask,  render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
  return 'Hello from flask'


@app.route('/html')
def index_html():
  html_people = ['Pop Smoke', 'Passenger', 'Eminem', 'Kevin Gates', 'Drake']
  return render_template('index.html', people = html_people)



