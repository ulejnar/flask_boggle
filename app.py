from flask import Flask, request, render_template, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

@app.route('/')
def show_home_page():
    """ Show game board """

    session["board"] = boggle_game.make_board()

    return render_template("board.html",board=session["board"])

@app.route('/make-guess')
def make_guess():
    """ Checks guess and responds with JSON result """

    guess = request.args['guess']
    result = boggle_game.check_valid_word(session["board"], guess)
    
    response = {"result": result}

    return jsonify(response)

