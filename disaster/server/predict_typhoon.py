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
    request = ul.Request(url)
    response = ul.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        responseData = response.read()
        rD = xmltodict.parse(responseData)
        rDJ = json.dumps(rD)
        rDD = json.loads(rDJ)
        
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