from flask import Flask
from flask_googlemaps import GoogleMaps, Map

app = Flask(__name__)
GoogleMaps(app)
app.config["DATABASE"] = 'mydb.db'


from app import views,models
