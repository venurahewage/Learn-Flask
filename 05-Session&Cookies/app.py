from flask import *


app = Flask(__name__)
app.secret_key = "1010"


@app.route("/")
def home():
    return render_template("index.html", message="Index")

@app.route("/set")
def setdata():
    session['name'] = "Jhon"
    session['city'] = "NYC"

    return render_template("index.html", message="Session Data Set.")

@app.route("/get")
def getdata():
    name = session['name']
    city = session['city']

    return render_template("index.html", message=f"Name: {name}, City: {city}")

@app.route("/clear")
def clear():
    session.clear()
    return render_template("index.html", message="Session Cleared..!")


if __name__ == "__main__":
    app.run(debug=True)
