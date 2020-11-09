import pandas as pd

csv = pd.read_csv('./typhoon.csv', encoding = 'UTF-8')
csv = csv[['한글태풍명', '영문태풍명', '발생일시', '소멸일시']]

load = []
for i in range(0, 33):
    st = ''
    for j in range(0, 4):
        st += (str(csv.iat[i, j]) + ' ')
    load.append(st)

print(load[30])

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/CSV')
def lookup_csv():
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
    , 'load32': load[32]
    }

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000)