# set up and dependencies
from scrape_mars import scrape
import os
from Flask import Flask, jsonify
import pymongo

# set up connections to Mongo Database
# CONN = os.getenv("CONN")
# client = pymongo.MongoClient(CONN)
# db = client.mars
# db.students.drop()

app = Flask(__name__)

@app.route("/")
def main():
    return 

@app.route("/scrape")
def scrape_route():
    db.mars.insert_many(scrape(driver))