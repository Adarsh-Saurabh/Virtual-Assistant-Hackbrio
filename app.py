from flask import Flask, render_template

app = Flask(__name__)

@app.route("/helloWorld")
def hello():
    return "Hello World!"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/todo")
def todo():
    return render_template("todo.html")
    
if __name__ == "__main__":
    app.run(debug=True)