from flask import Flask, render_template, jsonify, request, g
from constants import *
from uscensus_api import USCensus_API_CD
app = Flask(__name__)
app.debug = True

@app.before_request
def before_request():
    g.usc = USCensus_API_CD()

@app.route("/")
def esri():
    return render_template(HTML_HOME)

@app.route("/data/pop/total", methods=['GET'])
def data_pop_total():
    usc = g.usc
    state = request.args.get('state')
    district = request.args.get('district')
    usc = USCensus_API_CD()
    return jsonify(usc.getPopTotal(state, district))

@app.route("/data/pop/sex", methods=['GET'])
def data_pop_sex():
    usc = g.usc
    state = request.args.get('state')
    district = request.args.get('district')
    return jsonify(usc.getPopSex(state, district))

if __name__ == "__main__":
    app.run()
