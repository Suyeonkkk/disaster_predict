from urllib.parse import quote
import urllib.request as ul
import xmltodict
import json

# 서울 인천 대구 대전 부산 울산 광주 제주
location = quote("제주")

url = "http://openapi.forest.go.kr/openapi/service/trailInfoService/getforeststoryservice" \
    "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
    "&mntnAdd=" + location + \
    "&numOfRows=100"
request = ul.Request(url)
response = ul.urlopen(request)
rescode = response.getcode()
weather = [[]]
if (rescode == 200):
    responseData = response.read().decode("utf8")
    rD = xmltodict.parse(responseData)
    rDJ = json.dumps(rD)
    rDD = json.loads(rDJ)
    height = 0
    size = int(rDD['response']['body']['totalCount'])
    for i in range(0, size):
        if (rDD['response']['body']['items']['item'][i]['mntninfohght'] is None):
            height += 0
        else:
            height += int(rDD['response']['body']['items']['item'][i]['mntninfohght'])
    
    print(height)

heightList = [7969, 6153, 13230, 7922, 11715, 21346, 12644, 5202]