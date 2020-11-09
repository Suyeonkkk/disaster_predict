import urllib.request as ul
import xmltodict
import json
import pandas as pd
import datetime as dt
import timedelta as td
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

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
                if (sumLrgEv is None):
                    sumLrgEv = 0

                try:
                    sumSmlEv = rDD['response']['body']['items']['item']['sumSmlEv']
                    # sumSmlEv 합계 소형증발량
                except TypeError:
                    sumSmlEv = -99
                if (sumSmlEv is None):
                    sumSmlEv = 0

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

def data_rain(start, end, location):
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
        weather = [[0] * 17] * (size)
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
                    sumRn = 0
                if (sumRn is None):
                    sumRn = 0
                if (float(sumRn) > 0):
                    sumRn = 1

            weather[index] = [str(date), avgTa, minTa, maxTa, avgTd, minRhm, avgRhm, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, avgTca, avgLmac, sumLrgEv, sumSmlEv, n99Rn, sumRn]

            date = date + td.Timedelta(days = 1)
    return weather

def data_typhoon(start, end):
    url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList" \
      "?serviceKey=LAEin4h5h2HeNf9fuSWuorK2uW5MyuvoiWeJL3uSRZivdAzWhtcrCECKzSKrU9Dfwe8W6tdNR24tDTBZEPYiEQ%3D%3D" \
      "&numOfRows=999" \
      "&dataCd=ASOS" \
      "&dateCd=DAY" \
      "&startDt=" + str(start) + \
      "&endDt=" + str(end) + \
      "&stnIds=184"
    request = ul.Request(url)
    response = ul.urlopen(request)
    rescode = response.getcode()
    weather = [[]]
    
    if (rescode == 200):
        responseData = response.read()
        rD = xmltodict.parse(responseData)
        rDJ = json.dumps(rD)
        rDD = json.loads(rDJ)

        try:
            size = int(rDD['response']['body']['totalCount'])
        except KeyError:
            size = 1
        
        weather = [[0] * 8] * (size)
        date = str(start)
        date = dt.datetime(int(date[0:4]), int(date[4:6]), int(date[6:8])).date()

        for index in range(0, size):
            try:
                if (size == 1):
                    avgRhm = rDD['response']['body']['items']['item']['avgRhm']
                else:
                    avgRhm = rDD['response']['body']['items']['item'][index]['avgRhm']
                # 평균 상대 습도
                if avgRhm is None:
                    avgRhm = 0
            except (TypeError, ValueError):
                avgRhm = 0

            try:
                if (size == 1):
                    avgPs = rDD['response']['body']['items']['item']['avgPs']
                else:
                    avgPs = rDD['response']['body']['items']['item'][index]['avgPs']
                # 평균 해면 기압
                if avgPs is None:
                    avgPs = 0
            except (TypeError, ValueError):
                avgPs = 0

            try:
                if (size == 1):
                    avgPa = rDD['response']['body']['items']['item']['avgPa']
                else:
                    avgPa = rDD['response']['body']['items']['item'][index]['avgPa']
                # 평균 현지 기압
                if avgPa is None:
                    avgPa = 0
            except (TypeError, ValueError):
                avgPa = 0

            try:
                if (size == 1):
                    avgWs = rDD['response']['body']['items']['item']['avgWs']
                else:    
                    avgWs = rDD['response']['body']['items']['item'][index]['avgWs']
                # 평균 풍속
                if avgWs is None:
                    avgWs = 0
            except (TypeError, ValueError):
                avgWs = 0

            try:
                if (size == 1):
                    sumRn = rDD['response']['body']['items']['item']['sumRn']
                else:   
                    sumRn = rDD['response']['body']['items']['item'][index]['sumRn']
                # 강수량
                if sumRn is None:
                    sumRn = 0
            except (TypeError, ValueError):
                sumRn = 0

            try:
                if (size == 1):
                    avgTa = rDD['response']['body']['items']['item']['avgTa']
                else:
                    avgTa = rDD['response']['body']['items']['item'][index]['avgTa']
                # 평균 기온
                if avgTa is None:
                    avgTa = 0
            except (TypeError, ValueError):
                avgTa = 0

            weather[index] = [str(date), avgRhm, avgPs, avgPa, avgWs, sumRn, avgTa, 0]
            date = date + td.Timedelta(days=1)
    return weather

# 지점 코드 (default: 대전)
locationCodeList = [108, 112, 143, 133, 159, 152, 156, 184]
date = (dt.datetime.today() - td.Timedelta(days = 2)).strftime('%Y%m%d')

# snow

# weather = data_snow(20120101, 20131231, 133)
# weather2 = data_snow(20140101, 20151231, 133)
# weather3 = data_snow(20160101, 20171231, 133)
# weather4 = data_snow(20180101, 20191231, 133)
# weather = np.vstack((weather, weather2, weather3, weather4))
# weather = pd.DataFrame(weather)
# weather.dropna(inplace = True)

# x = weather[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
# y = weather[[12]]

# x = x.astype(np.float64)
# y = y.astype(np.float64)

# scaler = StandardScaler()
# x_scaled = scaler.fit_transform(x)

# log = LogisticRegression()
# log.fit(x_scaled, y.values.ravel())

# snowLocation = []
# for index in locationCodeList:
#     snowX = np.array(data_snow(date, date, index))
#     snowX = np.nan_to_num(snowX[0, 1:12])
    
#     print(snowLocation)
#     print(snowX)
#     snowX = scaler.transform(snowX.reshape(1, -1))
#     snowY = log.predict_proba(snowX)
#     snowLocation.append(str(round(snowY[0, 1] * 100, 2)))

# # rain

# weather = data_rain(20120101, 20131231, 133)
# weather2 = data_rain(20140101, 20151231, 133)
# weather3 = data_rain(20160101, 20171231, 133)
# weather4 = data_rain(20180101, 20191231, 133)
# weather = np.vstack((weather, weather2, weather3, weather4))
# weather = pd.DataFrame(weather)
# weather.dropna(inplace = True)

# x = weather[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
# y = weather[[16]]

# x = x.astype(np.float64)
# y = y.astype(np.float64)

# scaler = StandardScaler()
# x_scaled = scaler.fit_transform(x)

# log = LogisticRegression()
# log.fit(x_scaled, y.values.ravel())

# rainLocation = []
# for index in locationCodeList:
#     rainX = np.array(data_rain(date, date, index))
#     rainX = np.nan_to_num(rainX[0, 1:16])
    
#     print(rainLocation)
#     print(rainX)
#     rainX = scaler.transform(rainX.reshape(1, -1))
#     rainY = log.predict_proba(rainX)
#     rainLocation.append(str(round(rainY[0, 1] * 100, 2)))

# typhoon

weather = data_typhoon(20120101, 20131231)
weather2 = data_typhoon(20140101, 20151231)
weather3 = data_typhoon(20160101, 20171231)
weather4 = data_typhoon(20180101, 20191231)
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

weather = np.array(weather)

x = weather[:, 1:7]
y = weather[:, 7]

x = x.astype(np.float64)
y = y.astype(np.float64)

weather = np.nan_to_num(weather)

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

date = (dt.datetime.today() - td.Timedelta(days = 2)).strftime('%Y%m%d')
typhoonX = np.array(data_typhoon(date, date))
typhoonX = np.nan_to_num(typhoonX[0, 1:7])

log = LogisticRegression()
log.fit(x_scaled, y)

typhoonX = scaler.transform(typhoonX.reshape(1, -1))
typhoonY = log.predict_proba(typhoonX)



from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/Snow')
def predict_snow():
    snow = snowLocation[3]
    return {'snow': snow}

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

@app.route('/Rain')
def predict_rain():
    rain = rainLocation[3]
    return {'rain': rain}

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

@app.route('/Typhoon')
def predict_typhoon():
    typhoon = (str(round(typhoonY[0, 1] * 100, 2)))
    return {'typhoon': typhoon}

@app.route('/CSV')
def lookup_csv():
    csv = pd.read_csv('./typhoon.csv', encoding = 'UTF-8')
    csv = csv[['한글태풍명', '영문태풍명', '발생일시', '소멸일시']]

    load = []
    for i in range(0, 33):
        st = ''
        for j in range(0, 4):
            st += (str(csv.iat[i, j]) + '\t')
        load.append(st)

    return {'load0': load[0]
    , 'load1': load[1]
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