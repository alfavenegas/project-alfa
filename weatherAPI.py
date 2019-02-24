import requests

print('******** WEATHER ********')
city=str(input("Please enter a city name\n"))

payload = {'q': '{}'.format(city), 'units': 'metric', 'APPID': '734825ddb56ff066587c21326dd47d41'}
r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
response = r.json()

if response['cod']=='404':
	print('\n',response['message'],'\n')
else:
	print('\nWeather in {0},{1}\n'.format(response['name'],response['sys']['country']))
	print('{} °C'.format(response['main']['temp']))
	print('{}\n'.format(response['weather'][0]['main']))
