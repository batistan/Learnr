from flask import Flask

app = Flask(__name__)
app.config["DATABASE"] = 'mydb.db'


from app import views,models