import requests


response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=c1ced8243a109e9b580be349c2c8b0b0")

data = response.json()

print(data)


