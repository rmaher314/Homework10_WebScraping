from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Mission_to_Mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    mars_data = mongo.db.mars_data.find_one()
    return render_template('index.html', mars_data=mars_data)


@app.route("/scrape")
def scraper():
    mars_data = mongo.db.mars_data
    data = Mission_to_Mars.scrape()
    print("updating database")
    mars_data.update({}, data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
