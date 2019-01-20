import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
        db = sqlite3.connect(
            'static/verCareDB.db',
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        db.row_factory = sqlite3.Row

        return db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('static/verCareDB.db.sql') as f:
        db.executescript(f.read().decode('utf8'))

def init_app(app):
    app.teardown_appcontext(close_db)
    init_db()