from flask import *

app = Flask(__name__)


todoList = []
@app.route("/")
def home():
    return render_template("index.html", todos = todoList)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo']
    todoList.append({'task': todo, 'done': False})
    return redirect(url_for("home"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    edittodo = todoList[index]
    if request.method == "POST":
        editedtask = request.form["todo"]
        edittodo['task'] = editedtask
        print(index)
        return redirect(url_for("home"))
    else:
        return render_template("edit.html", edittodo=edittodo, index=index)
    
@app.route("/check/<int:index>")
def check(index):
    todoList[index]['done'] = not todoList[index]['done']
    return redirect(url_for("home"))

@app.route("/delete/<int:index>")
def delete(index):
    print(index)
    del todoList[index]
    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)
