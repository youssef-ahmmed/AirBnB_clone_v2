#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template, redirect, url_for

from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

data = storage.all("State")


@app.route('/states')
def states():
    """Get all state data"""
    return render_template("9-states.html",
                           states=data)


@app.route('/states/<id>')
def states_by_id(id):
    obj = None
    for state in data.values():
        if state.id == id:
            obj = state
            return render_template("9-states.html",
                                   id=id, state=obj)
    return "<h1>Not Found</h1>", 404


@app.teardown_appcontext
def terminate(exc):
    """Close SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
