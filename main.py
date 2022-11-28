# imports

from flask import Flask


from utils import load_candidates, get_all, get_by_pk, get_by_skill


# variables
source = "candidates.json"


app = Flask(__name__)

@app.route("/")
def main_page():
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


app.run()
