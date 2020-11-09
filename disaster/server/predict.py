import urllib.request as ul
import xmltodict
import json
import datetime as dt
import timedelta as td
import numpy as np
import pandas as pd

# Snow
# 지점 코드 (default: 대전)
# 서울 108 인천 112 대구 143 대전 133 부산 159 울산 152 광주 156 제주도 184 

locationCode = 133

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

weather = data_snow(20170101, 20171231, 133)
weather2 = data_snow(20190101, 20191231, 133) # 대전 지역 20180101 ~ 20200101 기상 데이터 조회
snowX = np.vstack((weather, weather2))

date = (dt.datetime.today() - td.Timedelta(days = 3)).strftime('%Y%m%d')
date2 = (dt.datetime.today() - td.Timedelta(days = 2)).strftime('%Y%m%d')
today = data_snow(date, date2, 133) # 오늘 기준 이틀전 날씨 조회

from pyspark.ml.classification import LogisticRegression

snowX = pd.DataFrame(snowX)
today = np.array(today)
snowX.dropna(inplace = True)

x = snowX[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
y = snowX[[12]]

today = today[0, 1:12]

from sklearn.model_selection import train_test_split

train, test = train_test_split(snowX, test_size=0.25)

print("Training Dataset Count: " + str(train.count()))
print("Test Dataset Count: " + str(test.count()))

lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)
lrModel = lr.fit(train)
predictions = lrModel.transform(test)

from pyspark.ml.evaluation import BinaryClassificationEvaluator

evaluator = BinaryClassificationEvaluator()
print('Test Area Under ROC', evaluator.evaluate(predictions))



# print("오늘 눈이 올 확률은 " + str(round(snowY[0, 1] * 100, 2)) + "% 입니다.")