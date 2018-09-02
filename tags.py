#from flask import Flask, render_template, request
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import os
import collections

myApp = ClarifaiApp()
res=None
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

"""
def get_foodspo(files, links):
	fileDict = collections.OrderedDict()
	linkDict = collections.OrderedDict()

	for item in os.listdir(os.path.dirname('static/img/')):
		if item != '.DS_Store':
			fileDict[item] = myApp.inputs.search_by_image(filename=os.path.dirname(item))

	for i in links:
		linkDict[i] = myApp.inputs.search_by_image(url=item)

	for item in linkDict:
		fileDict[item] = linkDict[item]
	return fileDict
"""