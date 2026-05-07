from flask import Flask, render_template
from data import lessons

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", lessons=lessons)

@app.route("/lesson/<name>")
def lesson(name):
    lesson = lessons.get(name)
    return render_template("lesson.html", lesson=lesson)

if __name__ == "__main__":
    app.run(debug=True)
