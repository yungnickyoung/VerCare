import os
from flask import Flask, render_template, request

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

    @app.route('/keywords')
    def keywords():
        keywords = request.args.get('keywords').split()
        # maxNumResults = 0 # Table can hold no more than 10 results

        results_list = []

        if keywords:
            # a_result = { 'drg' = '...', 'desc' = '...' }
            # results_list.append(a_result)

            # Search table of DRG/Descriptions for descriptions containing keywords
            with open("static/drg_desc.csv") as f:
                f.readline()
                for line in f:
                    contains_keywords = True

                    line = line.split(',')
                    drg = line[0]
                    desc = line[1]

                    for word in keywords:
                        if word not in line[1]:
                            contains_keywords = False

                    if contains_keywords:
                        result = {'drg':line[0], 'desc':line[1] }
                        results_list.append(result)

        return render_template('keywords.html', table_info=results_list)

    from . import db
    db.init_app(app)

    return app