from flask import Flask
from flask_task_one import taskone
from flask_task_two import tasktwo
from flask_task_three import taskthree


app = Flask(__name__)

app.register_blueprint(taskone)
app.register_blueprint(tasktwo)
app.register_blueprint(taskthree)
