import dotenv
import os
from flask import Flask, render_template, request
from googleplaces import GooglePlaces

dotenv.load_dotenv()
gtoken = str(os.getenv("GTOKEN"))
flasktoken = str(os.getenv("FLASKTOKEN"))

app = Flask(__name__)
app.config['SECRET_KEY'] = flasktoken

@app.route('/', methods=["POST", "GET"])
def home():
    #form = LocationInputForm()
    if request.method == 'POST':
        location = request.form.get('location')
        print(location)
        keyword = request.form.get('type')
        return render_template("restaurants.html", foodType = keyword, userlocation = location)
    return render_template('home.html', name = "Home")

@app.route('/aboutMe')
def about():
    return render_template('aboutMe.html', name = "About")

@app.route('/resume')
def resume():
    return render_template('resumePage.html', name = "Resume")

if __name__ == '__main__':
    app.run(debug = True)
