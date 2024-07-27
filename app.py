# Import class Flask from flask library
# Import request method to make HTTP requests to a server
from flask import Flask,request

# (__name__) = "__main__"
app = Flask(__name__)

# default method is GET if none is passed.
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about")
def about():
    return "Some info about me"

@app.route("/contact")
def contact_us():
    return "My contact details are 0238 283 283"


# List of dictionaries combined in a list, this is a JSON file.
# Variable 'courses' is a global variable because it has been defined outside the function scope.
courses = [
    {
        "code": 101,
        "Name": "Diploma of IT",
        "duration": "1.5 years"
    },
    {
        "code": 102,
        "Name": "Diploma of Web Dev",
        "duration": "1.5 years"
    },
    {
        "code": 103,
        "Name": "Diploma of Data science",
        "duration": "2 years"
    },
      {
        "code": 104,
        "Name": "Bachelor of IT",
        "duration": "3 years"
    },
    {
        "code": 105,
        "Name": "Bachelor of Web Dev",
        "duration": "3 years"
    },
    {
        "code": 106,
        "Name": "Bachelor of Data science",
        "duration": "3 years"
    },
]

# Making a HTTP request for the server 
@app.route("/courses")
def list_courses():
    limit = request.args.get("limit")
    if limit:
        return courses[0:int(limit)] # make sure you wrap limit in INT
    return courses

# Fetching a specific course in the course list.
@app.route("/courses/101")
def get_course_101():
    return courses[0] # accessing course 101 by index

@app.route("/courses/102")
def get_course_102():
    return courses[0] 

# Creating a personalized message, returns in dictionary(JSON). Good idea to inform what type of error
@app.route("/courses/200")
def error_message():
    return {"error": "Course does not exist"}, 404


# POST request, add a new course. Define method in the parameter
@app.route("/courses", methods = ["POST"])
def add_course():
    body = request.get_json() # This is retrieving the value of json file and storing in 'body'
    courses.append(body) # Adding new data to json file
    return courses


# DELETE request, delete a course
@app.route("/courses/107", methods= ["DELETE"])
def delete_course_107():
    del courses[-1] # use del method to delete and -1 to access last element in the list
    return {"Message": "Course 107 has been successfully deleted"}


# PUT request: Updating an entire course
@app.route("/courses/107", methods=["PUT"])
def update_course_107():
    body = request.get_json()
    courses[-1] = body
    return courses[-1]

# PATCH request: Updating a specific value
# Fetch value from duration key and stores in courses first element (course 101).
@app.route("/courses/101", methods= ["PATCH"])
def patch_course_101():
    body = request.get_json()
    courses[0]["duration"] = body.get("duration") or courses[0]["duration"]
    courses[0]["Name"] = body.get("Name") or courses[0]["Name"]

    return courses[0]

# You can run this application in terminal
if __name__ == "__main__":
    app.run(debug=True)





# @app.route("/goodbye/")
# def goodbye_world():
#     return "<p>Goodbye, World!</p>"

# @app.route("/coder/")
# def coder():
#     return "<p>This web app was created in a class at Coder Academy.</p>"

# from flask import Flask
# from datetime import datetime

# app = Flask(__name__)

# @app.route("/current_time/")
# def hello_world():
#     return f"<p>{str(datetime.now().strftime('%H:%M'))}</p>"
    

