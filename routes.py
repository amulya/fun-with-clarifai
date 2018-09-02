from flask import Flask, request, render_template, url_for, redirect
import tags
from werkzeug import secure_filename
import os
from algoliasearch import algoliasearch

app = Flask(__name__)

myLinks = []

@app.route('/', methods=['GET', 'POST'])
def index():
	n = '\n'
	link = None
	tagsList = []
	if request.method == 'POST' and 'useLink' in request.form:
		link = request.form.get('link') #'https://imagesvc.timeincapp.com/v3/mm/image?url=http%3A%2F%2Fimg1.cookinglight.timeinc.net%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Fmedium_2x%2Fpublic%2F1516896485%2Fchicken-paella-ck-1803.jpg%3Fitok%3DBK5uGeSC&w=1600&q=70'

		myLinks.append(link) # add to record of img links used
		
		tagsList = tags.get_relevant_tags(link)
		return render_template(('recipes.html'), tagsList=tagsList, link=link)
	
	elif request.method == 'POST' and 'uploadImg' in request.form:
		# use uploaded image
		f = request.files['photo']
		sfname = str(os.path.join('static/img/',str(secure_filename(f.filename))))
		f.save(sfname)
		tagsList = tags.get_relevant_tags_file(sfname)
		return render_template(('recipes.html'), tagsList=tagsList, link=sfname)
	return render_template('index.html')

@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
	return render_template('recipes.html', tagsList=tagsList, link=link)

@app.route('/prep', methods=['GET', 'POST'])
def prep():
	pathNames = []
	for filename in os.listdir(os.path.dirname('static/img/')):
		pathNames.append(filename)

	return render_template('prep.html', myLinks=myLinks,pathNames=pathNames)

@app.route('/foodspo', methods=['GET', 'POST'])
def foodspo():
	return render_template('foodspo.html')

if __name__=='__main__':
	app.run(debug=True)