import os

from flask import Flask, render_template, session

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

app = create_app()

@app.route('/', methods=['GET'])
def user():
    if "started" in session:
        print(session["started"])
        return render_template('user.html')
    else:
        return board()

@app.route('/board', methods=['GET'])
def board():
    if "started" in session:
        return render_template('board.html')
    else:
        return render_template('host.html')

@app.route('/host', methods=['GET'])
def host():
    session["started"] = 1
    print(session["started"])
    return {}


## we need to store
