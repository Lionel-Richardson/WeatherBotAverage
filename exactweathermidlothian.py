from bs4 import BeautifulSoup
import requests
import time

while True:
    try:
        def get_weather():
            temps = []

            html_text = requests.get(
                "https://weather.com/weather/today/l/2d7ddcd5bcb306eb395707b513d91ff9601ca1fb230431b3946fb889247f2a7f").text
            soup = BeautifulSoup(html_text, "lxml")
            weather = soup.find("div", class_= "CurrentConditions--CurrentConditions--1swR9")
            temperature_weather_channel = weather.find("span", class_= "CurrentConditions--tempValue--3a50n").text
            temps.append(int(temperature_weather_channel[0:-1]))

            html_text = requests.get(
                "https://www.wunderground.com/dashboard/pws/KVAMIDLO74?cm_ven=localwx_pwsdash").text
            soup = BeautifulSoup(html_text, "lxml")
            temperature_wunderground = soup.find("span", class_="wu-value wu-value-to").text
            temps.append(float(temperature_wunderground))

            html_text = requests.get(
                "https://forecast.weather.gov/MapClick.php?CityName=Midlothian&state=VA&site=AKQ&textField1=37.5025&textField2=-77.6398&e=0").text
            soup = BeautifulSoup(html_text, "lxml")
            temperature_noaa = soup.find("p", class_="myforecast-current-lrg").text
            noaa_conditions = soup.find("p", class_="myforecast-current").text
            temps.append(int(temperature_noaa[0:-2]))

            html_text = requests.get(
                "https://www.localconditions.com/weather-midlothian-virginia/23112/").text
            soup = BeautifulSoup(html_text, "lxml")
            temperature_local = soup.find("p", class_="row-stat-value").text
            value = (temperature_local.split(" ")[0:-1])
            for i in value:
                updated_value = i[0:-2]
            temps.append(int(updated_value))

            sum_temps = 0
            for temperatures in temps:
                sum_temps = sum_temps + temperatures

            average = sum_temps / 4
            true_average = round(average)

            # placeholder

            payload = {
                "content": f"""
                            Current average temperature in Midlothian:
                            
                            **{true_average} degrees Fahrenheit**
                            {noaa_conditions}
                            
                            Sources: *Weather Channel, Wunderground, NOAA, Local Conditions*
                            
                            Next update in 15 minutes...
                            """
            }

            header = {
                "authorization": "placeholder"
            }
            r = requests.post("placeholder", data=payload, headers=header)


        if __name__ == "__main__":
            while True:
                get_weather()
                time_wait = 900
                time.sleep(time_wait)


    except AttributeError:
        print("Trying again...")
        get_weather()
