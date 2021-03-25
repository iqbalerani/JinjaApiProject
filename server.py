from flask import Flask, render_template
app = Flask(__name__)
import random
import datetime
import requests

Genderize_ENDPOINT = "https://api.genderize.io?"
Agify_ENDPOINT = "https://api.agify.io?"


@app.route('/')
def hello_world():
    current_year = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<username>')
def guess(username):
    location_endpoint = f"{Genderize_ENDPOINT}name="
    location_endpoint2 = f"{Agify_ENDPOINT}name="
    xy = requests.get(url=f"{location_endpoint}{username}")
    gender_data = xy.json()
    yearage = requests.get(url=f"{location_endpoint2}{username}")
    year_data = yearage.json()
    return render_template("guess.html", name=username, gender=gender_data, year=year_data)


if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)