from waitress import serve
from dae import app

serve(app, host='0.0.0.0', port=8080)
