#!/usr/bin/env python
# coding: utf-8

# In[4]:


kor = [60,70,80,50,90]
math = [77,88,99,55,66]
eng = [90,90,90,80,80]
score = [kor, math, eng]
for i in score:
    print(sum(i)/len(i))
for i in range(5):
    sum = kor[i] + math[i] + eng[i]
    print(sum/3)


# In[6]:


a = int(input())
for i in range(1,10):
    print(a, 'x', i, '=', a*i)


# In[8]:


import random
a = random.randint(1, 1000)
print(a)


# In[10]:


import random as ra
a = ra.randint(1,1000)
print(a)


# In[17]:


import pandas as pd

df = pd.read_csv('auto-mpg.csv', header=None) # 헤더가 없는 파일이기 때문에 첫번 째 행을 colunmn 이름으로 지정을 안하기 위해 
print(df)


# In[16]:


import pandas as pd

df = pd.read_csv('auto_mpg.csv', header=None) # 헤더가 없는 파일이기 때문에 첫번 째 행을 colunmn 이름으로 지정을 안하기 위해 
print(df)


# In[19]:


df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
             'acceleration', 'mode year', 'origin', 'name' ] # 열 이름 리스트로 해서 지정
print(df)


# In[20]:


print(df.head()) # 위에서 5번째줄까지만 출력함


# In[21]:


print(df.tail())# 뒤쪽에서부터 5번째줄까지만 출력


# In[24]:


print(df.shape)# 데이터프레임이 갖고 있는 모양, 크기 정보 확인


# In[25]:


print(df.info())# 데이터프레임 기본 정보 확인


# In[28]:


print(df.dtypes)# 데이터프레임 자료형(타입), 열이 저장하고 있는 타입만 보여줌


# In[29]:


print(df.dtypes[5])# 데이터프레임 특정 열의 자료형(타입)이 알고싶을 때 해당 열만 보여줌


# In[30]:


print(df.dtypes['weight'])


# In[31]:


print(df.describe()) # column별로 요약해서 보여주는 메소드, 수치로 표현된 colunmn만 나옴
#float, integer 부분만 뽑아서 기술 통계로 만들어서 출력해줌


# In[32]:


print(df.count()) # 데이터 갯수, 전체 데이터 프레임의 모든 열에 대한 것


# In[33]:


print(df.count().mpg) 
# 특정 값의 갯수 출력, 특정한 열에 대해 처리할 때는 시리즈에 접근하는 방식으로 가져오면 됨


# In[34]:


print(type(df.count())) 


# In[37]:


unique_values = df['origin'].value_counts() # 특정 열이 선택되며 그 열만을 뽑아내면 시리즈 데이터가 넘어옴
# 해당 column에 사용되고 있는 고유한 값들을 unique_values라는 변수에 저장
print(unique_values)
# 시리즈에 사용되는 앞쪽의 값은 해당 column에 unique한 값들의 인덱스 값이 올 것임
# 해당 인덱스에 대한 갯수가 출력됨


# In[38]:


print(type(unique_values))


# In[39]:


unique_values = df['cylinders'].value_counts() # 실린더 각각의 갯수별로 전체 데이터가 몇개씩이 분포가 되어있느냐
print(unique_values)


# In[40]:


df.mean() # 주피터 노트북은 환경이 인터프린터라 바로 결과가 나옴


# In[41]:


print(df.mean()) # 숫자가 적용되어 있는 열에 대해서만 평균을 낼 수 있음


# In[42]:


print(df.mpg.mean()) # = df['mpg'].mean


# In[43]:


print(df[['mpg','weight']].mean()) # 여러 개의 열을 선택해서 그 부분의 평균을 구할 때 리스트를 사용함


# In[45]:


print(df.median()) # 저장되어 있는 상태에서 순서대로 놨을 때 가운데 값을 구할 때, 모든 열 중에서 


# In[52]:


print(df['mpg'].median()) # 특정 열 중에서 가운데 값 구할 때


# In[51]:


print(df[['mpg','cylinders']].median()) # 특정 열 여러개 중에서 가운데 값 구할 때


# In[53]:


print(df.max()) # 특정 열에 대한 최대값을 구할 때는 위처럼 열 지정 해주고 값을 구하면 됨


# In[54]:


print(df.min())


# In[55]:


print(df.std()) # 표준편차


# In[56]:


print(df.corr())# 상관계수: 두 개의 열 사이에 관계가 있냐, 둘 사이의 데이터의 분포가 한 쪽이 커졌을 때 다른쪽이 커지냐


# In[ ]:




