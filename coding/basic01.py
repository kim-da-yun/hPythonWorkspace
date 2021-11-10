#!/usr/bin/env python
# coding: utf-8

# In[1]:


3 ** 2 # 3^2 3의 2승


# In[2]:


type(2.7)


# In[3]:


# list : 배열과 유사하게 사용되지만 데이터 타입을 모두 원소로 가질 수 있는 파이썬의 새로운 데이터 타입
a = [1,2,3,4]
print(a)


# In[4]:


len(a)


# In[5]:


a[-1] # 뒤에서 첫번째 자리


# In[6]:


b = [1,2,3,'c']
print(b)


# In[7]:


b[-1]


# In[8]:


type(b[-1])


# In[9]:


# slicing: list의 일부 데이터들을 가져올 수 있는 방법
print(a)


# In[10]:


a[0:2]


# In[11]:


a[1:]


# In[12]:


a[1:-2]


# In[13]:


# dictionary : key 값과 해당하는 value 값을 한쌍으로 해서 정의하는 데이터 타입, { : }
me = {'height':180}
me['height']


# In[14]:


me['height'] = 70


# In[15]:


print(me)


# In[16]:


me['weight'] = 100
print(me)


# In[17]:


# bool: true 혹은 false로 나타내는 참 거짓 데이터 타입
hungry = True
sleepy = False


# In[19]:


type(hungry)


# In[20]:


hungry


# In[21]:


not hungry


# In[22]:


not sleepy


# In[23]:


hungry and sleepy


# In[24]:


hungry or sleepy


# In[26]:


# if문: 논리 연산을 사용해서 문장의 조건적 실행을 결정하는 구문
if not hungry:
    print("I am hungry")
else:
    print("I am not hungry")
    print("나는 배고프지 않아")


# In[27]:


# for: 조건을 만족하는 loop 동안 반복 실행하게 하는 구문
for i in [1,2,3]:
    print(i)


# In[28]:


sum = 0
for i in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + i
print(sum)


# In[29]:


sum = 0
for i in range(1,11):
    sum = sum + i
print(sum)


# In[30]:


# 함수: 프로그램에서 반복실행되는 부분을 모듈화해서 반복사용을 피하는 효율적 방법
def hello():
    print("hello world")


# In[31]:


hello()


# In[32]:


def sum():
    sum = 0
    for i in range(1,11):
        sum = sum + i
    return sum


# In[33]:


sum()


# In[ ]:




