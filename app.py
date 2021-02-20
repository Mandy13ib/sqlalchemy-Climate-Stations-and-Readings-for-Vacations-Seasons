#import depend
from flask import Flask

#create an app
app = Flask(__name__)

#first index 
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my API!"

#/about
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "My Name is Mandy Farrell"

#/contact
@app.route("/contact")
def contact():
    print("Server received request for 'Contact' page...")
    return "I can be reached at mandy13ib@gmail.com"

if __name__ == "__main__":
    app.run(debug=True)
