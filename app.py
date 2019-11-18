from flask import Flask, render_template, redirect, url_for, request
app=Flask(__name__)
from db import all_bike
import uuid

bike=[]



@app.route('/', methods=['POST'])
def post_bike():
    model=request.form.get('model')
    fee=request.form.get('fee')
    image=request.form.get('image')
    year=request.form.get('year')
    new={'model':model,'fee':fee,'image':image,'year':year,'_id':str(uuid.uuid4())}
    bike.append(new)
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('ex1.html',data=all_bike())

if __name__=='__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)

