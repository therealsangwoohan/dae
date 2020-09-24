from flask import Flask

app = Flask(__name__)

from dae.views import calendar, deadline_crud, event_crud
