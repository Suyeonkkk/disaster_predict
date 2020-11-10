import urllib.request as ul
import xmltodict
import json
import pandas as pd
import datetime as dt
import timedelta as td
import numpy as np

def data_snow(start, end, location):
    url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
        "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
        "&numOfRows=999" \
        "&dataCd=ASOS" \
        "&dateCd=DAY" \
        "&startDt=" + str(start) + \
        "&endDt=" + str(end) + \
        "&stnIds=" + str(location)
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
        weather = [[0] * 13] * (size)
        date = str(start)
        date = dt.datetime(int(date[0:4]), int(date[4:6]), int(date[6:8])).date()

        for index in range(0, size):
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
                    ddMefs = rDD['response']['body']['items']['item']['ddMefs']
                    # ddMefs 일 최심신적설
                except TypeError:
                    ddMefs = -99
                if (ddMefs is None):
                    ddMefs = 0
                if (float(ddMefs) > 0):
                    ddMefs = 1
            else:
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
                    ddMefs = rDD['response']['body']['items']['item'][index]['ddMefs']
                    # ddMefs 일 최심신적설
                except TypeError:
                    ddMefs = -99
                if (ddMefs is None):
                    ddMefs = 0
                if (float(ddMefs) > 0):
                    ddMefs = 1

            weather[index] = [str(date), avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, avgTca, avgLmac, sumLrgEv, sumSmlEv, ddMefs]
            date = date + td.Timedelta(days = 1)
    return weather

weather = data_snow(20120101, 20131231, 133)
weather2 = data_snow(20140101, 20151231, 133) # 대전 지역 20180101 ~ 20200101 기상 데이터 조회
weather3 = data_snow(20160101, 20171231, 133)
weather4 = data_snow(20180101, 20191231, 133)
weather = np.vstack((weather, weather2, weather3, weather4))

date = (dt.datetime.today() - td.Timedelta(days = 2)).strftime('%Y%m%d')
snowX = data_snow(date, date, 133)
snowX = np.array(snowX)
snowX = snowX[0, 1:12]

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

weather = pd.DataFrame(weather)
weather.dropna(inplace = True)

x = weather[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
y = weather[[12]]

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

log = LogisticRegression()
log.fit(x_scaled, y.values.ravel())

snowX = snowX.reshape(1, -1)
snowX = scaler.transform(snowX)

snowY = log.predict_proba(snowX)
print("오늘 눈이 올 확률은 " + str(round(snowY[0, 1] * 100, 2)) + "% 입니다.")

# from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route('/Snow')
# def predict_rain():
#     snow = (str(round(snowY[0, 1] * 100, 2)))
#     return {'snow': snow}

# if __name__ == '__main__':
#     app.run(host = '127.0.0.1', port = 5000)