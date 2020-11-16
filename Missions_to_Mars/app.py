# set up and dependencies
from scrape_mars import scrape
import os
from flask import Flask, render_template
import pymongo

# set up connections to Mongo Database
CONN = os.getenv("CONN")
client = pymongo.MongoClient(CONN)
db = client.mars

db.mars.drop()

app = Flask(__name__)

@app.route("/")
def main():
    return "The app is up!"


#     for result in db.mars.find():
#         results.append({key: value for key, value in result.items()})
#     return render_template("index.html", mars_dict=results)

@app.route("/scrape")
def scrape_route():
    db.mars.insert_many(scrape())
    return "Successfully scraped webpages!"


if __name__ == "__main__":
    app.run(debug=True)