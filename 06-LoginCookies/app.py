from flask import *

app = Flask(__name__)
app.secret_key = "1010"


@app.route("/")
def home():

    try:
        uname = request.cookies['user']
        pasw = request.cookies['pswd']

        if (uname == uname) and (pasw == pasw):
            return render_template("profile.html", message="Logged in")
        else:
            return render_template("index.html", message="Username or Password Incorrect")


    except:
        pass

    return render_template("index.html")



@app.route("/login", methods=["POST"])
def login():

    if request.method == "POST":
        user = request.form.get('username')
        pswd = request.form.get('password')

        if user and pswd:
            session['uname'] = user
            try:
                uname = request.cookies['user']
                pasw = request.cookies['pswd']

                if (uname == user) and (pasw == pswd):
                    
                    return render_template("profile.html", message=f"Logged in to {session['uname']}")
                else:
                    return render_template("index.html", message="Username or Password Incorrect")


            except:
                resp = make_response(render_template("profile.html", message=f"Logged in to {session['uname']}"))
                resp.set_cookie("user", user)
                resp.set_cookie("pswd", pswd)
                return resp
            
        else:
            return render_template("index.html", message="Please Complete")


    return render_template("index.html", message="Please Login")

@app.route("/clear")
def clear():
    resp = make_response(render_template("index.html", message="Removed Cookies"))
    resp.set_cookie('user', expires=0)
    resp.set_cookie('pswd', expires=0)
    session.clear()
    return resp

@app.route("/myorders")
def myorders():
    username = session['uname']
    return render_template("orders.html", prof=username)



if __name__ == "__main__":
    app.run(debug=True)
