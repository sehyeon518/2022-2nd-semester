import pickle
import matplotlib.pyplot as plt
from numpy import dot
from numpy.linalg import norm
import numpy as np


data = pickle.load(open("mid_animal_data_pub.pkl", "rb"))
# print(data)
# plt.imshow(data['train_images'][2]) # 2번 위치의 사진

# plt.show()

# print(data['train_images']) # 사진으로 생성한 numpy array
# data['train_vectors' 사진을 256차원의 벡터로 표현한 것
# data['train_images'][2]를 표현한 벡터

# data['train_labels'] 어떤 동물인지 나타내는 numpy
# 0 고양이  1 강아지  2 다람쥐
# data['test1_images']
# - 10 장의 사진으로 생성한 numpy array 입니다.
#
# data['test1_vectors']
# - data['test1_images'] 와 상응하는 벡터를 포함합니다. numpy array 입니다.
#
# data['test2_vectors']
# - 익명의 이미지 30장을 벡터로 변환하여 모아둔 numpy array 입니다.

# f, axarr = plt.subplots(10,1)
#
# for i in range(10):
#     axarr[i].imshow(data['test1_images'][i]) # 2번 위치의 사진
# plt.show()
def cosine_sim(a, b):
    return dot(a, b)/(norm(a)*norm(b))

v1 = data['train_vectors'][0]
max_data = 0

for i in range(10):
    v2 = data['test1_vectors'][i]
    if cosine_sim(v1, v2) > max_data:
        max_data = cosine_sim(v1, v2)
        print(i)
print(max_data)
# 0~9 중 8번 이미지

