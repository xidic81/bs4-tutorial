import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.7627488405625e-5,"date":"Mon, 24 Aug 2020 12:00:01 GMT","inverseRate":14786.886568995},"eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":5.7307894625793e-5,"date":"Mon, 24 Aug 2020 12:00:01 GMT","inverseRate":17449.60282575}}

print(json_data)

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])
