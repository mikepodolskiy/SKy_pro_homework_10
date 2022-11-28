# imports

from flask import Flask

from utils import get_all, get_by_pk, get_by_skill

# variables definition
source = "candidates.json"

# starting app
app = Flask(__name__)


@app.route("/")
def main_page():
    """
    routing for main page, showing all candidates in required format
    :return: all candidates data in required format
    """
    candidates = get_all(source)
    output = "<br>"
    for person in candidates:
        output += person["name"] + "<br>"
        output += person["position"] + "<br>"
        output += person["skills"] + "<br>"
        output += "<br>"
    return f"<pre> {output} <pre>"


@app.route("/candidates/<int:pk>")
def get_candidate(pk):
    """
    routing for candidates pages, showing more information about required person
    :param pk: single person pk
    :return: person's data in required format
    """
    person = get_by_pk(pk, source)
    if not person:
        return "Candidate not found"

    output = f"<img src=\"{person['picture']}\">"
    output += "<br>"
    output += person["name"] + "<br>"
    output += person["position"] + "<br>"
    output += person["gender"] + "<br>"
    output += str(person["age"]) + "<br>"
    output += person["skills"] + "<br>"
    output += "<br>"
    return f"<pre> {output} <pre>"


@app.route("/candidates/skills/<skill>")
def get_candidate_by_skill(skill):
    """
    routing for skill page, showing list of persons having required skill
    :param skill: required skill
    :return: persons having required skill in required format
    """
    candidates = get_by_skill(skill, source)
    output = "<br>"
    for person in candidates:
        output += person["name"] + "<br>"
        output += person["position"] + "<br>"
        output += person["gender"] + "<br>"
        output += str(person["age"]) + "<br>"
        output += person["skills"] + "<br>"
        output += "<br>"
    return f"<pre> {output} <pre>"


# launching app
app.run()
