from flask import Flask, request
from flask import json
from flask.json import jsonify
from flask import render_template
app = Flask(__name__)
import json
import requests

token = open("tokenfile","r").read()

@app.route('/',methods=['GET'])
def index():
	channel = request.args.get('channel', '')

	r = requests.get(f"https://discord.com/api/channels/{channel}/messages",headers={"Authorization":token})

	messages = json.loads(r.text)

	output = ""
	for x in messages:
		output += f"<p>{x['author']['username']}<br>{x['content']}</p>"

	return output
