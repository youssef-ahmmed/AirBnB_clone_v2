#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False

data = storage.all(State)


@app.route('/states_list')
def states():
    """"""
    name_id_pairs = [(value["name"], value["id"]) for value in data.values()]
    name_id_pairs.sort(key=lambda name: name[0])
    return render_template('7-states_list.html',
                           name_id_pairs=name_id_pairs)


@app.teardown_appcontext
def terminate():
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
