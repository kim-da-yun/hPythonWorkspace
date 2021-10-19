#!/usr/bin/env python
# coding: utf-8

# In[79]:


import pandas as pd

x=['','','']

a1=pd.read_excel('전자과.xlsx', sheet_name = '1차시험',index_col='학번')

a2=pd.read_excel('전자과.xlsx', sheet_name = '2차시험',index_col='학번')

a3=pd.read_excel('전자과.xlsx', sheet_name = '3차시험',index_col='학번')

b1=pd.read_excel('전기과.xlsx', sheet_name = '1차시험',index_col='학번')

b2=pd.read_excel('전기과.xlsx', sheet_name = '2차시험',index_col='학번')

b3=pd.read_excel('전기과.xlsx', sheet_name = '3차시험',index_col='학번')

r1=a1+a2*5

r1=r1.add(a3,fill_value=60)

r1=r1/3

r1['평균']=(r1['국어']+r1['영어']+r1['수학']+r1['사회']+r1['과학'])/5

r1.loc['평균']=r1.mean();

r1.loc['최대']=r1.max();

r1.loc['최소']=r1.min();

 

 

w = pd.ExcelWriter('exam.xlsx')

r1.to_excel(w, sheet_name='전자과')

# r2.to_excel(w, sheet_name='전기과')

w.save()


# In[ ]:




