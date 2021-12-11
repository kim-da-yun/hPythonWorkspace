#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_excel('학년별·학급별 학생수(초) 2019.xlsx')
df2 = pd.read_excel('학년별·학급별 학생수(초) 2020.xlsx')


# In[2]:


# <1> 2020년 시도교육청별
# <1-1>1학년 학생 수 최저 10개 학교, 최고 10개 학교
# <1-2>교원 1인당 학생 수 최저 10개 학교, 최고 10개 학교
# 출력 : 학교 명, 학생 수, 지역, 그래프


# In[3]:


# <1-1>
# 1학년 데이터 전처리
df2 = df2.fillna(method = 'ffill')
print(df2.columns)
print('\n')

df3 = df2.drop(df2.index[0])
print(df3)
print('\n')

#df3.to_excel('i.xlsx')


# In[4]:


# df2를 '1학년.1' 기준 오름차순으로 정렬
a = df3.sort_values(by='1학년.1' ,ascending=False)
print(a[['1학년.1']])
print('\n')

a = a.loc[:,['시도교육청','학교명','1학년.1','지역' ]]
print(a)

a['1학년.1'] = a['1학년.1'].astype('float')


# In[5]:


# 시도교육청별로 그룹화
b = a.groupby(['시도교육청'])
for key, group in b:  
    print('***key:',key)
    print(group.head(10))
    print('\n')
    print(group.tail(10))


# In[6]:


# 각 그룹의 최고, 최저 10개학교의 교명, 학생 수, 지역 출력
for key, group in b:  
    print('***key:',key)
    print(group.head(10))
    print('\n')
    print(group.tail(10))


# In[7]:


# 그래프(평균) - 제목:시도별 1학년 평균 학생 수 (가로:시도교육청, 세로: 평균 학생 수)

ave = b.mean()
print(ave.index)
print('\n')
print(ave.values)
print('\n')
print(ave)


# In[25]:


plt.figure(figsize=(14, 5))

plt.plot(ave)
#plt.bar(ave.index, ave.values)


#폰트 추가
from matplotlib import font_manager, rc
font_path = "./malgun.ttf" #폰트 파일 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

plt.title('시도별 1학년 평균 학생 수', size = 17)
plt.xlabel('교육청', size=12)
plt.ylabel('학생수', size=12)

plt.xticks(rotation=75)

plt.ylim(20,120)

plt.tick_params(axis="x",labelsize=9)
plt.tick_params(axis="y",labelsize=9)

plt.show()


# In[ ]:


b.plot(kind='bar', figsize(20,10), width = 0.9)

plt.show()


# In[9]:


# <1-2>

# 1학년 데이터 전처리
df2 = df2.fillna(method = 'ffill')
print(df2.columns)
print('\n')

df3 = df2.drop(df2.index[0])
print(df3)
print('\n')

#df3.to_excel('i.xlsx')


# In[27]:


# df2를 수 '수업 교원 \n 1인당 학생수' 기준 오름차순으로 정렬
a = df3.sort_values(by='수업 교원 \n 1인당 학생수' ,ascending=True)
print(a[['수업 교원 \n 1인당 학생수']])
print('\n')

a = a.loc[:,['시도교육청','학교명','수업 교원 \n 1인당 학생수','지역' ]]
print(a)

a['수업 교원 \n 1인당 학생수'] = a['수업 교원 \n 1인당 학생수'].astype('float')


# In[28]:


# 시도교육청별로 그룹화
b = a.groupby(['시도교육청'])

# 각 그룹의 최고, 최저 10개학교의 교명, 학생 수, 지역, 출력
for key, group in b:  
    print('***key:',key)
    print(group.head(10))
    print('\n')
    print(group.tail(10))
    print('\n')


# In[32]:


# 그래프(평균) - 제목:시도교육청별 초등학교 교원당 학생수 평균 (가로:시도교육청, 세로: 교원당 학생 수 평균)

ave = b.mean()
print(ave.index)
print('\n')
print(ave.values)
print('\n')
print(ave)


# In[39]:


plt.figure(figsize=(14, 5))

plt.plot(ave)
#plt.bar(ave.index, ave.values)


#폰트 추가
from matplotlib import font_manager, rc
font_path = "./malgun.ttf" #폰트 파일 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

plt.title('시도교육청별 초등학교 교원당 학생수 평균', size = 17)
plt.xlabel('교육청', size=12)
plt.ylabel('학생수', size=12)

plt.xticks(rotation=75)

plt.ylim(10,20)

plt.tick_params(axis="x",labelsize=9)
plt.tick_params(axis="y",labelsize=9)


plt.show()


# In[ ]:




