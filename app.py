from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

@app.route('/')
def show_home_page():
    """ Show the home page """
    
    return "Hello"
