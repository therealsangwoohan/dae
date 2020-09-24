from bson import ObjectId
from dae import app
from dae.database import deadlines
from flask import redirect, request


@app.route("/add_deadline/", methods=["POST"])
def addDeadline():
    deadlines.insert_one({
        "date": request.form["date"],
        "endTime": request.form["endTime"],
        "project": request.form["project"],
        "title": request.form["title"],
        "description": request.form["description"]
    })
    return redirect("/")


@app.route("/deadlines/<deadlineId>/edit/", methods=["POST"])
def editDeadline(deadlineId):
    aFilter = {"_id": ObjectId(deadlineId)}
    anUpdate = {"$set": {"date": request.form["date"],
                         "endTime": request.form["endTime"],
                         "project": request.form["project"],
                         "title": request.form["title"],
                         "description": request.form["description"]}}
    deadlines.update_one(aFilter, anUpdate)
    return redirect("/")


@app.route("/deadlines/<deadlineId>/delete/", methods=["POST"])
def deleteDeadline(deadlineId):
    deadlines.delete_one({"_id": ObjectId(deadlineId)})
    return redirect("/")
