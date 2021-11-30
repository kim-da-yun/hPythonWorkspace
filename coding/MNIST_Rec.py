#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys, os # 폴더 정리, 파일 정리 등 관련 라이브러리
sys.path.append(os.pardir)
import numpy as np
import pickle # 이미지 처리, 파일 정리 등에 사용되는 라이브러리
# dataset 폴더의 mnist 파일 안에 load_mnist 함수를 가져다 씀
from dataset.mnist import load_mnist


# In[2]:


def sigmoid(x):
    return 1 / (np.exp(-x))


# In[3]:


def softmax(a):
    c = np.max(a)
    return np.exp(a-c)/np.sum(np.exp(a-c))


# In[4]:


# 데이터를 가져오는 코드
#load_mnist 함수를 통해서 훈련 데이터와 테스트 데이터(이미지와 정답값으로 이루어진)를 가져옴
def get_data():
    # x: 이미지, t/t: 정답 0 ~ 9로 표현 (one-hot vector로 표현한게 아님, 숫자로 표현한 것임)   
    (x_train, y_train), (x_test, t_test) = load_mnist(normalize = True, flatten = True, one_hot_label = False) # (이미지, 정답), (이미지, 정답)
    # normalize: 값을 0 ~ 1로 정규화시킴, flatten: (28.28)을 쭉 펼쳐서 784차원의 데이터로 바꿈
    # one_hot vector: 어떤 값을 표현할 때 해당하는 도메인만 1이고 나머지는 0으로 표현, 여기선 그냥 숫자로 표시되어 있음
    return x_test, t_test


# In[5]:


def init_network():
    # 미리 train 된 값을 가져옴
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


# In[6]:


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3'] # 키 값을 기반으로 w1, w2, w3 value를 가져오겠다
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    
    return y


# In[7]:


x, t = get_data()
network = init_network()
accuracy_cnt = 0


# In[8]:


for i in range(len(x)): # x의 길이만큼 반복
    # y: one-hot vector의  softmax 추론 결과,
    # network: 사전에 훈련시킨 네트워크의 가중치 값
    # x[i]: i번째 test 이미지
    y = predict(network, x[i]) # x[i]는 이미지임
    # np.argmax: y의 softmax 결과 중에서 확률이 가장 높은 원소의 인덱스를 출력
    p = np.argmax(y) # 어떤 벡터에서 제일 최대가 되는 값의 위치를 뽑아줌
    if p == t[i]: # p가 정답과 같으면 / t[i]는 정답을 0 ~ 9로 표현한 것
        accuracy_cnt += 1


# In[9]:


print("Accuracy:" + str(float(accuracy_cnt) / len(x)))


# In[ ]:




