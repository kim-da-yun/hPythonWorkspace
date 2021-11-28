#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 신경망 함수
import numpy as np


# In[2]:


# 평균 제곱 오차
def mean_squared_error(y, t):
    return 0.5 * np.sum( (y-t)**2)


# In[3]:


y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]


# In[4]:


t = [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


# In[5]:


mean_squared_error(np.array(y), np.array(t))


# In[7]:


# 교차 엔트로피 오차  
def cross_entropy_error(y, t):
    # log0 = 무한대임으로 - 값으로 가는 걸 막기 위헤 미세한 값을 넣어줘야 됨
    delta = 1e-7 # 0.00000000001이어도 됨, 미세한 값을 넣어주기
    return -np.sum(t*np.log(y + delta))


# In[8]:


cross_entropy_error(np.array(y), np.array(t))


# In[9]:


# 미분
def numerical_diff(f, x):
    h = 1e-4 # h를 순간적으로 아주 작은 값으로 해야되니깐 10^(-4)
    return (f(x + h) - f(x - h))/(2 * h)


# In[10]:


# 예제, y = 0.01*x**2 + 0.1x 함수에 대한 수치 미분값
def function_1(x):
    return 0.01*x**2 + 0.1*x


# In[11]:


numerical_diff(function_1, 5) # x = 5


# In[12]:


# function_1의 그래프
import matplotlib.pylab as plt


# In[13]:


x = np.arange(0.0, 20.0, 0.1) # 0 ~ 20, 범위는 0.1씩
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()


# In[14]:


numerical_diff(function_1, 10)


# In[15]:


numerical_diff(function_1, 15)


# In[16]:


# 편미분
def function_tmp1(x0):
    return x0*x0 + (4)**2 # x0** + x1**2


# In[17]:


numerical_diff(function_tmp1, 3.0)


# In[18]:


# x0 = 3, x1 = 4일 때 x1에 대한 편미분값을 구하시오
def function_tmp2(x1):
    return (3)**2 + x1*x1


# In[19]:


numerical_diff(function_tmp2, 4)


# In[20]:


# 기울기
def function_2(x):
    # 벡터: 순서쌍,  x0, x1 두 변수로 이루어진 변수쌍.
    return x[0]**2 + x[1]**2 # 벡터


# In[21]:


# 편미분을 다 합친 기울기(gradient)
def numerical_gradient(f, x): # 인자: x 값과 그거에 대한 함수값인 f
    h = 1e-4 # 10^(-4)
    grad = np.zeros_like(x) # x의 shape를 받아서 0으로 초기화 시킴
    
    for idx in range(x.size): # x의 크기만큼 반복
        # 수치미분 공식 사용
        tmp_val = x[idx] # x[idx] = 1.0이면
        # x + h와 해당하는 f값
        x[idx] = tmp_val + h # x[idx] = 1.0004
        #f(x) # f로 입력받았지만 함수처럼 쓸 수 있음. x에 idx를 넣으면 해당하는 인덱스 값(tmp_val + h)으로 업데이트 됨
        fxh1 = f(x) # f(x+h)
        # x-h와 해당하는 f값
        x[idx] = tmp_val - h
        fxh2 = f(x) # f(x-h)
        # 최종 기울기 값(gradient)
        grad[idx] = (fxh1 - fxh2)/(2*h)
        x[idx] = tmp_val # 값 복원
        
    return grad


# In[22]:


numerical_gradient(function_2, np.array([3.0, 4.0]))


# In[23]:


numerical_gradient(function_2, np.array([0.0, 2.0]))


# In[24]:


numerical_gradient(function_2, np.array([2.0, 0.0]))


# In[25]:


# 경사하강법
def gradient_descent(f, init_x, lr = 0.01, step_num = 100): # 입력값, 초기값, learning rate(학습률, 에타), 몇번 이동할지(스텝)
    x = init_x # 초기값: 탐색을 시작하는 지점
    
    for i in range(step_num):
        # 편미분값
        grad = numerical_gradient(f, x)
        x = x - lr * grad # x -= lr*grad
        
    return x


# In[26]:


# 예제, f(x0, x1) = x0**2 + x1**2
init_x = np.array([-3.0, 4.0])


# In[27]:


gradient_descent(function_2, init_x = init_x, lr = 0.1, step_num = 100)


# In[ ]:




