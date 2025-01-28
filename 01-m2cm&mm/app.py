from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    m2cm = 0
    m2mm = 0
    fin = ""
    meters = 0

    if request.method == 'POST':

        if request.form['submit'] == "tocm":
        
            met = request.form.get('m')
            if met != "":
                meters = int(met)
                m2cm = meters * 100
            
            fin = str(meters)+" M Converted to : " + str(m2cm) + " cm"

        elif request.form['submit'] == "tomm":
        
            met = request.form.get('m')
            if met != "":
                meters = int(met)
                m2mm = meters * 1000
            
            fin = str(meters)+" M Converted to : " + str(m2mm) + " mm"

    return render_template("index.html", out = fin)


if __name__ == "__main__":
    app.run(debug=True)
