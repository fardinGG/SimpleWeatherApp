from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            api_key = "80ae0e7e07b181cb53d42f61b50a0871"  # Replace with your OpenWeatherMap API key
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather = {
                    "city": data["name"],
                    "country": data["sys"]["country"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "current_date": datetime.now().strftime("%Y-%m-%d")
                }
                weather_data = weather

    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
