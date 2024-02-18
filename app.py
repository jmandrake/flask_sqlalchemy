from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/test/<name>')
def index(name):
    return render_template('index.html', name=name)