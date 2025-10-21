from flask import Flask, render_template, session, redirect, url_for
from models import Challenge, Alchemy, Hacker, Team, Event
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect
from sqlmodel import create_engine, Session
import redis
import os
import uuid
from pyfiglet import Figlet


load_dotenv('.env')
app = Flask(__name__)
app.config['REDIS_URL='] = os.environ.get('REDIS_URL')
app.config['REDIS_PORT'] = os.environ.get('REDIS_PORT')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
csrf = CSRFProtect(app)
db_engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
redis_cl = redis.Redis(host='localhost', port=6380, db=0, decode_responses=True)


def ascii_art_text():
    hackerboard_text = 'H a c k e r b o a r d'
    figlet_font = Figlet(font="banner3-D", width=400)
    return figlet_font.renderText(hackerboard_text)

@app.route('/')
def home():
    return render_template('index.html', ascii_art_text=ascii_art_text())

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    #sign in
    return render_template('hello.html', ascii_art_text=ascii_art_text())

@app.route('/hello-again')
def hello_again():
    return render_template('hello-again.html', ascii_art_text=ascii_art_text())

@app.route('/goodbye')
def goodbye():
    pass

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/teams')
def teams():
    pass

@app.route('/team/<team_name>')
def team(team_name):
    pass

@app.route('/join/team/<team_name>')
def join_team():
    pass

@app.route('/team/<team_name>/invite', methods=['GET', 'POST'])
def team_invitation():
    pass

@app.route('/events')
def events():
    pass

@app.route('/event/<event_id>')
def event(event_id):
    pass

@app.route('/join/event/<event_id>')
def join_event(event_id):
    pass

@app.route('/hackers')
def hackers():
    pass

@app.route('/hacker/<handle>')
def hacker(handle):
    pass

@app.route('/challenges')
def challenges():
    pass

@app.route('/challenge/<challenge_number>')
def challenge():
    pass

@app.route('/submit/challenge/<challenge_number>', methods=['POST'])
def submit_challenge(challenge_number):
    pass

@app.route('/change/challenge/<challenge_number>', methods=['GET', 'POST'])
def change_challenge(challenge_number):
    pass

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html', ascii_art_text=ascii_art_text())

if __name__ == '__main__':
    app.run(debug=True)
