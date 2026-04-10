import requests
api_key = "YOUR_API_KEY"
city = input("Enter city: ")
url = "https://api.openweathermap.org/data/2.5/weather"
full_url = url + "?q=" + city + "&appid=" + api_key
response = requests.get(full_url)
data = response.json()
weather = data["weather"][0]["description"]
temp_kelvin = data["main"]["temp"]
temp_celsius = temp_kelvin - 273.15
print("Weather:", weather)
print("Temperature:", round(temp_celsius, 2), "C")