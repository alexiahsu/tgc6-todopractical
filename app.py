from flask import Flask, render_template, request, redirect, url_for
import pymongo
from dotenv import load_dotenv
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

@app.route('/')
def home():
    return "Welcome home"

# FOR "C" in CRUD
## One route to show the form and ask the user to type in
## One route to process the form (extract the data) & send to database

### Show form
@app.route('/tasks/create')
def show_create_form():
    return render_template('create_task.template.html')

### Process form (extract data) and write into mongo db
@app.route('/tasks/create', methods=["POST"])
def create_task():
    task_name = request.form.get('task-name')
    due_date = request.form.get('due-date')
    comments = request.form.get('comments')

    client[DB_NAME].todos.insert_one({
        'task_name': task_name,
        'due_date': datetime.datetime.strptime(due_date, "%Y-%m-%d"),
        'comments': comments
    })

    return "Task created successfully!"

#### By default, date is stored as string
#### use datetime.datetime.strptime()



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)