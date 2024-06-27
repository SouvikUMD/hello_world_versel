# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:56:03 2024

@author: prama
"""


from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)