import os
import json
from flask import Flask, jsonify, render_template, request,redirect


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button', methods=['POST','GET'])
def button():
    if request.method=='POST':
        startdate=request.form['startdate']
        enddate=request.form['enddate']
        return render_template('button.html',startdate=startdate,enddate=enddate)


    return render_template('index.html')  
        

if __name__ == '__main__':
   app.run(debug=True)