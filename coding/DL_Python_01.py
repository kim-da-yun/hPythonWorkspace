#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.8
    temp = x1*w1 + x2*w2
    if temp <= theta:
        return 0
    elif temp > theta:
        return 1


# In[3]:


AND(0, 0)


# In[5]:


AND(1, 0)


# In[6]:


AND(0, 1)


# In[7]:


AND(1, 1)


# In[8]:


def NAND(x1, x2):
    w1, w2, theta = -0.5, -0.5, -0.8
    temp = x1*w1 + x2*w2
    if temp <= theta:
        return 0
    elif temp > theta:
        return 1


# In[9]:


NAND(0, 0)


# In[10]:


NAND(0, 1)


# In[11]:


NAND(1, 0)


# In[13]:


NAND(1, 1)


# In[14]:


def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.3
    temp = x1*w1 + x2*w2
    if temp <= theta:
        return 0
    elif temp > theta:
        return 1


# In[15]:


OR(0, 0)


# In[16]:


OR(0, 1)


# In[17]:


OR(1, 0)


# In[18]:


OR(1, 1)


# In[19]:


def AND(x1, x2):
    w1, w2, b = 0.5, 0.5, -0.8
    theta = 0
    temp = x1*w1 + x2*w2 + b
    if temp <= theta:
        return 0
    elif temp > theta:
        return 1


# In[20]:


AND( 0,0)


# In[21]:


AND(0,1)


# In[22]:


AND(1,0)


# In[23]:


AND(1,1)


# In[24]:


# 다층 퍼셉트론 XOR
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


# In[25]:


XOR(0,0)


# In[26]:


XOR(0,1)


# In[27]:


XOR(1,0)


# In[28]:


XOR(1,1)


# In[ ]:




