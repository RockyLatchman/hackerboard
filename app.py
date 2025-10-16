from flask import Flask, render_template, session, redirect, url_for
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect
import redis
import os


load_dotenv('.env')
app = Flask(__name__)
app.config['REDIS_URL='] = os.environ.get('REDIS_URL')
app.config['REDIS_PORT'] = os.environ.get('REDIS_PORT')
app.config['SECRET_KEY'] =os.environ.get('SECRET_KEY')
csrf = CSRFProtect(app)
redis_cl = redis.Redis(host='localhost', port=6380, db=0, decode_responses=True)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    #sign in
    return render_template('hello.html')

@app.route('/hello-again')
def hello_again():
    pass

@app.route('/goodbye')
def goodbye():
    pass

@app.route('/dashboard')
def dashboard():
    pass

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
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
