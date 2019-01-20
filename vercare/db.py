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