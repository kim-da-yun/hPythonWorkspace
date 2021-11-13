#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np

df = pd.read_csv('auto-mpg.csv', header=None) # Header가 없는 파일
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']
# 문자열은 경계를 나눌 수 있는 자동 메소드 처리의 도움을 못 받아서 horsepower 열 자체를 실수값으로 변경을 하고 pandas에서 제공하는 함수의 도움을 받으려 함
df['horsepower'].replace('?', np.nan, inplace=True) # replace를 이용해서 ? 값을 np가 갖고있는 not a number로 바꾸는 작업
df.dropna(subset=['horsepower'], axis=0, inplace=True)# 변경된 내용에 대한 not a number(nan)가 들어가는 부분을 삭제,
# 특정 열만 국한하기 위해 subset 사용, 축을 행 방향으로 삭제.
df['horsepower']=df['horsepower'].astype('float') # 타입 변환


# In[8]:


a = np.histogram(df['horsepower'], bins=3)# 구하고 싶은 경계값에 대해서 3개로 나누겠다는 정보 제공,
# 경계를 나눌 데이터 열이 horsepower임, 전체 구간에 대해 슬롯 갯수 3으로 지정해서 메소드에게 전달
print(a) # 튜플로 두 개를 받음, 두번째는 배열에다가 숫자 4개를 받아옴, 
# 구역을 3개로 나누라 해서 마력이 가장 작은 46~107까지 107~168까지 168~230까지로 구간이 3개가 되는데 이 영역별로 해당 데이터가 몇개씩 들어가있냐의
# 구간별 갯수가 첫번째 자리로 옴 257개, 103개, 32개.
# 이 두 개의 값이 넘어오기 때문에


# In[9]:


count, bin_dividers = np.histogram(df['horsepower'], bins=3)
print(bin_dividers)


# In[10]:


# 숫자의 마력 부분을 46~107 부분을 저출력으로 107~168을 보통 출력으로 168~을 고출력으로 하겠다는 이름을 정의
# 범위는 자동으로 histogram이 같은 간격(60정도)으로 끊어서 3구간으로 나눔
bin_names = ['저출력','보통출력','고출력']
df['hp_bin'] = pd.cut(x=df['horsepower'], bins=bin_dividers, labels=bin_names, include_lowest=True) 
# cut 메소드는 어떤한 데이터를 갖고 나눌건지가 첫번째 자리에 들어감 / 두번째 자리에는 경계를 나누기 위한 숫자 / 
# 세번째는 labels 옵션으로 경계로 나눌 떄 각각의 경계 부분에 포함되는 데이터를 어떤 이름의 카테고리라고 부를까라는 이름이 담긴 리스트 /
# 최초의 가장 작은 경계값(46/0)을 해당 카테고리에 포함시킬거냐 했을 떄 해당 카테고리에 포함되게 하겠다 -> include_lowest=True
# 상한선은 include_highst=True, 하한선은 include_lowest=True


# In[11]:


print(df)


# In[12]:


# 해당 카테고리에 대한 값을 계산을 처리하기 위한 용도의 숫자로 변경하기 위한 방법 -> 더미변수 
# 더미변수: 계산을 할때 유용하게 쓸 수 있는 별도의 column들을 만들고 실제 카테고리 값을 0 또는 1로 표시해서 해당 3개 카테고리에 대한 특징이 있느냐 없느냐에 대한 것을 간단하게 표현하는 방법
# 저출력, 보통출력, 고출력에 대한 것을 별도의 열로 만들고 해당 열에 대해서 해당 자동차 모델 행이 저출력의 특성이 있냐.
# 만약에 보통 출력에 해당하는 모델이면 저출력의 특성이 없으니깐 0, 보통 출력이 있으니깐 1, 고출력의 특성이 없으니깐 0.
# 이후의 후속 작업을 위한 처리를 쉽게 하는 방법을 더미 변수 추가.
hp_dummies = pd.get_dummies(df['hp_bin'])
print(hp_dummies)


# In[13]:


# 정규화: -1 ~ 1 사이의 2 크기 구간내로 랩핑이 될 수 있는 과정
print(df.horsepower)


# In[14]:


print(df.horsepower.describe()) # 상대적인 형태들을 알 수 있음


# In[ ]:





# In[15]:


print(df.horsepower)


# In[16]:


print(df.horsepower.describe())


# In[17]:


min_max = df['horsepower'].max()-df['horsepower'].min()
min_x = df['horsepower']-df['horsepower'].min() # min_x는 horsepower 갯수만큼 생김
print(min_x) # 위 df['horsepower'] = df['horsepower']/df['horsepower'].max() 삭제


# In[18]:


df['horsepower'] = min_x/min_max
print(df['horsepower'])


# In[19]:


print(df.horsepower.describe())


# In[20]:


# 기존의 문자열 데이터를 시리얼 데이터 중에 타임스탬프로 변경하는 방법
df = pd.read_csv('stock-data.csv')


# In[21]:


print(df)


# In[22]:


df['new_date'] = pd.to_datetime(df['Date']) # 갖고있던 date 열을 변경하기 위해 판다스가 가지고 있는 메소드 to_datetime


# In[23]:


print(df)


# In[24]:


df.info()


# In[25]:


df.set_index('new_date', inplace = True) # 원하는 특정 열을 인덱스로 지정할 수 있음


# In[26]:


print(df)


# In[27]:


df.drop('Date', axis = 1, inplace = True) # 기존 Date를 삭제


# In[28]:


print(df)


# In[29]:


print(df.info()) # 해당 인덱스가 Datetime으로 바뀜


# In[30]:


dates = ['2020-01-01', '2020-03-01', '2020-06-01']
ts = pd.to_datetime(dates)
print(ts)


# In[31]:


# time 스탬프를 period로변경
p_day = ts.to_period(freq = 'D') # D= day, M = month, W = week, a = year
print(p_day)


# In[32]:


p_day = ts.to_period(freq = 'M') # D= day, M = month, W = week, a = year
print(p_day)


# In[33]:


p_day = ts.to_period(freq = 'A') # D= day, M = month, W = week, a = annual(1년)
print(p_day)


# In[34]:


# data를 자동으로 만들어서 배열 형태로 채우는 방법
a = pd.date_range(start = '2020-01-01', end = None, periods = 6, freq = 'MS', tz = 'Asia/Seoul') 
# 끝나는걸 지정하지 않고 간격 갯수 생성할 부분만 알려줌. period = timestemp의 갯수를 몇개를 만들거냐는 지정. 
# freq = 간격(MS : 월의 시작일), tz= 시간대


# In[35]:


a = pd.date_range(start = '2020-01-01', end = None, periods = 6, freq = 'M', tz = 'Asia/Seoul')  # freq = M은 끝나는 날짜를 기준으로(1달간격)
print(a)


# In[36]:


a = pd.date_range(start = '2020-01-01', end = None, periods = 6, freq = '3M', tz = 'Asia/Seoul') # 3M은 3달간격
print(a)


# In[37]:


a = pd.period_range(start = '2020-01-01', end = None, periods = 6, freq = 'M') # 타임스탬프가 아니라 timeson(tz)를 쓰지 않음
print(a)


# In[38]:


a = pd.period_range(start = '2020-01-01', end = None, periods = 6, freq = 'H') # H = 시간
print(a)


# In[39]:


a = pd.period_range(start = '2020-01-01', end = None, periods = 6, freq = '2H') # H = 3시간 간격
print(a)


# In[40]:


df = pd.read_csv('stock-data.csv')


# In[41]:


df['new_date'] = pd.to_datetime(df['Date'])


# In[42]:


print(df)


# In[43]:


print(df['new_date'].dt) # dt 속성으로 DatetimeProject를 의미함


# In[44]:


df['year'] = df['new_date'].dt.year


# In[45]:


print(df)


# In[46]:


df['year'] = df['new_date'].dt.year
df['month'] = df['new_date'].dt.month
df['day'] = df['new_date'].dt.day


# In[47]:


print(df)


# In[48]:


df['date_year'] = df['new_date'].dt.to_period(freq = 'A') # year는 연도를 뽑아가지고 단순한 형태의 문자열로 저장했으면 
# date_year는 period 형태의 변화를 통해서 갖고온 period 타입의 데이터가 됨


# In[49]:


print(df)


# In[50]:


df['date_year'] = df['new_date'].dt.to_period(freq = 'A')
df['date_m'] = df['new_date'].dt.to_period(freq = 'M')


# In[51]:


print(df)


# In[52]:


# period 타입의 월 단위의 값을 행의 인덱스로 사용
df.set_index('date_m', inplace = True)
print(df)


# In[53]:


# 인덱스로 new_date 전체를 사용
df.set_index('new_date', inplace = True)
print(df)
# 장점: index는 해당 행을 가져오는 용도로 사용해서 정확히 일치하는 형태로만 해당 값을 갖다가 특정한 범위나 특정한 index가 일치하는 형태로
# 사용할 수 있었는 datetime 형태가 사용이 되면 시간대를 활용해서 indexing 할 수 있음


# In[55]:


# df의 특정한 행을 가져오는데 날짜 인덱스를 사용할 수 있음
a = df['2018']
print(a) # df내에서 인덱스의 2018와 일치하는 게 아닌 인덱스 자체의 성격이 datetime이니 연도에 해당되는 2018 부분과 일치되는 부분을 찾을 수 있음


# In[56]:


a = df['2018-07']
print(a) # 행에 대한 부분을 갖고올 때 df의 loc을 쓰는데 쓰지 않음 


# In[57]:


a = df.loc['2018-07']
print(a)


# In[59]:


# 특정 일 출력
a = df['2018-07-02']
print(a)


# In[60]:


# 특정 일~ 특정 일(index slicing 사용)
a = df['2018-06-11':'2018-06-18']
print(a) # 결과가 안 나옴


# In[62]:


a = df['2018-06-18':'2018-06-11']
print(a)


# In[63]:


# 날짜들 사이의 계산, 간격들을 자동으로 계산시킬 수 있음
today = pd.to_datetime('2021-11-03')


# In[65]:


df['time_delta'] = today - df.index
print(df)


# In[66]:


# time_delta의 열을 새로운 인덱스로 만듦
df.set_index('time_delta', inplace = True)


# In[67]:


print(df)


# In[69]:


a = df['1232 days':'1241 days']
print(a)


# In[ ]:




