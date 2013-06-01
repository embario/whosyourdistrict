from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

@app.route("/")
def esri():
    return render_template("esri.html")

if __name__ == "__main__":
    app.run()