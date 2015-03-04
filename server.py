import os
import sys
sys.path.append(str(os.path.realpath(__file__)).replace('/server.py',''))



import requests
import json
from flask import Flask, render_template, request, Response, stream_with_context
from sticker.clustering import clustering_by_words_frequency

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	print request.args.get('keyword')
	if request.args.get('keyword') == "" or request.args.get('keyword') == None:
		return render_template('index.html')
	else:
		clustering_by_words_frequency.search(request.args.get('keyword'))
		return render_template('data5.html')



@app.route('/data1')
def data1():
	if request.args.get('keyword') == "" or request.args.get('keyword') == None:
		return render_template('data1.html')
	else:
		clustering_by_words_frequency.search(request.args.get('keyword'))
		return render_template('data1.html')

@app.route('/data2')
def data2():
	if request.args.get('keyword') == "" or request.args.get('keyword') == None:
		return render_template('data2.html')
	else:
		clustering_by_words_frequency.search(request.args.get('keyword'))
		return render_template('data2.html')

@app.route('/data3')
def data3():
	if request.args.get('keyword') == "" or request.args.get('keyword') == None:
		return render_template('data3.html')
	else:
		clustering_by_words_frequency.search(request.args.get('keyword'))
		return render_template('data3.html')

@app.route('/data4')
def data4():
	if request.args.get('keyword') == "" or request.args.get('keyword') == None:
		return render_template('data4.html')
	else:
		clustering_by_words_frequency.search(request.args.get('keyword'))
		return render_template('data4.html')

@app.route('/data5')
def data5():
	if request.args.get('keyword') == "" or request.args.get('keyword') == None:
		return render_template('data5.html')
	else:
		clustering_by_words_frequency.search(request.args.get('keyword'))
		return render_template('data5.html')



if __name__ == "__main__":
	# Get host/port from the Bluemix environment, or default to local
	HOST_NAME = os.getenv("VCAP_APP_HOST", "127.0.0.1")
	PORT_NUMBER = int(os.getenv("VCAP_APP_PORT", "3000"))

	app.run(host=HOST_NAME, port=int(PORT_NUMBER), debug=True)

	# Start the server
	print("Listening on %s:%d" % (HOST_NAME, PORT_NUMBER))