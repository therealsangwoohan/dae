from bson import ObjectId

from dae import app
from dae.database import events
from flask import redirect, request


@app.route("/add_event/", methods=["POST"])
def addEvent():
    events.insert_one({
        "date": request.form["date"],
        "startTime": request.form["startTime"],
        "endTime": request.form["endTime"],
        "project": request.form["project"],
        "title": request.form["title"],
        "description": request.form["description"]
    })
    return redirect("/")


@app.route("/events/<eventId>/edit/", methods=["POST"])
def editEvent(eventId):
    aFilter = {"_id": ObjectId(eventId)}
    anUpdate = {"$set": {"date": request.form["date"],
                         "startTime": request.form["startTime"],
                         "endTime": request.form["endTime"],
                         "project": request.form["project"],
                         "title": request.form["title"],
                         "description": request.form["description"]}}
    events.update_one(aFilter, anUpdate)
    return redirect("/")


@app.route("/events/<eventId>/delete/", methods=["POST"])
def eventDeadline(eventId):
    events.delete_one({"_id": ObjectId(eventId)})
    return redirect("/")
