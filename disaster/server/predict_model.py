import urllib.request as ul
import xmltodict
import json
import datetime as dt
import timedelta as td
import numpy as np

# Snow
# 지점 코드 (default: 대전)
# 서울 108 인천 112 대구 143 대전 133 부산 159 울산 152 광주 156 제주도 184 

locationCode = 133
url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=20120101" \
      "&endDt=20140101" \
      "&stnIds=" + str(locationCode)
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

weather = [[]]
size = 0
date = 0

if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음

    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    size = int(rDD['response']['body']['totalCount'])
    weather = [[0] * 14] * (size)
    date = dt.datetime(2012, 1, 1).date()

    weather[0] = ['date', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
    for index in range(1, size):
        try:
            avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
            # avgTa 평균 기온
        except TypeError:
            avgTa = -99

        try:
            minTa = rDD['response']['body']['items']['item'][index]['minTa']
            # minTa 최저 기온
        except TypeError:
            minTa = -99

        try:
            maxTa = rDD['response']['body']['items']['item'][index]['maxTa']
            # maxTa 최고 기온
        except TypeError:
            maxTa = -99

        try:
            avgTd = rDD['response']['body']['items']['item'][index]['avgTd']
            # avgTd 평균 이슬점온도
        except TypeError:
            avgTd = -99

        try:
            minRhm = rDD['response']['body']['items']['item'][index]['minRhm']
            # minRhm 최소 상대습도
        except TypeError:
            minRhm = -99

        try:
            avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
            # avgRhm 평균 상대습도
        except TypeError:
            avgRhm = -99

        try:
            ssDur = rDD['response']['body']['items']['item'][index]['ssDur']
            # ssDur 가조시간
        except TypeError:
            ssDur = -99

        try:
            avgTca = rDD['response']['body']['items']['item'][index]['avgTca']
            # avgTca 평균 전운량
        except TypeError:
            avgTca = -99

        try:
            avgLmac = rDD['response']['body']['items']['item'][index]['avgLmac']
            # avgLmac 평균 중하층운량
        except TypeError:
            avgLmac = -99

        try:
            sumLrgEv = rDD['response']['body']['items']['item'][index]['sumLrgEv']
            # sumLrgEv 합계 대형증발량
        except TypeError:
            sumLrgEv = -99

        try:
            sumSmlEv = rDD['response']['body']['items']['item'][index]['sumSmlEv']
            # sumSmlEv 합계 소형증발량
        except TypeError:
            sumSmlEv = -99

        try:
            n99Rn = rDD['response']['body']['items']['item'][index]['n99Rn']
            # n99Rn 9-9 강수
        except TypeError:
            n99Rn = -99

        try:
            ddMefs = rDD['response']['body']['items']['item'][index]['ddMefs']
            # ddMefs 일 최심신적설
        except TypeError:
            ddMefs = -99

        if (ddMefs is None):
            ddMefs = 0
        if (float(ddMefs) > 0):
            ddMefs = 1

        weather[index] = [str(date), avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, ddMefs]

        date = date + td.Timedelta(days = 1)

url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=20140101" \
      "&endDt=20160101" \
      "&stnIds=" + str(locationCode)
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

weather2 = [[]]

if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음

    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    size = int(rDD['response']['body']['totalCount'])
    weather2 = [[0] * 14] * (size)
    date = dt.datetime(2014, 1, 1).date()

    for index in range(0, size - 1):
        try:
            avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
            # avgTa 평균 기온
        except TypeError:
            avgTa = -99

        try:
            minTa = rDD['response']['body']['items']['item'][index]['minTa']
            # minTa 최저 기온
        except TypeError:
            minTa = -99

        try:
            maxTa = rDD['response']['body']['items']['item'][index]['maxTa']
            # maxTa 최고 기온
        except TypeError:
            maxTa = -99

        try:
            avgTd = rDD['response']['body']['items']['item'][index]['avgTd']
            # avgTd 평균 이슬점온도
        except TypeError:
            avgTd = -99

        try:
            minRhm = rDD['response']['body']['items']['item'][index]['minRhm']
            # minRhm 최소 상대습도
        except TypeError:
            minRhm = -99

        try:
            avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
            # avgRhm 평균 상대습도
        except TypeError:
            avgRhm = -99

        try:
            ssDur = rDD['response']['body']['items']['item'][index]['ssDur']
            # ssDur 가조시간
        except TypeError:
            ssDur = -99

        try:
            avgTca = rDD['response']['body']['items']['item'][index]['avgTca']
            # avgTca 평균 전운량
        except TypeError:
            avgTca = -99

        try:
            avgLmac = rDD['response']['body']['items']['item'][index]['avgLmac']
            # avgLmac 평균 중하층운량
        except TypeError:
            avgLmac = -99

        try:
            sumLrgEv = rDD['response']['body']['items']['item'][index]['sumLrgEv']
            # sumLrgEv 합계 대형증발량
        except TypeError:
            sumLrgEv = -99

        try:
            sumSmlEv = rDD['response']['body']['items']['item'][index]['sumSmlEv']
            # sumSmlEv 합계 소형증발량
        except TypeError:
            sumSmlEv = -99

        try:
            n99Rn = rDD['response']['body']['items']['item'][index]['n99Rn']
            # n99Rn 9-9 강수
        except TypeError:
            n99Rn = -99

        try:
            ddMefs = rDD['response']['body']['items']['item'][index]['ddMefs']
            # ddMefs 일 최심신적설
        except TypeError:
            ddMefs = -99

        if (ddMefs is None):
            ddMefs = 0
        if (float(ddMefs) > 0):
            ddMefs = 1

        weather2[index] = [str(date), avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, ddMefs]

        date = date + td.Timedelta(days = 1)

url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=20160101" \
      "&endDt=20180101" \
      "&stnIds=" + str(locationCode)
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

weather3 = [[]]

if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음

    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    size = int(rDD['response']['body']['totalCount'])
    weather3 = [[0] * 14] * (size)
    date = dt.datetime(2016, 1, 1).date()

    for index in range(0, size - 1):
        try:
            avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
            # avgTa 평균 기온
        except TypeError:
            avgTa = -99

        try:
            minTa = rDD['response']['body']['items']['item'][index]['minTa']
            # minTa 최저 기온
        except TypeError:
            minTa = -99

        try:
            maxTa = rDD['response']['body']['items']['item'][index]['maxTa']
            # maxTa 최고 기온
        except TypeError:
            maxTa = -99

        try:
            avgTd = rDD['response']['body']['items']['item'][index]['avgTd']
            # avgTd 평균 이슬점온도
        except TypeError:
            avgTd = -99

        try:
            minRhm = rDD['response']['body']['items']['item'][index]['minRhm']
            # minRhm 최소 상대습도
        except TypeError:
            minRhm = -99

        try:
            avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
            # avgRhm 평균 상대습도
        except TypeError:
            avgRhm = -99

        try:
            ssDur = rDD['response']['body']['items']['item'][index]['ssDur']
            # ssDur 가조시간
        except TypeError:
            ssDur = -99

        try:
            avgTca = rDD['response']['body']['items']['item'][index]['avgTca']
            # avgTca 평균 전운량
        except TypeError:
            avgTca = -99

        try:
            avgLmac = rDD['response']['body']['items']['item'][index]['avgLmac']
            # avgLmac 평균 중하층운량
        except TypeError:
            avgLmac = -99

        try:
            sumLrgEv = rDD['response']['body']['items']['item'][index]['sumLrgEv']
            # sumLrgEv 합계 대형증발량
        except TypeError:
            sumLrgEv = -99

        try:
            sumSmlEv = rDD['response']['body']['items']['item'][index]['sumSmlEv']
            # sumSmlEv 합계 소형증발량
        except TypeError:
            sumSmlEv = -99

        try:
            n99Rn = rDD['response']['body']['items']['item'][index]['n99Rn']
            # n99Rn 9-9 강수
        except TypeError:
            n99Rn = -99

        try:
            ddMefs = rDD['response']['body']['items']['item'][index]['ddMefs']
            # ddMefs 일 최심신적설
        except TypeError:
            ddMefs = -99

        if (ddMefs is None):
            ddMefs = 0
        if (float(ddMefs) > 0):
            ddMefs = 1

        weather3[index] = [str(date), avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, ddMefs]

        date = date + td.Timedelta(days = 1)

url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=20180101" \
      "&endDt=20200101" \
      "&stnIds=" + str(locationCode)
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

weather4 = [[]]

if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음

    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    size = int(rDD['response']['body']['totalCount'])
    weather4 = [[0] * 14] * (size)
    date = dt.datetime(2018, 1, 1).date()

    for index in range(0, size - 1):
        try:
            avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
            # avgTa 평균 기온
        except TypeError:
            avgTa = -99

        try:
            minTa = rDD['response']['body']['items']['item'][index]['minTa']
            # minTa 최저 기온
        except TypeError:
            minTa = -99

        try:
            maxTa = rDD['response']['body']['items']['item'][index]['maxTa']
            # maxTa 최고 기온
        except TypeError:
            maxTa = -99

        try:
            avgTd = rDD['response']['body']['items']['item'][index]['avgTd']
            # avgTd 평균 이슬점온도
        except TypeError:
            avgTd = -99

        try:
            minRhm = rDD['response']['body']['items']['item'][index]['minRhm']
            # minRhm 최소 상대습도
        except TypeError:
            minRhm = -99

        try:
            avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
            # avgRhm 평균 상대습도
        except TypeError:
            avgRhm = -99

        try:
            ssDur = rDD['response']['body']['items']['item'][index]['ssDur']
            # ssDur 가조시간
        except TypeError:
            ssDur = -99

        try:
            avgTca = rDD['response']['body']['items']['item'][index]['avgTca']
            # avgTca 평균 전운량
        except TypeError:
            avgTca = -99

        try:
            avgLmac = rDD['response']['body']['items']['item'][index]['avgLmac']
            # avgLmac 평균 중하층운량
        except TypeError:
            avgLmac = -99

        try:
            sumLrgEv = rDD['response']['body']['items']['item'][index]['sumLrgEv']
            # sumLrgEv 합계 대형증발량
        except TypeError:
            sumLrgEv = -99

        try:
            sumSmlEv = rDD['response']['body']['items']['item'][index]['sumSmlEv']
            # sumSmlEv 합계 소형증발량
        except TypeError:
            sumSmlEv = -99

        try:
            n99Rn = rDD['response']['body']['items']['item'][index]['n99Rn']
            # n99Rn 9-9 강수
        except TypeError:
            n99Rn = -99

        try:
            ddMefs = rDD['response']['body']['items']['item'][index]['ddMefs']
            # ddMefs 일 최심신적설
        except TypeError:
            ddMefs = -99

        if (ddMefs is None):
            ddMefs = 0
        if (float(ddMefs) > 0):
            ddMefs = 1

        weather4[index] = [str(date), avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, ddMefs]

        date = date + td.Timedelta(days = 1)

date = (dt.datetime.today() - td.Timedelta(days = 2)).strftime('%Y%m%d')
url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=20200101" \
      "&endDt=" + str(date) + \
      "&stnIds=" + str(locationCode)
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

weather5 = [[]]

if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음

    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    size = int(rDD['response']['body']['totalCount'])
    weather5 = [[0] * 14] * (size)
    date = dt.datetime(2020, 1, 1).date()

    for index in range(0, size - 1):
        try:
            avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
            # avgTa 평균 기온
        except TypeError:
            avgTa = -99

        try:
            minTa = rDD['response']['body']['items']['item'][index]['minTa']
            # minTa 최저 기온
        except TypeError:
            minTa = -99

        try:
            maxTa = rDD['response']['body']['items']['item'][index]['maxTa']
            # maxTa 최고 기온
        except TypeError:
            maxTa = -99

        try:
            avgTd = rDD['response']['body']['items']['item'][index]['avgTd']
            # avgTd 평균 이슬점온도
        except TypeError:
            avgTd = -99

        try:
            minRhm = rDD['response']['body']['items']['item'][index]['minRhm']
            # minRhm 최소 상대습도
        except TypeError:
            minRhm = -99

        try:
            avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
            # avgRhm 평균 상대습도
        except TypeError:
            avgRhm = -99

        try:
            ssDur = rDD['response']['body']['items']['item'][index]['ssDur']
            # ssDur 가조시간
        except TypeError:
            ssDur = -99

        try:
            avgTca = rDD['response']['body']['items']['item'][index]['avgTca']
            # avgTca 평균 전운량
        except TypeError:
            avgTca = -99

        try:
            avgLmac = rDD['response']['body']['items']['item'][index]['avgLmac']
            # avgLmac 평균 중하층운량
        except TypeError:
            avgLmac = -99

        try:
            sumLrgEv = rDD['response']['body']['items']['item'][index]['sumLrgEv']
            # sumLrgEv 합계 대형증발량
        except TypeError:
            sumLrgEv = -99

        try:
            sumSmlEv = rDD['response']['body']['items']['item'][index]['sumSmlEv']
            # sumSmlEv 합계 소형증발량
        except TypeError:
            sumSmlEv = -99

        try:
            n99Rn = rDD['response']['body']['items']['item'][index]['n99Rn']
            # n99Rn 9-9 강수
        except TypeError:
            n99Rn = -99

        try:
            ddMefs = rDD['response']['body']['items']['item'][index]['ddMefs']
            # ddMefs 일 최심신적설
        except TypeError:
            ddMefs = -99

        if (ddMefs is None):
            ddMefs = 0
        if (float(ddMefs) > 0):
            ddMefs = 1

        weather5[index] = [str(date), avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, ddMefs]

        date = date + td.Timedelta(days = 1)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, cross_validate

weather = np.vstack((weather, weather2, weather3, weather4, weather5))

x = weather[1:, 1:13]
y = weather[1:, 13]

x = x.astype(np.float64)
y = y.astype(np.float64)

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y)

date = (dt.datetime.today() - td.Timedelta(days = 2)).strftime('%Y%m%d')
url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt="+date+ \
      "&endDt="+date+ \
      "&stnIds=" + str(locationCode)

request = ul.Request(url)
response = ul.urlopen(request)
rescode = response.getcode()

if (rescode == 200):
    responseData = response.read()
    rD = xmltodict.parse(responseData)
    rDJ = json.dumps(rD)
    rDD = json.loads(rDJ)

try:
    avgTa = rDD['response']['body']['items']['item']['avgTa']
    # avgTa 평균 기온
except TypeError:
    avgTa = -99

try:
    minTa = rDD['response']['body']['items']['item']['minTa']
    # minTa 최저 기온
except TypeError:
    minTa = -99

try:
    maxTa = rDD['response']['body']['items']['item']['maxTa']
    # maxTa 최고 기온
except TypeError:
    maxTa = -99

try:
    avgTd = rDD['response']['body']['items']['item']['avgTd']
    # avgTd 평균 이슬점온도
except TypeError:
    avgTd = -99

try:
    minRhm = rDD['response']['body']['items']['item']['minRhm']
    # minRhm 최소 상대습도
except TypeError:
    minRhm = -99

try:
    avgRhm = rDD['response']['body']['items']['item']['avgRhm']
    # avgRhm 평균 상대습도
except TypeError:
    avgRhm = -99

try:
    ssDur = rDD['response']['body']['items']['item']['ssDur']
    # ssDur 가조시간
except TypeError:
    ssDur = -99

try:
    avgTca = rDD['response']['body']['items']['item']['avgTca']
    # avgTca 평균 전운량
except TypeError:
    avgTca = -99

try:
    avgLmac = rDD['response']['body']['items']['item']['avgLmac']
    # avgLmac 평균 중하층운량
except TypeError:
    avgLmac = -99

try:
    sumLrgEv = rDD['response']['body']['items']['item']['sumLrgEv']
    # sumLrgEv 합계 대형증발량
except TypeError:
    sumLrgEv = -99

try:
    sumSmlEv = rDD['response']['body']['items']['item']['sumSmlEv']
    # sumSmlEv 합계 소형증발량
except TypeError:
    sumSmlEv = -99

try:
    n99Rn = rDD['response']['body']['items']['item']['n99Rn']
    # n99Rn 9-9 강수
except TypeError:
    n99Rn = -99

snowX = [[avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn]]

from sklearn.linear_model import LogisticRegression

np.nan_to_num(x_scaled, copy=False)

log = LogisticRegression()
log.fit(x_scaled, y)

snowX = scaler.transform(snowX)
np.nan_to_num(snowX, copy=False)
snowY = log.predict_proba(snowX)
print("오늘 눈이 올 확률은 " + str(round(snowY[0, 1] * 100, 2)) + "% 입니다.")

locationCodeList = [108, 112, 143, 133, 159, 152, 156, 184]

# Seoul
def snowAnotherLocation(index):
    date = (dt.datetime.today() - td.Timedelta(days = 2)).strftime('%Y%m%d')
    url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
        "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
        "&numOfRows=999" \
        "&dataCd=ASOS" \
        "&dateCd=DAY" \
        "&startDt="+date+ \
        "&endDt="+date+ \
        "&stnIds=" + str(locationCodeList[index])

    request = ul.Request(url)
    response = ul.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        responseData = response.read()
        rD = xmltodict.parse(responseData)
        rDJ = json.dumps(rD)
        rDD = json.loads(rDJ)

    try:
        avgTa = rDD['response']['body']['items']['item']['avgTa']
        # avgTa 평균 기온
    except TypeError:
        avgTa = -99

    try:
        minTa = rDD['response']['body']['items']['item']['minTa']
        # minTa 최저 기온
    except TypeError:
        minTa = -99

    try:
        maxTa = rDD['response']['body']['items']['item']['maxTa']
        # maxTa 최고 기온
    except TypeError:
        maxTa = -99

    try:
        avgTd = rDD['response']['body']['items']['item']['avgTd']
        # avgTd 평균 이슬점온도
    except TypeError:
        avgTd = -99

    try:
        minRhm = rDD['response']['body']['items']['item']['minRhm']
        # minRhm 최소 상대습도
    except TypeError:
        minRhm = -99

    try:
        avgRhm = rDD['response']['body']['items']['item']['avgRhm']
        # avgRhm 평균 상대습도
    except TypeError:
        avgRhm = -99

    try:
        ssDur = rDD['response']['body']['items']['item']['ssDur']
        # ssDur 가조시간
    except TypeError:
        ssDur = -99

    try:
        avgTca = rDD['response']['body']['items']['item']['avgTca']
        # avgTca 평균 전운량
    except TypeError:
        avgTca = -99

    try:
        avgLmac = rDD['response']['body']['items']['item']['avgLmac']
        # avgLmac 평균 중하층운량
    except TypeError:
        avgLmac = -99

    try:
        sumLrgEv = rDD['response']['body']['items']['item']['sumLrgEv']
        # sumLrgEv 합계 대형증발량
    except TypeError:
        sumLrgEv = -99

    try:
        sumSmlEv = rDD['response']['body']['items']['item']['sumSmlEv']
        # sumSmlEv 합계 소형증발량
    except TypeError:
        sumSmlEv = -99

    try:
        n99Rn = rDD['response']['body']['items']['item']['n99Rn']
        # n99Rn 9-9 강수
    except TypeError:
        n99Rn = -99

    snowX = [[avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn]]

    np.nan_to_num(x_scaled, copy=False)

    log = LogisticRegression()
    log.fit(x_scaled, y)

    snowX = scaler.transform(snowX)
    
    np.nan_to_num(snowX, copy=False)
    temp = log.predict_proba(snowX)
    return str(round(temp[0, 1] * 100, 2))

snowLocation = []
snowLocation.append(snowAnotherLocation(0))
snowLocation.append(snowAnotherLocation(1))
snowLocation.append(snowAnotherLocation(2))
snowLocation.append(snowAnotherLocation(3))
snowLocation.append(snowAnotherLocation(4))
snowLocation.append(snowAnotherLocation(5))
snowLocation.append(snowAnotherLocation(6))
snowLocation.append(snowAnotherLocation(7))



# Rain
# 지점 코드 (default: 대전)
locationCode = 133

url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=20120101" \
      "&endDt=20140101" \
      "&stnIds=" + str(locationCode)
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

weather = [[]]
size = 0
date = 0

if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음

    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    size = int(rDD['response']['body']['totalCount'])
    weather = [[0] * 17] * (size)
    date = dt.datetime(2012, 1, 1).date()

    weather[0] = ['date', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    for index in range(1, size):
        try:
            avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
            # avgTa 평균 기온
        except TypeError:
            avgTa = -99

        try:
            minTa = rDD['response']['body']['items']['item'][index]['minTa']
            # minTa 최저 기온
        except TypeError:
            minTa = -99

        try:
            maxTa = rDD['response']['body']['items']['item'][index]['maxTa']
            # maxTa 최고 기온
        except TypeError:
            maxTa = -99

        try:
            avgTd = rDD['response']['body']['items']['item'][index]['avgTd']
            # avgTd 평균 이슬점온도
        except TypeError:
            avgTd = -99

        try:
            minRhm = rDD['response']['body']['items']['item'][index]['minRhm']
            # minRhm 최소 상대습도
        except TypeError:
            minRhm = -99

        try:
            avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
            # avgRhm 평균 상대습도
        except TypeError:
            avgRhm = -99

        try:
            ssDur = rDD['response']['body']['items']['item'][index]['ssDur']
            # ssDur 가조시간
        except TypeError:
            ssDur = -99

        try:
            sumSsHr = rDD['response']['body']['items']['item'][index]['sumSsHr']
            # sumSsHr 합계 일조 시간
        except TypeError:
            sumSsHr = -99

        try:
            hr1MaxIcsr = rDD['response']['body']['items']['item'][index]['hr1MaxIcsr']
            # hr1MaxIcsr 1시간 최다 일사량
        except TypeError:
            hr1MaxIcsr = -99

        try:
            sumGsr = rDD['response']['body']['items']['item'][index]['sumGsr']
            # sumGsr 합계 일사
        except TypeError:
            sumGsr = -99

        try:
            avgTca = rDD['response']['body']['items']['item'][index]['avgTca']
            # avgTca 평균 전운량
        except TypeError:
            avgTca = -99

        try:
            avgLmac = rDD['response']['body']['items']['item'][index]['avgLmac']
            # avgLmac 평균 중하층운량
        except TypeError:
            avgLmac = -99

        try:
            sumLrgEv = rDD['response']['body']['items']['item'][index]['sumLrgEv']
            # sumLrgEv 합계 대형증발량
        except TypeError:
            sumLrgEv = -99

        try:
            sumSmlEv = rDD['response']['body']['items']['item'][index]['sumSmlEv']
            # sumSmlEv 합계 소형증발량
        except TypeError:
            sumSmlEv = -99

        try:
            n99Rn = rDD['response']['body']['items']['item'][index]['n99Rn']
            # n99Rn 9-9 강수
        except TypeError:
            n99Rn = -99

        try:
            sumRn = rDD['response']['body']['items']['item'][index]['sumRn']
            # sumRn 일강수량
        except TypeError:
            sumRn = -99
        if (float(sumRn) > 0):
            sumRn = 1

        weather[index] = [str(date), avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, sumRn]

        date = date + td.Timedelta(days = 1)

url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=20140101" \
      "&endDt=20160101" \
      "&stnIds=" + str(locationCode)
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

weather2 = [[]]

if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음

    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    size = int(rDD['response']['body']['totalCount'])
    weather2 = [[0] * 17] * (size)
    date = dt.datetime(2014, 1, 1).date()

    for index in range(0, size - 1):
        try:
            avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
            # avgTa 평균 기온
        except TypeError:
            avgTa = -99

        try:
            minTa = rDD['response']['body']['items']['item'][index]['minTa']
            # minTa 최저 기온
        except TypeError:
            minTa = -99

        try:
            maxTa = rDD['response']['body']['items']['item'][index]['maxTa']
            # maxTa 최고 기온
        except TypeError:
            maxTa = -99

        try:
            avgTd = rDD['response']['body']['items']['item'][index]['avgTd']
            # avgTd 평균 이슬점온도
        except TypeError:
            avgTd = -99

        try:
            minRhm = rDD['response']['body']['items']['item'][index]['minRhm']
            # minRhm 최소 상대습도
        except TypeError:
            minRhm = -99

        try:
            avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
            # avgRhm 평균 상대습도
        except TypeError:
            avgRhm = -99

        try:
            ssDur = rDD['response']['body']['items']['item'][index]['ssDur']
            # ssDur 가조시간
        except TypeError:
            ssDur = -99

        try:
            sumSsHr = rDD['response']['body']['items']['item'][index]['sumSsHr']
            # sumSsHr 합계 일조 시간
        except TypeError:
            sumSsHr = -99

        try:
            hr1MaxIcsr = rDD['response']['body']['items']['item'][index]['hr1MaxIcsr']
            # hr1MaxIcsr 1시간 최다 일사량
        except TypeError:
            hr1MaxIcsr = -99

        try:
            sumGsr = rDD['response']['body']['items']['item'][index]['sumGsr']
            # sumGsr 합계 일사
        except TypeError:
            sumGsr = -99

        try:
            avgTca = rDD['response']['body']['items']['item'][index]['avgTca']
            # avgTca 평균 전운량
        except TypeError:
            avgTca = -99

        try:
            avgLmac = rDD['response']['body']['items']['item'][index]['avgLmac']
            # avgLmac 평균 중하층운량
        except TypeError:
            avgLmac = -99

        try:
            sumLrgEv = rDD['response']['body']['items']['item'][index]['sumLrgEv']
            # sumLrgEv 합계 대형증발량
        except TypeError:
            sumLrgEv = -99

        try:
            sumSmlEv = rDD['response']['body']['items']['item'][index]['sumSmlEv']
            # sumSmlEv 합계 소형증발량
        except TypeError:
            sumSmlEv = -99

        try:
            n99Rn = rDD['response']['body']['items']['item'][index]['n99Rn']
            # n99Rn 9-9 강수
        except TypeError:
            n99Rn = -99

        try:
            sumRn = rDD['response']['body']['items']['item'][index]['sumRn']
            # sumRn 일강수량
        except TypeError:
            sumRn = -99
        if (float(sumRn) > 0):
            sumRn = 1

        weather2[index] = [str(date), avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, sumRn]

        date = date + td.Timedelta(days = 1)

url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=20160101" \
      "&endDt=20180101" \
      "&stnIds=" + str(locationCode)
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

weather3 = [[]]

if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음

    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    size = int(rDD['response']['body']['totalCount'])
    weather3 = [[0] * 17] * (size)
    date = dt.datetime(2016, 1, 1).date()

    for index in range(0, size - 1):
        try:
            avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
            # avgTa 평균 기온
        except TypeError:
            avgTa = -99

        try:
            minTa = rDD['response']['body']['items']['item'][index]['minTa']
            # minTa 최저 기온
        except TypeError:
            minTa = -99

        try:
            maxTa = rDD['response']['body']['items']['item'][index]['maxTa']
            # maxTa 최고 기온
        except TypeError:
            maxTa = -99

        try:
            avgTd = rDD['response']['body']['items']['item'][index]['avgTd']
            # avgTd 평균 이슬점온도
        except TypeError:
            avgTd = -99

        try:
            minRhm = rDD['response']['body']['items']['item'][index]['minRhm']
            # minRhm 최소 상대습도
        except TypeError:
            minRhm = -99

        try:
            avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
            # avgRhm 평균 상대습도
        except TypeError:
            avgRhm = -99

        try:
            ssDur = rDD['response']['body']['items']['item'][index]['ssDur']
            # ssDur 가조시간
        except TypeError:
            ssDur = -99

        try:
            sumSsHr = rDD['response']['body']['items']['item'][index]['sumSsHr']
            # sumSsHr 합계 일조 시간
        except TypeError:
            sumSsHr = -99

        try:
            hr1MaxIcsr = rDD['response']['body']['items']['item'][index]['hr1MaxIcsr']
            # hr1MaxIcsr 1시간 최다 일사량
        except TypeError:
            hr1MaxIcsr = -99

        try:
            sumGsr = rDD['response']['body']['items']['item'][index]['sumGsr']
            # sumGsr 합계 일사
        except TypeError:
            sumGsr = -99

        try:
            avgTca = rDD['response']['body']['items']['item'][index]['avgTca']
            # avgTca 평균 전운량
        except TypeError:
            avgTca = -99

        try:
            avgLmac = rDD['response']['body']['items']['item'][index]['avgLmac']
            # avgLmac 평균 중하층운량
        except TypeError:
            avgLmac = -99

        try:
            sumLrgEv = rDD['response']['body']['items']['item'][index]['sumLrgEv']
            # sumLrgEv 합계 대형증발량
        except TypeError:
            sumLrgEv = -99

        try:
            sumSmlEv = rDD['response']['body']['items']['item'][index]['sumSmlEv']
            # sumSmlEv 합계 소형증발량
        except TypeError:
            sumSmlEv = -99

        try:
            n99Rn = rDD['response']['body']['items']['item'][index]['n99Rn']
            # n99Rn 9-9 강수
        except TypeError:
            n99Rn = -99

        try:
            sumRn = rDD['response']['body']['items']['item'][index]['sumRn']
            # sumRn 일강수량
        except TypeError:
            sumRn = -99
        if (float(sumRn) > 0):
            sumRn = 1

        weather3[index] = [str(date), avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, sumRn]

        date = date + td.Timedelta(days = 1)

url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=20180101" \
      "&endDt=20200101" \
      "&stnIds=" + str(locationCode)
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

weather4 = [[]]

if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음

    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    size = int(rDD['response']['body']['totalCount'])
    weather4 = [[0] * 17] * (size)
    date = dt.datetime(2018, 1, 1).date()

    for index in range(0, size - 1):
        try:
            avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
            # avgTa 평균 기온
        except TypeError:
            avgTa = -99

        try:
            minTa = rDD['response']['body']['items']['item'][index]['minTa']
            # minTa 최저 기온
        except TypeError:
            minTa = -99

        try:
            maxTa = rDD['response']['body']['items']['item'][index]['maxTa']
            # maxTa 최고 기온
        except TypeError:
            maxTa = -99

        try:
            avgTd = rDD['response']['body']['items']['item'][index]['avgTd']
            # avgTd 평균 이슬점온도
        except TypeError:
            avgTd = -99

        try:
            minRhm = rDD['response']['body']['items']['item'][index]['minRhm']
            # minRhm 최소 상대습도
        except TypeError:
            minRhm = -99

        try:
            avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
            # avgRhm 평균 상대습도
        except TypeError:
            avgRhm = -99

        try:
            ssDur = rDD['response']['body']['items']['item'][index]['ssDur']
            # ssDur 가조시간
        except TypeError:
            ssDur = -99

        try:
            sumSsHr = rDD['response']['body']['items']['item'][index]['sumSsHr']
            # sumSsHr 합계 일조 시간
        except TypeError:
            sumSsHr = -99

        try:
            hr1MaxIcsr = rDD['response']['body']['items']['item'][index]['hr1MaxIcsr']
            # hr1MaxIcsr 1시간 최다 일사량
        except TypeError:
            hr1MaxIcsr = -99

        try:
            sumGsr = rDD['response']['body']['items']['item'][index]['sumGsr']
            # sumGsr 합계 일사
        except TypeError:
            sumGsr = -99

        try:
            avgTca = rDD['response']['body']['items']['item'][index]['avgTca']
            # avgTca 평균 전운량
        except TypeError:
            avgTca = -99

        try:
            avgLmac = rDD['response']['body']['items']['item'][index]['avgLmac']
            # avgLmac 평균 중하층운량
        except TypeError:
            avgLmac = -99

        try:
            sumLrgEv = rDD['response']['body']['items']['item'][index]['sumLrgEv']
            # sumLrgEv 합계 대형증발량
        except TypeError:
            sumLrgEv = -99

        try:
            sumSmlEv = rDD['response']['body']['items']['item'][index]['sumSmlEv']
            # sumSmlEv 합계 소형증발량
        except TypeError:
            sumSmlEv = -99

        try:
            n99Rn = rDD['response']['body']['items']['item'][index]['n99Rn']
            # n99Rn 9-9 강수
        except TypeError:
            n99Rn = -99

        try:
            sumRn = rDD['response']['body']['items']['item'][index]['sumRn']
            # sumRn 일강수량
        except TypeError:
            sumRn = -99
        if (float(sumRn) > 0):
            sumRn = 1

        weather4[index] = [str(date), avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, sumRn]

        date = date + td.Timedelta(days = 1)

date = (dt.datetime.today() - td.Timedelta(days = 2)).strftime('%Y%m%d')
url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=20200101" \
      "&endDt=" + str(date) + \
      "&stnIds=" + str(locationCode)
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

weather5 = [[]]

if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음

    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    size = int(rDD['response']['body']['totalCount'])
    weather5 = [[0] * 17] * (size)
    date = dt.datetime(2020, 1, 1).date()

    for index in range(0, size - 1):
        try:
            avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
            # avgTa 평균 기온
        except TypeError:
            avgTa = -99

        try:
            minTa = rDD['response']['body']['items']['item'][index]['minTa']
            # minTa 최저 기온
        except TypeError:
            minTa = -99

        try:
            maxTa = rDD['response']['body']['items']['item'][index]['maxTa']
            # maxTa 최고 기온
        except TypeError:
            maxTa = -99

        try:
            avgTd = rDD['response']['body']['items']['item'][index]['avgTd']
            # avgTd 평균 이슬점온도
        except TypeError:
            avgTd = -99

        try:
            minRhm = rDD['response']['body']['items']['item'][index]['minRhm']
            # minRhm 최소 상대습도
        except TypeError:
            minRhm = -99

        try:
            avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
            # avgRhm 평균 상대습도
        except TypeError:
            avgRhm = -99

        try:
            ssDur = rDD['response']['body']['items']['item'][index]['ssDur']
            # ssDur 가조시간
        except TypeError:
            ssDur = -99

        try:
            sumSsHr = rDD['response']['body']['items']['item'][index]['sumSsHr']
            # sumSsHr 합계 일조 시간
        except TypeError:
            sumSsHr = -99

        try:
            hr1MaxIcsr = rDD['response']['body']['items']['item'][index]['hr1MaxIcsr']
            # hr1MaxIcsr 1시간 최다 일사량
        except TypeError:
            hr1MaxIcsr = -99

        try:
            sumGsr = rDD['response']['body']['items']['item'][index]['sumGsr']
            # sumGsr 합계 일사
        except TypeError:
            sumGsr = -99

        try:
            avgTca = rDD['response']['body']['items']['item'][index]['avgTca']
            # avgTca 평균 전운량
        except TypeError:
            avgTca = -99

        try:
            avgLmac = rDD['response']['body']['items']['item'][index]['avgLmac']
            # avgLmac 평균 중하층운량
        except TypeError:
            avgLmac = -99

        try:
            sumLrgEv = rDD['response']['body']['items']['item'][index]['sumLrgEv']
            # sumLrgEv 합계 대형증발량
        except TypeError:
            sumLrgEv = -99

        try:
            sumSmlEv = rDD['response']['body']['items']['item'][index]['sumSmlEv']
            # sumSmlEv 합계 소형증발량
        except TypeError:
            sumSmlEv = -99

        try:
            n99Rn = rDD['response']['body']['items']['item'][index]['n99Rn']
            # n99Rn 9-9 강수
        except TypeError:
            n99Rn = -99

        try:
            sumRn = rDD['response']['body']['items']['item'][index]['sumRn']
            # sumRn 일강수량
        except TypeError:
            sumRn = -99
        if (float(sumRn) > 0):
            sumRn = 1

        weather5[index] = [str(date), avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, sumRn]

        date = date + td.Timedelta(days = 1)

weather = np.vstack((weather, weather2, weather3, weather4, weather5))

x = weather[1:, 1:16]
y = weather[1:, 16]

x = x.astype(np.float64)
y = y.astype(np.float64)

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y)

date = (dt.datetime.today() - td.Timedelta(days = 2)).strftime('%Y%m%d')
url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt="+date+ \
      "&endDt="+date+ \
      "&stnIds=" + str(locationCode)

request = ul.Request(url)
response = ul.urlopen(request)
rescode = response.getcode()

if (rescode == 200):
    responseData = response.read()
    rD = xmltodict.parse(responseData)
    rDJ = json.dumps(rD)
    rDD = json.loads(rDJ)

try:
    avgTa = rDD['response']['body']['items']['item']['avgTa']
    # avgTa 평균 기온
except TypeError:
    avgTa = -99

try:
    minTa = rDD['response']['body']['items']['item']['minTa']
    # minTa 최저 기온
except TypeError:
    minTa = -99

try:
    maxTa = rDD['response']['body']['items']['item']['maxTa']
    # maxTa 최고 기온
except TypeError:
    maxTa = -99

try:
    avgTd = rDD['response']['body']['items']['item']['avgTd']
    # avgTd 평균 이슬점온도
except TypeError:
    avgTd = -99

try:
    minRhm = rDD['response']['body']['items']['item']['minRhm']
    # minRhm 최소 상대습도
except TypeError:
    minRhm = -99

try:
    avgRhm = rDD['response']['body']['items']['item']['avgRhm']
    # avgRhm 평균 상대습도
except TypeError:
    avgRhm = -99

try:
    ssDur = rDD['response']['body']['items']['item']['ssDur']
    # ssDur 가조시간
except TypeError:
    ssDur = -99

try:
    sumSsHr = rDD['response']['body']['items']['item']['sumSsHr']
    # sumSsHr 합계 일조 시간
except TypeError:
    sumSsHr = -99

try:
    hr1MaxIcsr = rDD['response']['body']['items']['item']['hr1MaxIcsr']
    # hr1MaxIcsr 1시간 최다 일사량
except TypeError:
    hr1MaxIcsr = -99

try:
    sumGsr = rDD['response']['body']['items']['item']['sumGsr']
    # sumGsr 합계 일사
except TypeError:
    sumGsr = -99

try:
    avgTca = rDD['response']['body']['items']['item']['avgTca']
    # avgTca 평균 전운량
except TypeError:
    avgTca = -99

try:
    avgLmac = rDD['response']['body']['items']['item']['avgLmac']
    # avgLmac 평균 중하층운량
except TypeError:
    avgLmac = -99

try:
    sumLrgEv = rDD['response']['body']['items']['item']['sumLrgEv']
    # sumLrgEv 합계 대형증발량
except TypeError:
    sumLrgEv = -99

try:
    sumSmlEv = rDD['response']['body']['items']['item']['sumSmlEv']
    # sumSmlEv 합계 소형증발량
except TypeError:
    sumSmlEv = -99

try:
    n99Rn = rDD['response']['body']['items']['item']['n99Rn']
    # n99Rn 9-9 강수
except TypeError:
    n99Rn = -99

rainX = [[avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn]]

np.nan_to_num(x_scaled, copy=False)

log = LogisticRegression()
log.fit(x_scaled, y)

rainX = scaler.transform(rainX)
np.nan_to_num(rainX, copy=False)
rainY = log.predict_proba(rainX)
print("오늘 비가 올 확률은 " + str(round(rainY[0, 1] * 100, 2)) + "% 입니다.")





locationCodeList = [108, 112, 143, 133, 159, 152, 156, 184]

def rainAnotherLocation(index):
    date = (dt.datetime.today() - td.Timedelta(days = 2)).strftime('%Y%m%d')
    url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
        "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
        "&numOfRows=999" \
        "&dataCd=ASOS" \
        "&dateCd=DAY" \
        "&startDt="+date+ \
        "&endDt="+date+ \
        "&stnIds=" + str(locationCodeList[index])

    request = ul.Request(url)
    response = ul.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        responseData = response.read()
        rD = xmltodict.parse(responseData)
        rDJ = json.dumps(rD)
        rDD = json.loads(rDJ)

    try:
        avgTa = rDD['response']['body']['items']['item']['avgTa']
        # avgTa 평균 기온
    except TypeError:
        avgTa = -99

    try:
        minTa = rDD['response']['body']['items']['item']['minTa']
        # minTa 최저 기온
    except TypeError:
        minTa = -99

    try:
        maxTa = rDD['response']['body']['items']['item']['maxTa']
        # maxTa 최고 기온
    except TypeError:
        maxTa = -99

    try:
        avgTd = rDD['response']['body']['items']['item']['avgTd']
        # avgTd 평균 이슬점온도
    except TypeError:
        avgTd = -99

    try:
        minRhm = rDD['response']['body']['items']['item']['minRhm']
        # minRhm 최소 상대습도
    except TypeError:
        minRhm = -99

    try:
        avgRhm = rDD['response']['body']['items']['item']['avgRhm']
        # avgRhm 평균 상대습도
    except TypeError:
        avgRhm = -99

    try:
        ssDur = rDD['response']['body']['items']['item']['ssDur']
        # ssDur 가조시간
    except TypeError:
        ssDur = -99

    try:
        sumSsHr = rDD['response']['body']['items']['item']['sumSsHr']
        # sumSsHr 합계 일조 시간
    except TypeError:
        sumSsHr = -99

    try:
        hr1MaxIcsr = rDD['response']['body']['items']['item']['hr1MaxIcsr']
        # hr1MaxIcsr 1시간 최다 일사량
    except TypeError:
        hr1MaxIcsr = -99

    try:
        sumGsr = rDD['response']['body']['items']['item']['sumGsr']
        # sumGsr 합계 일사
    except TypeError:
        sumGsr = -99

    try:
        avgTca = rDD['response']['body']['items']['item']['avgTca']
        # avgTca 평균 전운량
    except TypeError:
        avgTca = -99

    try:
        avgLmac = rDD['response']['body']['items']['item']['avgLmac']
        # avgLmac 평균 중하층운량
    except TypeError:
        avgLmac = -99

    try:
        sumLrgEv = rDD['response']['body']['items']['item']['sumLrgEv']
        # sumLrgEv 합계 대형증발량
    except TypeError:
        sumLrgEv = -99

    try:
        sumSmlEv = rDD['response']['body']['items']['item']['sumSmlEv']
        # sumSmlEv 합계 소형증발량
    except TypeError:
        sumSmlEv = -99

    try:
        n99Rn = rDD['response']['body']['items']['item']['n99Rn']
        # n99Rn 9-9 강수
    except TypeError:
        n99Rn = -99

    rainX = [[avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn]]

    np.nan_to_num(x_scaled, copy=False)

    log = LogisticRegression()
    log.fit(x_scaled, y)

    rainX = scaler.transform(rainX)
    
    np.nan_to_num(rainX, copy=False)
    temp = log.predict_proba(rainX)
    return str(round(temp[0, 1] * 100, 2))

rainLocation = []
rainLocation.append(rainAnotherLocation(0))
rainLocation.append(rainAnotherLocation(1))
rainLocation.append(rainAnotherLocation(2))
rainLocation.append(rainAnotherLocation(3))
rainLocation.append(rainAnotherLocation(4))
rainLocation.append(rainAnotherLocation(5))
rainLocation.append(rainAnotherLocation(6))
rainLocation.append(rainAnotherLocation(7))






# Typhoon
url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=20120101" \
      "&endDt=20140101" \
      "&stnIds=184"
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

weather = [[]]
size = 0
date = 0

if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음

    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    size = int(rDD['response']['body']['totalCount'])
    weather = [[0] * 8] * (size)
    date = dt.datetime(2012, 1, 1).date()

    weather[0] = ['date', '1', '2', '3', '4', '5', '6', '7']
    for index in range(1, size):
        try:
            avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
            # 평균 상대 습도
        except TypeError:
            avgRhm = -99

        try:
            avgPs = rDD['response']['body']['items']['item'][index]['avgPs']
            # 평균 해면 기압
        except TypeError:
            avgPs = -99

        try:
            avgPa = rDD['response']['body']['items']['item'][index]['avgPa']
            # 평균 현지 기압
        except TypeError:
            avgPa = -99

        try:
            avgWs = rDD['response']['body']['items']['item'][index]['avgWs']
            # 평균 풍속
        except TypeError:
            avgWs = -99

        try:
            sumRn = rDD['response']['body']['items']['item'][index]['sumRn']
            # 강수량
        except TypeError:
            sumRn = -99

        try:
            avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
            # 평균 기온
        except TypeError:
            avgTa = -99

        weather[index] = [str(date), avgRhm, avgPs, avgPa, avgWs, sumRn, avgTa, 0]

        date = date + td.Timedelta(days=1)

url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=20140101" \
      "&endDt=20160101" \
      "&stnIds=184"
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

weather2 = [[]]
size = 0
date = 0

if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음

    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    size = int(rDD['response']['body']['totalCount'])
    weather2 = [[0] * 8] * (size - 1)
    date = dt.datetime(2014, 1, 1).date()

    for index in range(0, size - 1):
        try:
            avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
            # 평균 상대 습도
        except TypeError:
            avgRhm = -99

        try:
            avgPs = rDD['response']['body']['items']['item'][index]['avgPs']
            # 평균 해면 기압
        except TypeError:
            avgPs = -99

        try:
            avgPa = rDD['response']['body']['items']['item'][index]['avgPa']
            # 평균 현지 기압
        except TypeError:
            avgPa = -99

        try:
            avgWs = rDD['response']['body']['items']['item'][index]['avgWs']
            # 평균 풍속
        except TypeError:
            avgWs = -99

        try:
            sumRn = rDD['response']['body']['items']['item'][index]['sumRn']
            # 강수량
        except TypeError:
            sumRn = -99

        try:
            avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
            # 평균 기온
        except TypeError:
            avgTa = -99

        weather2[index] = [str(date), avgRhm, avgPs, avgPa, avgWs, sumRn, avgTa, 0]

        date = date + td.Timedelta(days=1)        

url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=20160101" \
      "&endDt=20180101" \
      "&stnIds=184"
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

weather3 = [[]]
size = 0
date = 0

if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음

    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    size = int(rDD['response']['body']['totalCount'])
    weather3 = [[0] * 8] * (size - 1)
    date = dt.datetime(2016, 1, 1).date()

    for index in range(0, size - 1):
        try:
            avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
            # 평균 상대 습도
        except TypeError:
            avgRhm = -99

        try:
            avgPs = rDD['response']['body']['items']['item'][index]['avgPs']
            # 평균 해면 기압
        except TypeError:
            avgPs = -99

        try:
            avgPa = rDD['response']['body']['items']['item'][index]['avgPa']
            # 평균 현지 기압
        except TypeError:
            avgPa = -99

        try:
            avgWs = rDD['response']['body']['items']['item'][index]['avgWs']
            # 평균 풍속
        except TypeError:
            avgWs = -99

        try:
            sumRn = rDD['response']['body']['items']['item'][index]['sumRn']
            # 강수량
        except TypeError:
            sumRn = -99

        try:
            avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
            # 평균 기온
        except TypeError:
            avgTa = -99

        weather3[index] = [str(date), avgRhm, avgPs, avgPa, avgWs, sumRn, avgTa, 0]

        date = date + td.Timedelta(days=1)     

url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=20180101" \
      "&endDt=20200101" \
      "&stnIds=184"
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

weather4 = [[]]
size = 0
date = 0

if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음

    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    size = int(rDD['response']['body']['totalCount'])
    weather4 = [[0] * 8] * (size - 1)
    date = dt.datetime(2018, 1, 1).date()

    for index in range(0, size - 1):
        try:
            avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
            # 평균 상대 습도
        except TypeError:
            avgRhm = -99

        try:
            avgPs = rDD['response']['body']['items']['item'][index]['avgPs']
            # 평균 해면 기압
        except TypeError:
            avgPs = -99

        try:
            avgPa = rDD['response']['body']['items']['item'][index]['avgPa']
            # 평균 현지 기압
        except TypeError:
            avgPa = -99

        try:
            avgWs = rDD['response']['body']['items']['item'][index]['avgWs']
            # 평균 풍속
        except TypeError:
            avgWs = -99

        try:
            sumRn = rDD['response']['body']['items']['item'][index]['sumRn']
            # 강수량
        except TypeError:
            sumRn = -99

        try:
            avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
            # 평균 기온
        except TypeError:
            avgTa = -99

        weather4[index] = [str(date), avgRhm, avgPs, avgPa, avgWs, sumRn, avgTa, 0]

        date = date + td.Timedelta(days=1)     

date = (dt.datetime.today() - td.Timedelta(days = 2)).strftime('%Y%m%d')
url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=20200101" \
      "&endDt="+date+ \
      "&stnIds=184"
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

weather5 = [[]]
size = 0
date = 0

if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음

    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    size = int(rDD['response']['body']['totalCount'])
    weather5 = [[0] * 8] * (size - 1)
    date = dt.datetime(2020, 1, 1).date()

    for index in range(0, size - 1):
        try:
            avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
            # 평균 상대 습도
        except TypeError:
            avgRhm = -99

        try:
            avgPs = rDD['response']['body']['items']['item'][index]['avgPs']
            # 평균 해면 기압
        except TypeError:
            avgPs = -99

        try:
            avgPa = rDD['response']['body']['items']['item'][index]['avgPa']
            # 평균 현지 기압
        except TypeError:
            avgPa = -99

        try:
            avgWs = rDD['response']['body']['items']['item'][index]['avgWs']
            # 평균 풍속
        except TypeError:
            avgWs = -99

        try:
            sumRn = rDD['response']['body']['items']['item'][index]['sumRn']
            # 강수량
        except TypeError:
            sumRn = -99

        try:
            avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
            # 평균 기온
        except TypeError:
            avgTa = -99

        weather5[index] = [str(date), avgRhm, avgPs, avgPa, avgWs, sumRn, avgTa, 0]

        date = date + td.Timedelta(days=1)
weather = np.vstack((weather, weather2, weather3, weather4, weather5))

import pandas as pd

csv = pd.read_csv('./typhoon.csv', encoding = 'UTF-8')
csv = csv[['start', 'end']]

size = len(weather)
rowCount = len(csv)
for index in range(0, rowCount):
    startDate = str(csv.iloc[index, 0])
    endDate = str(csv.iloc[index, 1])

    startDate = dt.datetime.strptime(startDate, '%Y%m%d').date()
    endDate = dt.datetime.strptime(endDate, '%Y%m%d').date()

    dateGap = (endDate - startDate).days
    date = startDate

    for temp in range(0, dateGap + 1):
        count = 1
        while True:
            if (str(date) == weather[count][0]):
                weather[count][7] = 1
                break
            else:
                count += 1
                if (count > size):
                    count = 1
                    print('! restart ')
        date = date + td.Timedelta(days=1)

weather = np.array(weather)
x = weather[1:, 1:7]
y = weather[1:, 7]

x = x.astype(np.float64)
y = y.astype(np.float64)

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y)
date = (dt.datetime.today() - td.Timedelta(days = 2)).strftime('%Y%m%d')
url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt="+date+ \
      "&endDt="+date+ \
      "&stnIds=184"

request = ul.Request(url)
response = ul.urlopen(request)
rescode = response.getcode()

if (rescode == 200):
    responseData = response.read()
    rD = xmltodict.parse(responseData)
    rDJ = json.dumps(rD)
    rDD = json.loads(rDJ)
    
try:
    avgRhm = rDD['response']['body']['items']['item']['avgRhm']
    # 평균 상대 습도
except TypeError:
    avgRhm = -99

try:
    avgPs = rDD['response']['body']['items']['item']['avgPs']
    # 평균 해면 기압
except TypeError:
    avgPs = -99

try:
    avgPa = rDD['response']['body']['items']['item']['avgPa']
    # 평균 현지 기압
except TypeError:
    avgPa = -99

try:
    avgWs = rDD['response']['body']['items']['item']['avgWs']
    # 평균 풍속
except TypeError:
    avgWs = -99

try:
    sumRn = rDD['response']['body']['items']['item']['sumRn']
    # 강수량
except TypeError:
    sumRn = -99

try:
    avgTa = rDD['response']['body']['items']['item']['avgTa']
    # 평균 기온
except TypeError:
    avgTa = -99

typhoonX = [[avgRhm, avgPs, avgPa, avgWs, sumRn, avgTa]]

log = LogisticRegression()
np.nan_to_num(x_scaled, copy=False)
log.fit(x_scaled, y)

typhoonX = scaler.transform(typhoonX)
np.nan_to_num(typhoonX, copy=False)
typhoonY = log.predict_proba(typhoonX)
print("오늘 태풍이 발생할 확률은 " + str(round(typhoonY[0, 1] * 100, 2)) + "% 입니다.")

csv = pd.read_csv('./typhoon.csv', encoding = 'UTF-8')
csv = csv[['한글태풍명', '영문태풍명', '발생일시', '소멸일시']]

load = []
for i in range(0, 33):
    st = ''
    for j in range(0, 4):
        st += (str(csv.iat[i, j]) + '\t')
    load.append(st)

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/Snow')
def predict_snow():
    snow = (str(round(snowY[0, 1] * 100, 2)))
    return {'snow': snow}

@app.route('/Rain')
def predict_rain():
    rain = (str(round(rainY[0, 1] * 100, 2)))
    return {'rain': rain}

@app.route('/Typhoon')
def predict_typhoon():
    typhoon = (str(round(typhoonY[0, 1] * 100, 2)))
    return {'typhoon': typhoon}

@app.route('/SnowLocation')
def predict_snowAnother():
    return {'loc0': snowLocation[0],
    'loc1': snowLocation[1],
    'loc2': snowLocation[2],
    'loc3': snowLocation[3],
    'loc4': snowLocation[4],
    'loc5': snowLocation[5],
    'loc6': snowLocation[6],
    'loc7': snowLocation[7]}

@app.route('/RainLocation')
def predict_rainAnother():
    return {'loc0': rainLocation[0],
    'loc1': rainLocation[1],
    'loc2': rainLocation[2],
    'loc3': rainLocation[3],
    'loc4': rainLocation[4],
    'loc5': rainLocation[5],
    'loc6': rainLocation[6],
    'loc7': rainLocation[7]}

@app.route('/CSV')
def lookup_csv():
    return {'load1': load[1]
    , 'load2': load[2]
    , 'load3': load[3]
    , 'load4': load[4]
    , 'load5': load[5]
    , 'load6': load[6]
    , 'load7': load[7]
    , 'load8': load[8]
    , 'load9': load[9]
    , 'load10': load[10]
    , 'load11': load[11]
    , 'load12': load[12]
    , 'load13': load[13]
    , 'load14': load[14]
    , 'load15': load[15]
    , 'load16': load[16]
    , 'load17': load[17]
    , 'load18': load[18]
    , 'load19': load[19]
    , 'load20': load[20]
    , 'load21': load[21]
    , 'load22': load[22]
    , 'load23': load[23]
    , 'load24': load[24]
    , 'load25': load[25]
    , 'load26': load[26]
    , 'load27': load[27]
    , 'load28': load[28]
    , 'load29': load[29]
    , 'load30': load[30]
    , 'load31': load[31]
    , 'load32': load[32] }

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000)