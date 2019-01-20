import os
from flask import Flask, render_template

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'vercare.sqlite'),
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

    # a simple page that says hello
    @app.route('/home')
    def home():
        return render_template('home.html', title='Home')

    @app.route('/search')
    def search():
        return render_template('search.html', title='Search', drgCode='123', searchLoc='Gainesville, FL')

    @app.route('keywords')
    def keywords():
        keywords = request.args.get('keywords').split()
        maxNumResults = 0 # Table can hold no more than 10 results

        if keywords:
            # Search table of DRG/Descriptions for descriptions containing 

    from . import db
    db.init_app(app)

    return app