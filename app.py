# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:56:03 2024

@author: prama
"""


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()