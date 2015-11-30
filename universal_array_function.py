
# coding: utf-8

# In[1]:

import numpy


# In[2]:

import numpy as np


# In[3]:

arr = np.arange(11)


# In[4]:

arr


# In[5]:

#universal functions you can apply to every value in an array


# In[6]:

np.sqrt(arr)


# In[7]:

#takes square root of every value in the array


# In[8]:

np.exp(arr) #takes E to the power of the number in the array


# In[9]:

#e (how many further decimal points it goes) 


# In[10]:

A = np.random.randn(10)


# In[11]:

A


# In[12]:

#normal distribution of some random numbers


# In[13]:

B = np.random.randn(10)


# In[14]:

B


# In[15]:

#Binary functions that use two arrays


# In[16]:

np.add(A,B) #will add every value of A to every value of B


# In[18]:

#can find max or min between two arrays
np.maximum(A,B)


# In[19]:

#compares values at each index


# In[20]:

#and sets them as the value for the array you just called


# In[21]:

#can also check for mins


# In[22]:

#directs to ufuncts documentation in numpy -http://docs.scipy.org/doc/numpy/reference/ufuncs.html


# In[ ]:



