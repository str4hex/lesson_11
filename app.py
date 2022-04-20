from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", candidate_all=load_candidates_from_json())


@app.route("/candidate/<int:id>")
def candidate(id):
    return render_template("single.html", candidate=get_candidate(id))

@app.route("/search/<candidate_name>")
def search(candidate_name):
    return render_template("search.html", search_candidate=get_candidates_by_name(candidate_name))


@app.route("/skill/<skill_name>")
def skill(skill_name):
    return render_template("skill.html", skill=get_candidates_by_skill(skill_name), skill_names=skill_name)


if __name__ == '__main__':
    app.run()
