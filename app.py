from flask import *
import requests
import json

app = Flask(__name__)

api_key = "YOUR_API_KEY"

@app.route('/')
def home():
    return redirect(url_for('trending'))

@app.route('/historical_data')
def historical_data():
    return render_template('base.html')

@app.route('/historical_data', methods=['POST'])
def my_form_post1():
    stock_name = request.form['text']
    url = "https://indian-stock-exchange-api2.p.rapidapi.com/historical_data"

    querystring = {"stock_name":stock_name,"period":"1m","filter":"price"}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "indian-stock-exchange-api2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

@app.route('/trending')
def trending():
    url = "https://indian-stock-exchange-api2.p.rapidapi.com/trending"
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "indian-stock-exchange-api2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    return render_template('trending.html', context=response.json())

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')

