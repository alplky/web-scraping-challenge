# set up and dependencies
from scrape_mars import scrape
import os
from Flask import Flask, render_template
import pymongo

# set up connections to Mongo Database
# CONN = os.getenv("CONN")
# client = pymongo.MongoClient(CONN)
# db = client.mars
# db.mars.drop()

app = Flask(__name__)

@app.route("/")
def main():
    for result in db.mars.find():
        results.append({key: value for key, value in result.items()})
    return render_template("index.html", )

@app.route("/scrape")
def scrape_route():
    db.mars.insert_many(scrape(driver))
    return 