import dotenv
import os
from flask import Flask, render_template, request
from googleplaces import GooglePlaces
import googlemaps
import time
import requests

dotenv.load_dotenv()
apiKey = str(os.getenv("APIKEY"))
flaskKey = str(os.getenv("FLASKTOKEN"))

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = flaskKey
gglObj = GooglePlaces(apiKey)
gmaps = googlemaps.Client(apiKey)

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        working = True
        location = request.form.get('location')
        type = request.form.get('type')

        businesses = []
        try:
            response = gmaps.places_nearby(
                location = location,
                keyword = type,
                name = 'food',
                radius = 10000,
            )
        except googlemaps.exceptions.ApiError:
                    
                    try:
                        params = {
                            'key': apiKey,
                            'address': location
                        }

                        base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
                        search = requests.get(base_url, params=params).json()
                        search.keys()

                        if search['status'] == 'OK':
                            geometry = search['results'][0]['geometry']
                            lat = geometry['location']['lat']
                            lng = geometry['location']['lng']
                            location = f'{lat}, {lng}'

                        response = gmaps.places_nearby(
                        location = location,
                        keyword = type,
                        name = 'food',
                        radius = 10000,
                        )

                    except googlemaps.exceptions.ApiError:
                         working = False
                         return render_template('home.html', name = "Home", failed = working)
                        
        businesses.extend(response.get('results'))
        next_page_token = response.get('next_page_token')

        while next_page_token:
            time.sleep(2)
            response = gmaps.places_nearby(
                location= location,
                keyword= type,
                name = 'food',
                radius= 10000,
                page_token = next_page_token
            )

            businesses.extend(response.get('results'))
            next_page_token = response.get('next_page_token')
        
        return render_template("restaurants.html", places = businesses, userLocation = location)
    return render_template('home.html', name = "Home")

@app.route('/aboutMe')
def about():
    return render_template('aboutMe.html', name = "About")

@app.route('/resume')
def resume():
    return render_template('resumePage.html', name = "Resume")

if __name__ == '__main__':
    app.run(debug = True)
