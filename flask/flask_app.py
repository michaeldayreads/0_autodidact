from flask import Flask, redirect, render_template, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from kc import sqlalchemy_comments

app = Flask(__name__)
app.config["DEBUG"] = True

keys = sqlalchemy_comments() # dict

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(username=keys['username'], password=keys['password'], hostname=keys['hostname'], databasename=keys['databasename'],)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

db=SQLAlchemy(app)

class Comment(db.Model):
	"""Comment tutorial db Model"""
	__tablename__ = "comments"

	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(4096))

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=Comment.query.all())

    comment = Comment(content=request.form["contents"])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))
