from flask import *

# initialize your flask app
app=Flask(__name__)


# define the route 
@app.route("/api/home")

def home():
    return jsonify({'Message':"Welcome to API" })

# create route for products
@app.route("/api/product")
def product():
    return jsonify({"Message":"Welcome to product Api"})

# define route
@app.route("/api/services")
def services():
    return jsonify({"Message":"Welcome to Our services API"})

# creating a route to upgrade user input
@app.route("/api/calc",methods={'POST'})
def calc():
    num1=request.form["num1"]
    num2=request.form["num2"]

    SUM=int(num1)+int(num2)
    return jsonify({"Answer":SUM})

# multiply two numbers
@app.route("/api/multiply",methods={"POST"})
def mult():
    num1=request.form["num1"]
    num2=request.form["num2"]

    product=int(num1)*int(num2)
    return jsonify({"Answer":product})

app.run(debug=True)


