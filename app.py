import requests
import os 
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
api_key = os.getenv("API_KEY")

#print(api_key)

city_name = input("Enter your city name\n")


complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

response = requests.get(complete_url)

if response.status_code==200:
  data = response.json()
  print(f"------Please find below details of your city {city_name} --------")
  print(" Temperature (in kelvin unit): ", data['main']['temp'])
  print("Weather: ", data['weather'][0]['description'])
  sunset = datetime.fromtimestamp(data['sys']['sunset'])
  print("Sunset in your city : ",sunset)
elif response.status_code==400:
  print("oh oo! city not found")  
elif response.status_code==401:
  print("Invalid API")
else:
  print("Unknown error ")    



# print(data['weather'][0]['description'])
# print(data['main']['temp'])
# sunrise = (data['sys']['sunset']) # it will return unix timestamps, we need to convert it to understand.

# sunrise = datetime.fromtimestamp(sunrise)
# print(sunrise.strftime("%I:%M %p"))


# if data.get("cod")==200:
#   print("Valid city:", data["name"])
# else:
#   print("Error: ", data.get("message"))  

