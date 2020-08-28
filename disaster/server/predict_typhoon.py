import urllib.request as ul
import xmltodict
import json
import datetime as dt
import timedelta as td
import pandas as pd
import numpy as np

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

csv = pd.read_csv('./typhoon.csv', encoding = 'CP949')
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

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, cross_validate

weather = np.array(weather)
x = weather[1:, 1:7]
y = weather[1:, 7]

x = x.astype(np.float64)
y = y.astype(np.float64)

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y)

# decision Tree
from sklearn.tree import DecisionTreeClassifier

# decision = DecisionTreeClassifier(max_depth = 4, random_state = 0)
# decision.fit(x_train, y_train)
# print("Decision Tree test data accuracy: ", format(decision.score(x_test, y_test)))

# scores = cross_val_score(decision, x_scaled, y, cv = 5)
# print("Decision Tree scores: ", scores.mean())

# # K-NN
# from sklearn.neighbors import KNeighborsClassifier

# nearest = KNeighborsClassifier(n_neighbors = 3)
# nearest.fit(x_train, y_train)
# print("KNN test data accuracy: ", format(nearest.score(x_test, y_test)))

# scores = cross_val_score(nearest, x_scaled, y, cv = 5)
# print("KNN scores: ", scores.mean())

# # SVM
# import sklearn.svm as svm

# svm_clf = svm.SVC(kernel = 'rbf')
# svm_clf.fit(x_train, y_train)
# print("SVM test data accuracy: ", format(svm_clf.score(x_test, y_test)))

# scores = cross_val_score(svm_clf, x_scaled, y, cv = 5)
# print("SVM scores: ", scores.mean())

# # Logistic Regression
# from sklearn.linear_model import LogisticRegression

# log = LogisticRegression()
# log.fit(x_train, y_train)
# print("Logistic test data accuracy: ", format(log.score(x_test, y_test)))

# scores = cross_val_score(log, x_scaled, y, cv = 5)
# print("Logistic scores: ", scores.mean())

# # Random Forest
# from sklearn.ensemble import RandomForestClassifier

# forest = RandomForestClassifier(n_estimators = 10)
# forest.fit(x_train, y_train)
# print("Random Forest test data accuracy: ", format(forest.score(x_test, y_test)))

# scores = cross_val_score(forest, x_scaled, y, cv = 5)
# print("Random Forest scores: ", scores.mean())

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

answerX = [[avgRhm, avgPs, avgPa, avgWs, sumRn, avgTa]]

from sklearn.linear_model import LogisticRegression

log = LogisticRegression()
log.fit(x_scaled, y)

answerX = scaler.transform(answerX)

answerY = log.predict_proba(answerX)
print("오늘 태풍이 발생할 확률은 " + str(round(answerY[0, 1] * 100, 2)) + "% 입니다.")

# from flask import Flask, request, jsonify, render_template

# app = Flask(__name__)

# @app.route("/")
# def hello():                           
#     return "<h1>Hello World!</h1>"

# @app.route('/TyphoonInfo')
# def predict_typhoon():
#     answer = (str(round(answerY[0, 1] * 100, 2)))
#     return "<p>" + answer + "</p>"

# if __name__ == '__main__':
#     app.run(host = '127.0.0.1', port = 5000)

# venv\Scripts\activate
