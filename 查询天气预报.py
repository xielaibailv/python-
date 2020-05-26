import urllib.request
import json
import pickle

f = open('city.pickle','rb')
city = pickle.load(f)

temp = input("请输入城市：")
code = city[temp]
file = urllib.request.urlopen('http://m.weather.com.cn/mweather/' + code + '.shtml' )
weatherhtml = file.read()
weatherjson = json.JSONDecoder().decode(weatherhtml)
# weatherjson = json.loads(weatherhtml)
weatherinfo = weatherjson['weatherinfo']

print('城市：',weatherinfo[city])
print('时间：',weatherinfo['time'])
print('星期：',weatherinfo['week'])
print('天气：',weatherinfo['dayWeatherDes'])
print('风向：',weatherinfo['dayWindDirection'])
print('风力：',weatherinfo['dayWindPower'])
print('经度：',weatherinfo['lat'])
print('纬度：',weatherinfo['lon'])

#json那里出了问题，报错