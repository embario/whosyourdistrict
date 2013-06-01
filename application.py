from flask import Flask, render_template
from constants import *
app = Flask(__name__)
app.debug = False

@app.route("/")
def esri():
    return render_template(HOME)

if __name__ == "__main__":
    app.run()
