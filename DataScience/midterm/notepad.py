import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import sys
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import os

meta = pd.read_csv('gts-seoul.csv')
# meta.loc[ [2103], ['습도', '풍속', '현지기압', '기온', '이슬점 온도'] ]
meta = meta[['습도', '풍속', '현지기압', '기온', '이슬점 온도'] ]

temp = meta['이슬점 온도']
# print(temp)

def pearson_similarity(u1, u2):
    u1_c = u1 - u1.mean()
    u2_c = u2 - u2.mean()
    denom = np.sqrt(np.sum(u1_c ** 2) * np.sum(u2_c ** 2))
    if denom != 0:
        return np.sum(u1_c * u2_c)/denom
    else:
        return 0


hum = meta['습도']
win = meta['풍속']
pre = meta['현지기압']
tem = meta['기온']

# print(pearson_similarity(hum, temp) + pearson_similarity(win, temp) + pearson_similarity(pre, temp) + pearson_similarity(tem, temp))

# plt.subplot(221)
# plt.scatter(hum, temp, label="hum")
# plt.legend()
#
# plt.subplot(222)
# plt.scatter(win, temp, label="wind")
# plt.legend()
#
# plt.subplot(223)
# plt.scatter(pre, temp, label="hpa")
# plt.legend()
#
# plt.subplot(224)
# plt.scatter(tem, temp, label="temp")
# plt.legend()
# plt.show()

meta = meta.loc[meta['현지기압'] >= 200, :]
print(meta)

hum = meta['습도']
win = meta['풍속']
pre = meta['현지기압']
tem = meta['기온']
temp = meta['이슬점 온도']
# print(pearson_similarity(hum, temp) + pearson_similarity(win, temp) + pearson_similarity(pre, temp) + pearson_similarity(tem, temp))

plt.subplot(221)
plt.scatter(hum, temp, label="hum")
plt.legend()

plt.subplot(222)
plt.scatter(win, temp, label="wind")
plt.legend()

plt.subplot(223)
plt.scatter(pre, temp, label="hpa")
plt.legend()

plt.subplot(224)
plt.scatter(tem, temp, label="temp")
plt.legend()
plt.show()

x = pd.DataFrame(meta, columns=['습도', '풍속', '현지기압', '기온'])
y = pd.DataFrame(meta, columns=['이슬점 온도'])
lr = LinearRegression()
lr.fit(x, y)

