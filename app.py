import json
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

# Creating a model for notes
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    text = db.Column(db.Text)

    def __init__(self, title, text):
        self.title = title
        self.text = text

@app.route("/helloWorld")
def hello():
    return "Hello World!"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/todo")
def todo():

    allTodos = Note.query.all()
    return render_template("todo.html", allTodos=allTodos)

@app.route("/todo/add", methods=["POST"])
def addTodo():

    if request.method == "POST":
        Data = request.get_json()
        title = Data["title"]
        text = Data["text"]

        newTodo = Note(title, text)
        db.session.add(newTodo)
        db.session.commit()

        flash("Record was added successfully")
        return redirect("/todo")


@app.route("/todo/delete/<int:id>", methods=["POST"])
def deleteTodo():

    if request.method == "POST":
        todo = Note.query.get_or_404(request.data["id"])
        db.session.delete(todo)
        db.session.commit()

        flash("Record was deleted successfully")
        return redirect(url_for("todo"))

@app.route("/todo/update/<int:id>", methods=["POST"])
def updateTodo():

    if request.method == "POST":
        todo = Note.query.get_or_404(request.data["id"])
        todo.title = request.form["title"]
        todo.text = request.form["text"]
        db.session.commit()

        flash("Record was updated successfully")
        return redirect(url_for("todo"))

@app.route("/openApp")
def openApp():
    name = request.json()["name"]
    name = name.replace(".", "")
    os.system("start " + name)
    return redirect(url_for("index"))



@app.route('/cal')
def cal():
    return render_template('cal.html')


# Running the app
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)