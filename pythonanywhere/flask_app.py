
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

comments = []

app.config["DEBUG"] = True

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))
