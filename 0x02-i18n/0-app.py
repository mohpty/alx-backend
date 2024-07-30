#!/usr/bin/python3
'''
task 0
'''

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    '''
    server the index page
    '''

    return render_template('index.html')
