from dae import app
from dae.core import sevenDaysOfTheWeek, getDays
from flask import render_template, request, session


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["startingWeek"] = int(request.form["startingWeek"])
        session["endingWeek"] = int(request.form["endingWeek"])

    if not ("startingWeek" in session or "endingWeek" in session):
        session["startingWeek"] = 0
        session["endingWeek"] = 0

    return render_template("calendar.html",
                           sevenDaysOfTheWeek=sevenDaysOfTheWeek,
                           displayedDays=getDays(session["startingWeek"],
                                                 session["endingWeek"]),
                           startWeek=session["startingWeek"])
