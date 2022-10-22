import json, sys
sys.path.append('modules')
from flask import Flask, request, Response
import requests
import webbrowser

map_app = Flask(__name__)

player_url = 'http://localhost:420/players'
master_url = 'http://localhost:420/master'

def update_map_file(player_map):
    map_file = open('mapData.json', 'w')
    map_file.write(json.dumps(player_map))
    map_file.close()

def load_map_file():
    map_file = open('mapData.json', 'r')
    map_data = map_file.read()
    map_file.close()
    return map_data

@map_app.route('/master')
def dm_index():
    master_html_file = open('static/master.html')
    master_html = master_html_file.read()
    master_html_file.close()
    return Response(master_html, mimetype='text/html', status=200)

@map_app.route('/players')
def player_index():
    player_map_file = open('static/player_map.html')
    player_map = player_map_file.read()
    player_map_file.close()
    return Response(player_map, mimetype='text/html', status=200)

@map_app.route('/loadMap')
def load_map():
    return Response(load_map_file(), mimetype='application/json', status=200)

@map_app.route('/uploadScaleFactor', methods=['POST'])
def parse_scale_factor():
    current_map_data = json.loads(load_map_file())
    scale_factor = request.form['scaleFactor']
    current_map_data['scaleFactor'] = scale_factor
    update_map_file(current_map_data)
    return Response('OK', mimetype='text/html', status=200)

@map_app.route('/uploadURL', methods=['POST'])
def parse_url():
    current_map_data = json.loads(load_map_file())
    image_URL = request.form['URL']
    current_map_data['mapImage'] = image_URL
    update_map_file(current_map_data)
    return Response('OK', mimetype='text/html', status=200)

@map_app.route('/uploadFile', methods=['POST'])
def parse_image():
    current_map_data = json.loads(load_map_file())
    image_file = request.form['file']
    current_map_data['mapImage'] = image_file
    update_map_file(current_map_data)
    return Response('OK', mimetype='text/html', status=200)

@map_app.route('/')
def index():
    player_map_file = open('static/player_map.html')
    player_map = player_map_file.read()
    player_map_file.close()
    return Response(player_map, mimetype='text/html', status=200)

@map_app.route('/styles.css')
def stylesheet():
    stylesheet_file = open('static/styles.css')
    stylesheet = stylesheet_file.read()
    stylesheet_file.close()
    return Response(stylesheet, mimetype='text/css', status=200)

@map_app.route('/favicon.ico')
def favicon():
    g = open('static/favicon.ico','rb')
    return Response(g, direct_passthrough=True, mimetype='image/x-icon')

@map_app.errorhandler(400)
def http_error(e):
    r = requests.get('https://http.cat/400')
    return Response(r, mimetype='image/jpeg', status=400)

@map_app.errorhandler(403)
def http_error(e):
    r = requests.get('https://http.cat/403')
    return Response(r, mimetype='image/jpeg', status=403)

@map_app.errorhandler(404)
def http_error(e):
    r = requests.get('https://http.cat/404')
    return Response(r, mimetype='image/jpeg', status=404)

@map_app.errorhandler(405)
def http_error(e):
    r = requests.get('https://http.cat/405')
    return Response(r, mimetype='image/jpeg', status=405)

@map_app.errorhandler(410)
def http_error(e):
    r = requests.get('https://http.cat/410')
    return Response(r, mimetype='image/jpeg', status=410)

@map_app.errorhandler(500)
def http_error(e):
    r = requests.get('https://http.cat/500')
    return Response(r, mimetype='image/jpeg', status=500)

if __name__ == '__main__':
    # If you want to run with specific info use host={ip}, port=80
    webbrowser.open_new(master_url)
    webbrowser.open_new(player_url)
    map_app.run(host='127.0.0.1', port=420)
