from urllib import request
import requests
import easygui


url = 'http://wenzhou_manager.dev.enesource.com/platform/login'
headers = {'Content-Type':'application/json;charset=UTF-8', 'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
data = {'userName':'TSKJ', 'password':'Aa123456'}
response = request.urlopen(url=url,data=data)

# response = requests.post(url, headers=headers, data=data)
