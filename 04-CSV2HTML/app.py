from flask import *
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    out = pd.read_csv("Path/to/csv")
    return render_template("index.html", tables=[out.to_html()])


if __name__ == "__main__":
    app.run(debug=True)
