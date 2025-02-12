#imoort the required modules from flask
from flask import Flask, request, render_template
#import the mongo module
from pymongo import MongoClient
import os

#Connect to MongoDB Compass on my local PC
#cluster = MongoClient("mongodb://localhost:27017")  
#cluster = MongoClient("mongodb+srv://baas:1234@cluster0.ftqsy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") #To be used when port 27017 is opened on my PC

#Retrieve MongoDB URI from environment variables
mongo_uri = os.getenv('MONGO_URI')

#Connect to MongoDB Atlas using the URI
cluster = MongoClient(mongo_uri)

#Set up the DB and collection method 
db = cluster["db_test"]  #Connect to the db_test database
collection = db["users"]  #Connect to the users collection in db_test

#Initialize the Flask app
app = Flask(__name__)

#Define the route to handle GET and POST methods
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        Age = int(request.form.get("Age"))
        Gender = request.form.get("Gender")
        Total_Income = int(request.form.get("Total_Income")) 
        #Checking which expense categories are selected and getting the amounts
        if request.form.get("check_utilities"):
            Utilities = int(request.form.get("utilities"))
        else:
            Utilities = None    

        if request.form.get("check_entertainment"):
            Entertainment = int(request.form.get("entertainment"))
        else: 
            Entertainment = None

        if request.form.get("check_schoolfees"):
            SchoolFees = int(request.form.get("schoolfees"))
        else:
            SchoolFees = None

        if request.form.get("check_shopping"):
            Shopping = int(request.form.get("shopping"))
        else:
            Shopping = None

        if request.form.get("check_healthcare"):
            Healthcare = int(request.form.get("healthcare"))
        else:
            Healthcare = None
        #Create a dictionary of the data captured from the survey form
        data_dictionary = {"Age": Age, "Gender": Gender, "Total_Income": Total_Income,"Expenses": {"Utilities": Utilities,"Entertainment": Entertainment,"SchoolFees": SchoolFees,"Shopping": Shopping,"Healthcare": Healthcare}}
        #print(data_dictionary) 
        #Insert the data into MongoDB
        collection.insert_one(data_dictionary)

    return render_template("index.html")  #Return the HTML form for the user

#Used to run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
