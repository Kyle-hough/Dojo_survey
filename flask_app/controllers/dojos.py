from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    data = {
        "id" : session["survey_id"]
    }
    dojo = Dojo.get_one(data)
    return render_template('result.html' , dojo = dojo)


# Action -----------------------------------------------

@app.route('/process', methods=['POST'])
def create():
    if Dojo.validate_dojo(request.form):
        session["survey_id"] = Dojo.create(request.form)
        return redirect('/result')
    return redirect('/')