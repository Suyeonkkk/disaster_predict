import pandas as pd

csv = pd.read_csv('./typhoon.csv', encoding = 'UTF-8')
csv = csv[['한글태풍명', '영문태풍명', '발생일시', '소멸일시']]

load = []
for i in range(0, 33):
    st = ''
    for j in range(0, 4):
        st += (str(csv.iat[i, j]) + '\t')
    load.append(st)

print(load)