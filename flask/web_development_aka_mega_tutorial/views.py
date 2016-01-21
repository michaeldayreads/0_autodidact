from flask import Flask
from flask import render_template
app = Flask(__name__)

#from here its the same as tutorial

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Michael'} #fake user
	posts = [
			{	'author': {'nickname': 'Jack'},
				'body': 'Lovely day in Boulder!'
			},
			{	'author': {'nickname': 'Jill'},
				'body': 'Bleh, too cold!'
			},
	]
	return render_template('index.html', title='Home',user=user,posts=posts)
