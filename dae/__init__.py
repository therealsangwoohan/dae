from flask import Flask

app = Flask(__name__)
app.secret_key = "aSecretKey"

from dae.views import calendar, deadline_crud, event_crud
