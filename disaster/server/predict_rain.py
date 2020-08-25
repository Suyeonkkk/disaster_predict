import urllib.request as ul
import xmltodict
import json
import datetime as dt
import timedelta as td

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
    weather = [[0] * 16] * (size)
    date = dt.datetime(2012, 1, 1).date()

    weather[0] = ['date', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
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

        weather[index] = [str(date), avgTa, minTa, maxTa, minRhm, avgRhm, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, sumRn]

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
    weather2 = [[0] * 16] * (size)
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

        weather2[index] = [str(date), avgTa, minTa, maxTa, minRhm, avgRhm, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, sumRn]

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
    weather3 = [[0] * 16] * (size)
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

        weather3[index] = [str(date), avgTa, minTa, maxTa, minRhm, avgRhm, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, sumRn]

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
    weather4 = [[0] * 16] * (size)
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

        weather4[index] = [str(date), avgTa, minTa, maxTa, minRhm, avgRhm, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, sumRn]

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
    weather5 = [[0] * 16] * (size)
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

        weather5[index] = [str(date), avgTa, minTa, maxTa, minRhm, avgRhm, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, sumRn]

        date = date + td.Timedelta(days = 1)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, cross_validate
import numpy as np

weather = np.vstack((weather, weather2, weather3, weather4, weather5))
weather = np.array(weather)
x = weather[1:, 1:15]
y = weather[1:, 15]

x = x.astype(np.float64)
y = y.astype(np.float64)

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y)

# decision Tree
from sklearn.tree import DecisionTreeClassifier

decision = DecisionTreeClassifier(max_depth = 4, random_state = 0)
decision.fit(x_train, y_train)
print("Decision Tree test data accuracy: ", format(decision.score(x_test, y_test)))

scores = cross_val_score(decision, x_scaled, y, cv = 5)
print("Decision Tree scores: ", scores.mean())

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

answerX = [[avgTa, minTa, maxTa, minRhm, avgRhm, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn]]

from sklearn.linear_model import LogisticRegression

log = LogisticRegression()
log.fit(x_scaled, y)

answerX = scaler.transform(answerX)

answerY = log.predict_proba(answerX)
print("오늘 비가 올 확률은 " + str(round(answerY[0, 1] * 100, 2)) + "% 입니다.")