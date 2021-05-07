from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url='https://redplanetscience.com/'
browser.visit(url)
html = browser.html
new_soup = soup(html, 'html.parser')
 
time.sleep(1)

# Create an instance of Flask
app = Flask(__name__)


------------------------  REVISIT  ------------------------

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", vacation=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    costa_data = scrape_costa.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, costa_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
