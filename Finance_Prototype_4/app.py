from flask import Flask, render_template
import nump as np

import sklearn
app = Flask(__name__)
@app.route('/')
def site():
    return render_template('layout.html')

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/getdata/')
def getdata(filename):



if __name__=='__main__':
    app.run(debug=True)