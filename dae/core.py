from datetime import date, timedelta, datetime
from dae.database import deadlines, events
from operator import itemgetter

sevenDaysOfTheWeek = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]


def getDays(startWeek, endWeek):
    todayDate = date.today()
    todayWeekDay = todayDate.weekday()
    curDate = todayDate - timedelta(days=todayWeekDay)
    for _ in range(startWeek):
        curDate += timedelta(days=7)

    displayedDays = []
    for _ in range(startWeek, endWeek + 1):
        aWeek = []
        for _ in range(7):
            aWeek.append(getDay(curDate))
            curDate += timedelta(days=1)
        displayedDays.append(aWeek)
    return displayedDays


def getDay(date):
    day = []

    es = events.find({"date": date.__str__()})
    targetedEvents = []
    for e in es:
        e["type"] = "event"
        targetedEvents.append(e)
    targetedEvents = sorted(targetedEvents, key=itemgetter("endTime"))

    ds = deadlines.find({"date": date.__str__()})
    targetedDeadlines = []
    for d in ds:
        d["type"] = "deadline"
        targetedDeadlines.append(d)
    targetedDeadlines = sorted(targetedDeadlines, key=itemgetter("endTime"))

    dIdx = eIdx = 0
    while dIdx < len(targetedDeadlines) and eIdx < len(targetedEvents):
        if targetedDeadlines[dIdx]["endTime"] < targetedEvents[eIdx]["endTime"]:
            day.append(targetedDeadlines[dIdx])
            dIdx += 1
        else:
            day.append(targetedEvents[eIdx])
            eIdx += 1

    day = day + targetedDeadlines[dIdx:] + targetedEvents[eIdx:]
    return day


def getDateFromString(stringDate):
    return datetime.strptime(stringDate, "%d/%m/%y").date()


def getTimeFromString(stringTime):
    return datetime.strptime(stringTime, "%H:%M").time()
