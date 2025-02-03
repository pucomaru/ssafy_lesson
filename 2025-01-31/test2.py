import requests
from pprint import pprint


# 서울의 위도
lat = 37.56
# 서울의 경도
lon = 126.97

#API KEY
key="0db51eebac77a9b126b18d8fafb19cdc"


# API 요청 URL
url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"

information=requests.get(url).json()

print(pprint(information))