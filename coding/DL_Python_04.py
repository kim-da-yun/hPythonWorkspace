#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def sigmoid(x):
    return 1 / np.exp(-x)


# In[2]:


# 예를 들어 a = np.array([10, 10, 5])
def softmax(a):
    return np.exp(a) / np.sum(np.exp(a)) # a에 각각의 array 각각 들어감(10, 10,5)
# 결과값: [np.exp(10) / np.sum(np.exp(10) + np.exp(10) + np.exp(5)),
#         np.exp(10) / np.sum(np.exp(10) + np.exp(10) + np.exp(5)),
#         np.exp(10) / np.sum(np.exp(10) + np.exp(10) + np.exp(5))]


# In[3]:


def softmax_(a):
    c = np.max(a) # 예) exp 10000
    return np.exp(a-c) / np.sum(np.exp(a-c))


# In[4]:


aa = np.array([1000, 10000])
softmax(aa)


# In[5]:


softmax_(aa)


# In[6]:


def init_network():
    network = {}
    # 행: 입력 노드 수, 열: 출력 노드 수
    network['w1'] = np.array([[0.2,0.2,0.2,0.2,0.2],
                              [0.2,0.2,0.2,0.2,0.2],
                              [0.2,0.2,0.2,0.2,0.2]]) # 3행 5열 
    # bias의 갯수: 출력 노드 수만큼
    network['b1'] = np.array([0,0,0,0,0])
    network['w2'] = np.array([[0.3,0.3,0.3,0.3,0.3],
                              [0.3,0.3,0.3,0.3,0.3],
                              [0.3,0.3,0.3,0.3,0.3],
                             [0.3,0.3,0.3,0.3,0.3],
                              [0.3,0.3,0.3,0.3,0.3]])
    network['b2'] = np.array([0,0,0,0,0])
    network['w3'] = np.array([[0.4,0.4,0.4],
                              [0.4,0.4,0.4], 
                              [0.4,0.4,0.4], 
                              [0.4,0.4,0.4], 
                              [0.4,0.4,0.4]])
    network['b3'] = np.array([0,0,0])
    
    return network


# In[7]:


def forward(network, x):
    w1, w2, w3 = network['w1'], network['w2'], network['w3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, w1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, w3) + b3
    y = softmax(a3)
    
    return y


# In[8]:


network = init_network()
x = np.array([0.1,0.1,0.1])
y = forward(network, x)
print(y)


# In[9]:


# 소프트맥스 함수 구현 시 어려운 점
# 1. 오버플로우에 주의
np.exp(1000) 


# In[10]:


np.exp(10000)


# In[ ]:




