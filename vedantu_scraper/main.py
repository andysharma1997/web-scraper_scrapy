import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from flask import Flask, request, Response

from vedantu_scraper.vedantu_scraper.spiders.vedbot import VedbotSpider


app = Flask(__name__)

@app.route("/get_site_scrape", methods=["POST", "GET"])
def site_scraper():
    start_url
