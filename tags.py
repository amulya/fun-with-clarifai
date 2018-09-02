#from flask import Flask, render_template, request
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

myApp = ClarifaiApp()

def get_relevant_tags(image_url):

	response_data = myApp.tag_urls([image_url])
	
	tag_urls = []
	for concept in response_data['outputs'][0]['data']['concepts']:
		tag_urls.append(concept['name'])

	return tag_urls

def get_relevant_tags_file(image_url):
	
	response = myApp.tag_files([image_url])

	tag_urls = []
	for concept in response['outputs'][0]['data']['concepts']:
		tag_urls.append(concept['name'])

	return tag_urls
	#print(tags)
