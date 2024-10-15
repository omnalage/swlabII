from flask import Flask, render_template, request
import googlemaps

app = Flask(__name__)

# Initialize Google Maps client with your API key
API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'  # Replace with your API key
gmaps = googlemaps.Client(key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_directions', methods=['POST'])
def get_directions():
    origin = request.form['origin']
    destination = request.form['destination']
    
    # Get directions
    directions = gmaps.directions(origin, destination)
    return {'directions': directions}

@app.route('/geocode', methods=['POST'])
def geocode():
    address = request.form['address']
    
    # Geocode the address
    geocode_result = gmaps.geocode(address)
    return {'geocode_result': geocode_result}

@app.route('/places', methods=['POST'])
def places():
    location = request.form['location']
    
    # Find nearby places
    places_result = gmaps.places_nearby(location=location, radius=1000)
    return {'places_result': places_result}

if __name__ == '__main__':
    app.run(debug=True)