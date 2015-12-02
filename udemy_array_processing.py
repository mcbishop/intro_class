
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

import matplotlib.pyplot as plt


# In[3]:

get_ipython().magic('matplotlib inline')


# In[4]:

points = np.arange(-5,5,0.01) #start, stop, step value


# In[5]:

dx,dy = np.meshgrid(points,points) #returns coordinates from vectors given


# In[6]:

dx


# In[7]:

#dx is a matrix where all rows go from -5 to 5 in .-1 steps


# In[8]:

dy


# In[9]:

#dy does the same but goes along columns instead


# In[10]:

z = (np.sin(dx) + np.sin(dy))


# In[11]:

z


# In[12]:

#in order to plot, call plt and do image show to plot along a matrix


# In[13]:

plt.imshow(z)


# In[14]:

#to plot with color bar


# In[15]:

plt.imshow(z)
plt.colorbar()

plt.title('Plot for sin(x)+sin(y)')


# In[16]:

#learning how to use numpy where - create two arrays


# In[17]:

A = np.array([1,2,3,4])
B = np.array([100,200,300,400])


# In[18]:

condition = np.array([True,True,False,False])


# In[19]:

#can use boolean array for list comprehension. choose the A value if the condition is true; otherwise choose B value.


# In[20]:

answer = [(A_val if cond else B_val) for A_val,B_val,cond in zip(A,B,condition)]


# In[21]:

# answer will say - in this array, show me the A value if the condition is met. otherwise show B value


# In[22]:

# choose A value if condition is True, otherwise choose B value. so you'll choose A, A, B, B - 1,2,300,400 
# uses list comprehension to use boolean logic in this array


# In[23]:

answer


# In[24]:

answer2 = np.where(condition,A,B) #short form: where my condition is met, choose A; otherwise choose B


# In[25]:

answer2


# In[26]:

from numpy.random import randn


# In[27]:

arr = randn(5,5)


# In[28]:

arr


# In[31]:

np.where(arr<0,0,arr)


# In[32]:

# for this where statement, if the value in the array is less than 0, replace with 0; otherwise keep the original value.


# In[33]:

#where: (if, then, else)


# In[34]:

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[35]:

arr


# In[36]:

arr.sum()


# In[37]:

# summed up all values in the array. can also sum up columns - specific axis


# In[38]:

arr.sum(0)


# In[39]:

#sums up all values in each column, respectively


# In[40]:

arr.mean()


# In[41]:

#average is 5


# In[42]:

arr.std()


# In[43]:

#standard deviation


# In[44]:

arr.var()


# In[45]:

bool_arr = np.array([True,False,True])


# In[46]:

bool_arr.any() #returns a value if anything was true


# In[47]:

bool_arr.all() #returns true only if all values were true - returns false


# In[48]:

#sort
arr = randn(5)


# In[49]:

arr


# In[50]:

arr.sort()


# In[51]:

arr


# In[52]:

#sorted from least to greatest


# In[53]:

countries = np.array(['France','Germany','USA','Russia','Mexico','Germany'])


# In[54]:

#to find out which values are unique
np.unique(countries)


# In[55]:

np.in1d(['France','USA','Sweden'],countries) #if France, Sweden are in countries array, will output boolean true or false


# In[ ]:



