import requests

api_key ='a58492cf6bc59ba298d7abca076a783c'

user_input =input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
if weather_data.json()['cod'] == '404':
    print("NO City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round (weather_data.json()['main']['temp'])

    print(f"The weather in{user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp} °F") 