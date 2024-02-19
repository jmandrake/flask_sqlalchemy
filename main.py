from website import create_app
from flask import Flask, request, jsonify, render_template, url_for, redirect

app = create_app()

# @app.route('/test/<name>')
# def index(name):
#     return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True) # debug=True allows for saved changes to be seen without restarting the server