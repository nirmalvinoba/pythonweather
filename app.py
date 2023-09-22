# from flask import Flask,render_template,request

# import requests

# app = Flask(__name__)

# api_key = '57cce3ca9b0832ec8156006f028b7d86'

# @app.route('/', methods = ["GET","POST"])
# def home():
#     if request.method == "POST":
#         city = request.form.get("name")
#         weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
#         data=weather_data.json()
#         return render_template ("index.html",temp=data.get("main").get("temp"),feels=data.get("main").get("feels_like"),pressure=data.get("main").get("pressure"),humidity=data.get('main').get("humidity"),wind=data.get("wind").get("speed"),name=data.get("name"),sunrise=data.get("sys").get("sunrise"),sunset=data.get("sys").get("sunset"),clouds=data.get("weather")[0].get("description"))
#     return render_template ("index.html")

# if __name__ == "__main__":
#     app.run(debug=True ,port=5005)
from flask import Flask,render_template,request
import requests
app = Flask(__name__)

api_key = '57cce3ca9b0832ec8156006f028b7d86'



@app.route('/', methods = ["GET","POST"])
def main():
    if request.method == "POST":
        city = request.form.get("city")
        weather_data = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

        temp = weather_data.json().get("main").get("temp")
        humi = weather_data.json().get("main").get("humidity")
        wind = weather_data.json().get("wind").get("speed")
        cityname = weather_data.json().get("name")
        sunrise = weather_data.json().get("sys").get("sunrise")
        sunset = weather_data.json().get("sys").get("sunset")
        pressure = weather_data.json().get("main").get("pressure")
        clouds = weather_data.json().get("weather")[0].get("description")

        return render_template ("index.html", box = temp, bag = humi, pen = wind, pencil = cityname,
                                rise = sunrise, set = sunset, press = pressure, clo = clouds)
    return render_template ("index.html")


if __name__ == "__main__":
    app.run(debug=True)