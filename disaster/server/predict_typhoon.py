import urllib.request as ul
import xmltodict
import json
import datetime as dt
import timedelta as td
import pandas as pd
import numpy as np

def typhoonPredict(dateStart, dateEnd):
    url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt="+dateStart+ \
      "&endDt="+dateEnd+ \
      "&stnIds=184"
    # 데이터를 받을 url

    request = ul.Request(url)
    # url의 데이터를 요청함

    response = ul.urlopen(request)
    # 요청받은 데이터를 열어줌

    rescode = response.getcode()
    # 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

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
        if (size != 1):
            weather = [[0] * 8] * (size)
        else :
            weather = [[0] * 6]
        date = dt.datetime.strptime(dateStart, '%Y%m%d').date()

        if (size != 1):
            weather[0] = ['date', '1', '2', '3', '4', '5', '6', '7']
        else :
            size = 2
        for index in range(1, size):
            try:
                if (size == 2):
                    avgRhm = rDD['response']['body']['items']['item']['avgRhm']
                else:
                    avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
                # 평균 상대 습도
                if avgRhm is None:
                    avgRhm = 0
            except (TypeError, ValueError):
                avgRhm = 0

            try:
                if (size == 2):
                    avgPs = rDD['response']['body']['items']['item']['avgPs']
                else:
                    avgPs = rDD['response']['body']['items']['item'][index]['avgPs']
                # 평균 해면 기압
                if avgPs is None:
                    avgPs = 0
            except (TypeError, ValueError):
                avgPs = 0

            try:
                if (size == 2):
                    avgPa = rDD['response']['body']['items']['item']['avgPa']
                else:
                    avgPa = rDD['response']['body']['items']['item'][index]['avgPa']
                # 평균 현지 기압
                if avgPa is None:
                    avgPa = 0
            except (TypeError, ValueError):
                avgPa = 0

            try:
                if (size == 2):
                    avgWs = rDD['response']['body']['items']['item']['avgWs']
                else:    
                    avgWs = rDD['response']['body']['items']['item'][index]['avgWs']
                # 평균 풍속
                if avgWs is None:
                    avgWs = 0
            except (TypeError, ValueError):
                avgWs = 0

            try:
                if (size == 2):
                    sumRn = rDD['response']['body']['items']['item']['sumRn']
                else:   
                    sumRn = rDD['response']['body']['items']['item'][index]['sumRn']
                # 강수량
                if sumRn is None:
                    sumRn = 0
            except (TypeError, ValueError):
                sumRn = 0

            try:
                if (size == 2):
                    avgTa = rDD['response']['body']['items']['item']['avgTa']
                else:
                    avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
                # 평균 기온
                if avgTa is None:
                    avgTa = 0
            except (TypeError, ValueError):
                avgTa = 0

            if (size != 2):
                weather[index] = [str(date), avgRhm, avgPs, avgPa, avgWs, sumRn, avgTa, 0]
            else :
                weather[0] = [avgRhm, avgPs, avgPa, avgWs, sumRn, avgTa]
            date = date + td.Timedelta(days=1)
    return weather

weather = typhoonPredict('20120101', '20140101')
weather2 = typhoonPredict('20140101', '20160101')
weather3 = typhoonPredict('20160101', '20180101')
weather4 = typhoonPredict('20180101', '20200101')
weather = np.vstack((weather, weather2, weather3, weather4))

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

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

weather = np.array(weather)

x = weather[1:, 1:7]
y = weather[1:, 7]

x = x.astype(np.float64)
y = y.astype(np.float64)

weather = np.nan_to_num(weather)

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y)

# Logistic Regression
from sklearn.linear_model import LogisticRegression

log = LogisticRegression()
log.fit(x_train, y_train)
print("Logistic test data accuracy: ", format(log.score(x_test, y_test)))

date = (dt.datetime.today() - td.Timedelta(days = 2)).strftime('%Y%m%d')
answerX = typhoonPredict(date, date)

from sklearn.linear_model import LogisticRegression

log = LogisticRegression()
log.fit(x_scaled, y)

answerX = scaler.transform(answerX)

answerY = log.predict_proba(answerX)
print("오늘 태풍이 발생할 확률은 " + str(round(answerY[0, 1] * 100, 2)) + "% 입니다.")

"""
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/Typhoon')
def predict_typhoon():
    answer = (str(round(answerY[0, 1] * 100, 2)))
    return {'data': answer}

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000)
"""