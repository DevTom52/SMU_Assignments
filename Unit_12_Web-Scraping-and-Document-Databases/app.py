from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# render index.html and find documentments 
@app.route("/")
def home(): 

    # Find data
    mars_data = mongo.db.mars_data.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_data)


@app.route('/scrape')
def scrape():

    mars_info = mongo.db.mars_info


if __name__ == "__main__":
    app.run(debug=True)