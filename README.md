# Requirements needed

```
click==7.1.2
dnspython==1.16.0
Flask==1.1.2
itsdangerous==1.1.0
pymongo==3.10.1
python-dotenv==0.13.0
Werkzeug==1.0.1
```

* `pip3 install flask`
* `pip3 install pymongo` -- to use Mongo DB
* `pip3 install dnspython` -- allows us to connect to Mongo with just the URL
* `pip3 install python-dotenv` -- allows the use of `.env` files for environment variables

## How to use requirements.txt
```
pip3 install -r requirements.txt
```

# Todos
What fields or information do we want to track for each Todos
* Task name
* Due date
* Whether it is done
* Comment

# SESSION KEYS
Generated from https://randomkeygen.com/

# Flash messages
1. See documentation (different class for errors) https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/
2. Ensure sessions are enabled -> we have to make sure 
`app.secret_key` has been set
3. In the `layout.template.html` add in the code to display the flash messages


# Restful API Review
* Post - create new data
* Put - modify existing data by replacing the old entirely with new
* Patch - modify existing data by changing one aspect of the old data
* Delete - delete existing data
* Get - fetch data