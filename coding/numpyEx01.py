#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x = np.array([1.0,2.0,3.0])
print(x)


# In[3]:


type(x)


# In[8]:


x = np.array([1.0,2.0,3.0])
y = np.array([2.0,4.0,6.0])
x + y


# In[9]:


x - y


# In[10]:


x * y


# In[11]:


x / y


# In[12]:


# 브로드캐스트(broadcast):  차원을 자동적으로 늘려서 자동연산해주는 방식 / 한 개의 원소만 사용해서 연산 가능하게 함
x = np.array([1.0,2.0,3.0])
x / 2.0


# In[13]:


x = np.array([1.0,2.0,3.0]) # 위와 동일함
y = np.array([2.0,2.0,2.0])
x/ y 


# In[15]:


A = np.array([[1,2], [3,4]])
print(A)


# In[16]:


A.shape # A의 행렬의 크기


# In[17]:


A.dtype


# In[18]:


B = np.array([[3,0], [0,6]])
A + B


# In[19]:


A * B


# In[22]:


X = np.array([[51,55], [14,19], [0,4]])
print(X)


# In[23]:


X[0]


# In[24]:


X[1]


# In[25]:


X[2]


# In[26]:


X[0][1]


# In[27]:


Y = X.flatten() # 리스트를 하나하나 분리


# In[28]:


print(Y)


# In[30]:


Y > 15


# In[31]:


Y[Y>15]


# In[33]:


# matplotlib를 사용해서 그래프 그리기
import matplotlib.pyplot as plt


# In[34]:


x = np.arange(0, 6, 0.1) # 원소 나열, 0~6까지 보는데 0.1 간격으로 봐라
y = np.sin(x)


# In[35]:


plt.plot(x,y)
plt.show()


# In[36]:


x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)


# In[40]:


plt.plot(x, y1,label='sin')
plt.plot(x, y2,linestyle='--', label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin & cos')
plt.legend() # sin이 - cos-- 이거라는 표시, 그래프 표시
plt.show()


# In[ ]:




