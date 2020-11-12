import urllib.request as ul
import xmltodict
import json
import datetime as dt
import timedelta as td
import numpy as np
import pandas as pd

# 지점 코드 서울 인천 대구 대전 부산 울산 광주 제주 순서
locationList = [108, 112, 143, 133, 159, 152, 156, 184]

# 지역에 위치한 산의 높이 (km)
heightList = [0.7969, 0.6153, 1.3230, 0.7922, 1.1715, 2.1346, 1.2644, 0.5202]

def data_rain(start, end, index):
    url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
        "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
        "&numOfRows=999" \
        "&dataCd=ASOS" \
        "&dateCd=DAY" \
        "&startDt=" + str(start) + \
        "&endDt=" + str(end) + \
        "&stnIds=" + str(locationList[index])
    request = ul.Request(url)
    response = ul.urlopen(request)
    rescode = response.getcode()
    weather = [[]]

    if (rescode == 200):
        responseData = response.read()
        rD = xmltodict.parse(responseData)
        rDJ = json.dumps(rD)
        rDD = json.loads(rDJ)

        size = int(rDD['response']['body']['totalCount'])
        weather = [[0] * 18] * (size)
        date = str(start)
        date = dt.datetime(int(date[0:4]), int(date[4:6]), int(date[6:8])).date()

        for i in range(0, size):
            if (size == 1):
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
                if (hr1MaxIcsr is None):
                    hr1MaxIcsr = -99

                try:
                    sumGsr = rDD['response']['body']['items']['item']['sumGsr']
                    # sumGsr 합계 일사
                except TypeError:
                    sumGsr = -99
                if (sumGsr is None):
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
                if (sumLrgEv is None):
                    sumLrgEv = -99

                try:
                    sumSmlEv = rDD['response']['body']['items']['item']['sumSmlEv']
                    # sumSmlEv 합계 소형증발량
                except TypeError:
                    sumSmlEv = -99
                if (sumSmlEv is None):
                    sumSmlEv = -99

                try:
                    n99Rn = rDD['response']['body']['items']['item']['n99Rn']
                    # n99Rn 9-9 강수
                except TypeError:
                    n99Rn = -99
                if (n99Rn is None):
                    n99Rn = -99

                try:
                    sumRn = rDD['response']['body']['items']['item']['sumRn']
                    # sumRn 일강수량
                except TypeError:
                    sumRn = 0
                if (sumRn is None):
                    sumRn = 0
                if (float(sumRn) > 0):
                    sumRn = 1
            else:
                try:
                    avgTa = rDD['response']['body']['items']['item'][i]['avgTa']
                    # avgTa 평균 기온
                except TypeError:
                    avgTa = -99

                try:
                    minTa = rDD['response']['body']['items']['item'][i]['minTa']
                    # minTa 최저 기온
                except TypeError:
                    minTa = -99

                try:
                    maxTa = rDD['response']['body']['items']['item'][i]['maxTa']
                    # maxTa 최고 기온
                except TypeError:
                    maxTa = -99

                try:
                    avgTd = rDD['response']['body']['items']['item'][i]['avgTd']
                    # avgTd 평균 이슬점온도
                except TypeError:
                    avgTd = -99

                try:
                    minRhm = rDD['response']['body']['items']['item'][i]['minRhm']
                    # minRhm 최소 상대습도
                except TypeError:
                    minRhm = -99

                try:
                    avgRhm = rDD['response']['body']['items']['item'][i]['avgRhm']
                    # avgRhm 평균 상대습도
                except TypeError:
                    avgRhm = -99

                try:
                    ssDur = rDD['response']['body']['items']['item'][i]['ssDur']
                    # ssDur 가조시간
                except TypeError:
                    ssDur = -99

                try:
                    sumSsHr = rDD['response']['body']['items']['item'][i]['sumSsHr']
                    # sumSsHr 합계 일조 시간
                except TypeError:
                    sumSsHr = -99

                try:
                    hr1MaxIcsr = rDD['response']['body']['items']['item'][i]['hr1MaxIcsr']
                    # hr1MaxIcsr 1시간 최다 일사량
                except TypeError:
                    hr1MaxIcsr = -99

                try:
                    sumGsr = rDD['response']['body']['items']['item'][i]['sumGsr']
                    # sumGsr 합계 일사
                except TypeError:
                    sumGsr = -99

                try:
                    avgTca = rDD['response']['body']['items']['item'][i]['avgTca']
                    # avgTca 평균 전운량
                except TypeError:
                    avgTca = -99

                try:
                    avgLmac = rDD['response']['body']['items']['item'][i]['avgLmac']
                    # avgLmac 평균 중하층운량
                except TypeError:
                    avgLmac = -99

                try:
                    sumLrgEv = rDD['response']['body']['items']['item'][i]['sumLrgEv']
                    # sumLrgEv 합계 대형증발량
                except TypeError:
                    sumLrgEv = -99

                try:
                    sumSmlEv = rDD['response']['body']['items']['item'][i]['sumSmlEv']
                    # sumSmlEv 합계 소형증발량
                except TypeError:
                    sumSmlEv = -99

                try:
                    n99Rn = rDD['response']['body']['items']['item'][i]['n99Rn']
                    # n99Rn 9-9 강수
                except TypeError:
                    n99Rn = -99

                try:
                    sumRn = rDD['response']['body']['items']['item'][i]['sumRn']
                    # sumRn 일강수량
                except TypeError:
                    sumRn = 0
                if (sumRn is None):
                    sumRn = 0
                if (float(sumRn) > 0):
                    sumRn = 1

            weather[i] = [str(date), avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, heightList[index], sumRn]

            date = date + td.Timedelta(days = 1)
    return weather

weather = data_rain(20180101, 20191231, 0)
weather2 = data_rain(20180101, 20191231, 1)
weather3 = data_rain(20180101, 20191231, 2)
weather4 = data_rain(20180101, 20191231, 3)
weather5 = data_rain(20180101, 20191231, 4)
weather6 = data_rain(20180101, 20191231, 5)
weather7 = data_rain(20180101, 20191231, 6)
weather8 = data_rain(20180101, 20191231, 7)
weather = np.vstack((weather, weather2, weather3, weather4, weather5, weather6, weather7, weather8))
weather = pd.DataFrame(weather)
weather.dropna(inplace = True)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

x = weather[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
y = weather[[17]]

x = x.astype(np.float64)
y = y.astype(np.float64)

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y)
y_train = y_train.values.ravel()

# Logistic Regression
from sklearn.linear_model import LogisticRegression

log = LogisticRegression()
log.fit(x_train, y_train)
print("Logistic test data accuracy: ", format(log.score(x_test, y_test)))

# Decision Tree
from sklearn.tree import DecisionTreeClassifier

decision = DecisionTreeClassifier(max_depth = 4, random_state = 0)
decision.fit(x_train, y_train)
print("Decision Tree test data accuracy: ", format(decision.score(x_test, y_test)))

# Random Forest
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(max_depth=2, random_state=0)
forest.fit(x_train, y_train)
print("Random Forest test data accuracy: ", format(forest.score(x_test, y_test)))