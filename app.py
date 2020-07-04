from flask import Flask, render_template, request, redirect, url_for, flash
import pymongo
from dotenv import load_dotenv
from bson import ObjectId
import os
import datetime

# load variables in the .env file in our operating system environment
load_dotenv()

app = Flask(__name__)

# Connect to mongodb
MONGO_URI = os.environ.get('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)

# Define db name
DB_NAME = "todolist"

# Read in the session_key variable from the operating system environment
SESSION_KEY = os.environ.get('SESSION_KEY')

# Set the session_key
app.secret_key = SESSION_KEY

# Home route
# Display all the tasks


@app.route('/')
def home():
    tasks = client[DB_NAME].todos.find()
    return render_template('home.template.html', tasks=tasks)

# FOR "C" in CRUD
# One route to show the form and ask the user to type in
# One route to process the form (extract the data) & send to database

# Show form


@app.route('/tasks/create')
def show_create_form():
    return render_template('create_task.template.html')

# Process form (extract data) and write into mongo db


@app.route('/tasks/create', methods=["POST"])
def create_task():
    task_name = request.form.get('task-name')
    due_date = request.form.get('due-date')
    comments = request.form.get('comments')

    client[DB_NAME].todos.insert_one({
        'task_name': task_name,
        'due_date': datetime.datetime.strptime(due_date, "%Y-%m-%d"),
        'comments': comments,
        'done': False
    })
    flash(f"New task '{task_name}' has been created")
    return redirect(url_for('home'))


@app.route('/tasks/check', methods=["PATCH"])
def check_task():
    task_id = request.json.get('task_id')
    task = client[DB_NAME].todos.find_one({
        "_id": ObjectId(task_id)
    })

    # there is a chance that task has no "done"
    # so if there is no key named "done", we just set "done" to False
    if task.get('done') is None:
        task['done'] = False

    client[DB_NAME].todos.update({
        "_id": ObjectId(task_id)
    }, {
        '$set': {
            'done': not task['done']
        }
    })
    # if we return a dictionary in Flask, flask will auto-convert to JSON
    return {
        "status": "OK"
    }
# By default, date is stored as string
# use datetime.datetime.strptime()


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
