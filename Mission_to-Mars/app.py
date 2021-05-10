# MongoDb and Flask Application

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Flask Setup

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# ##########################
# Flask Routes
# ##########################

# Root Route to Query MongoDB and pass Mars data into the html
# template called index.html which will display the data on the screen.


@app.route("/")
def index():
    mars_record = mongo.db.mars.find_one()
    # print(mars_record)
    return render_template("index.html", mars=mars_record)

# Scrape Route function to Import scrape_mars.py`


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    print(mars_data)
    mars.replace_one({}, mars_data, upsert=True)
    # Redirect back to home page
    return redirect("/")


# This standard and un blocks of code only if the program is the main
# program executed.
#
if __name__ == "__main__":
    app.run()
