#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# 2층에서 출력층으로서의 신호 전달
def sigmoid(x):
    return 1 / (np.exp(-x))


# In[3]:


def relu(x):
    return np.maximum(0, x)


# In[4]:


# 처음에 값을 넣는 함수를 생성
def init_network():
    network = {} # 딕셔너리 생성
    network['w1'] = np.array([[0.1, 0.2, 0.1],[0.2,0.1,0.2]]) # w1에 해당하는 key와 value 값 생성
    network['b1'] = np.array([0.1,0.2,0.3]) # 바이어스는 출력 갯수에 맞게    
    network['w2'] = np.array([[0.1,0.5],[0.3,0.2],[0.2,0.4]]) # 3행 2열
    network['b2'] = np.array([0.3,0.4]) # 출력 갯수가 2개니깐 1행 2열
    network['w3'] = np.array([[0.3,0.1],[0.2,0.1]])
    network['b3'] = np.array([0.2,0.1]) 
    
    return network


# In[5]:


def forward(network, x): # 인자: 출력이 된 network, x
    w1, w2, w3 = network['w1'], network['w2'], network['w3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, w1) + b1
    z1 = sigmoid(a1) # 활성함수(sigmoid)를 적용하면 z1 값이 나옴
    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, w3) + b3
    y = relu(a3)
    
    return y


# In[6]:


network = init_network()
x = np.array([2.0, 5.1])
y = forward(network, x)
print(y)

