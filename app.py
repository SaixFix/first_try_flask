from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def page_index():
    return candidates


@app.route("/candidates/<uid>")
def page_candidates(uid):
    return get_by_pk(uid)


@app.route("/skills/<uid>")
def page_skills(uid):
    return get_by_skill(list_candidates, uid)


app.run()
