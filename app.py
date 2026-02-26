from flask import *
import pymysql
import os
# initialize flask

app=Flask(__name__)
if not os.path.exists("static/images"):
    os.makedirs("static/images")

app.config["UPLOAD FOLDER"]="static/images"
@app.route("/api/signup",methods=["POST"])
def signup():
    # request user input
    username=request.form["username"]
    email=request.form["email"]
    password=request.form["password"]
    phone=request.form["phone"]


    # create connection to database
    connection=pymysql.connect(host="localhost",user="root",password="",database="tembo_sokogarden_lewie")

    # create a cursor 
    cursor=connection.cursor()

    # create sql statement to insert the data
    sql="insert into users(username,email,password,phone)values(%s,%s,%s,%s)"
    # prepare the data
    data=(username,email,password,phone)


    # excecute / run
    cursor.execute(sql,data)

    #commit/save
    connection.commit()

    # response 
    return jsonify ({"Message":"Thank you for joining"})

# sign in api

# Sign in route/endpoint
@app.route("/api/signin",methods=["POST"])


#  define  function
def signin():
    # request user input 
    email=request.form["email"]
    password=request.form["password"]
    
    # create a conection
    connection=pymysql.connect(host="localhost",user="root",password="",database="tembo_sokogarden_lewie")

    # create a cursor
    cursor=connection.cursor(pymysql.cursors.DictCursor)

    # sql statement to check if user exists
    sql="select*from users where email=%s and password=%s"

    # prepare data 
    data=(email,password)

    cursor.execute(sql,data)

    # response
    if cursor.rowcount==0:
        return jsonify({"Message":"Login failed"})
    else:
        user=cursor.fetchone()
        user.pop("password",None)
        return jsonify({"Message":"Login success","user":user})

# add product api
# create product route
@app.route("/api/add_product",methods=["POST"])


# create function
def add_product():
    # request user input
    product_name=request.form["product_name"]
    product_description=request.form["product_description"]
    product_cost=request.form["product_cost"]
    product_photo=request.files["product_photo"]

    # extract image name
    filename=product_photo.filename

    photo_path=os.path.join(app.config["UPLOAD FOLDER"],filename)

    product_photo.save(photo_path)

    # create connection
    connection=pymysql.connect(host="localhost",user="root",password="",database="tembo_sokogarden_lewie")

    # create a cursor
    cursor=connection.cursor()

    # sql statement to insert the records
    sql="insert into product_details(product_name,product_description,product_cost,product_photo)values(%s,%s,%s,%s)"

    # prepare data
    data=(product_name,product_description,product_cost,filename)

    # excecute/run
    cursor.execute(sql,data)

    # commit/save
    connection.commit()

    # return response

    return jsonify({"Message":"Product added successfully"})




     






































app.run(debug=True)