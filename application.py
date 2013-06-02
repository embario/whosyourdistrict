from flask import Flask, render_template, jsonify, request
from constants import *
from uscensus_api import USCensus_API_CD
app = Flask(__name__)
app.debug = True


@app.route("/")
def esri():
    print("Called root endpoint")
    return render_template(HTML_HOME)

@app.route("/data/pop/total", methods=['GET'])
def data_pop_total():
    print("Called /data/pop/total endpoint")
    state = request.args.get('state')
    print("state = " + str(state))
    district = request.args.get('district')
    print("district = " + str(district))
    usc = USCensus_API_CD()
    return jsonify(usc.getPopTotal(state, district))

if __name__ == "__main__":
    app.run()
