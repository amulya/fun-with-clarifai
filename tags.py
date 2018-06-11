from clarifai.rest import ClarifaiApp

app = ClarifaiApp()

def get_relevant_tags(image_url):
	response_data = app.tag_urls([image_url])
	
	tag_urls = []
	for concept in response_data['outputs'][0]['data']['concepts']:
		tag_urls.append(concept['name'])

	return tag_urls
n = '\n'
link = 'https://imagesvc.timeincapp.com/v3/mm/image?url=http%3A%2F%2Fimg1.cookinglight.timeinc.net%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Fmedium_2x%2Fpublic%2F1516896485%2Fchicken-paella-ck-1803.jpg%3Fitok%3DBK5uGeSC&w=1600&q=70'

print(n.join(get_relevant_tags(link)))
