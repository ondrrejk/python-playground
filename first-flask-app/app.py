from flask import Flask, render_template
# import Flask and render_template from the "flask" library on your local machine
# render_template = a helper that loads HTML files from a folder called templates
# flask automatically looks for HTML files inside a folder named templates/

app = Flask(__name__) # creates the flask app
# __name__ tells Flask where to look for things like templates and static files
# When you run the app directly (python app.py), Python sets __name__ to "__main__" because this file is the main program.
# IF you run the app as a module, ex.: import app, Python sets __name__ == "app".
## Flask uses __name__ to:
# - locate your templates/ folder
# - locate your static/ folder
# - know how to build paths relative to your project
# - help with debugging and error messages
# If you renamed your file, __name__ would automatically update, so Flask always knows the correct location.


# Basic route
@app.route("/")
# This tells Flask: “When someone visits the root URL (/), run the home() function.”
def home():
    return render_template("index.html")
    # Flask loads templates/index.html and sends it to the browser

# Another example route
@app.route("/hello/<name>") # This is a dynamic route
# <name> is a variable taken from the URL
def hello(name):
    return f"Hello, {name}!"
# ex.: http://localhost:5000/hello/John
# flask will run: hello("John")
# and return: Hello, John!

if __name__ == "__main__":
    app.run(debug=True)
# This block ensures the app only runs when you execute the file directly.
# debug=True enables:
# - automatic reload when you change code
# - helpful error messages
# You can also specify:
# - host: specifies the hostname to listen on (ex.: host="0.0.0.0" to make the server publicly available)
# - port: sets the port number for the server (default is 5000)

# REAL WORLD USE EXAMPLE:
# Imagine you have a script called "mymath.py":
# ---
#   def add(a, b):
#       return a + b
#   print(add(2, 3))
# ---
# If someone imports this file:
# ---
#   import mymath
# ---
# It would print 5, which is annoying.
# So Python programmers wrap executable code like this:
# ---
#   def add(a, b):
#       return a + b
#   if __name__ == "__main__":
#       print(add(2, 3))
# ---
# Now the print only runs when the file is executed directly.