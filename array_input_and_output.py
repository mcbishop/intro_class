
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

arr = np.arange(5)


# In[3]:

arr


# In[4]:

np.save('myarray',arr)


# In[5]:

arr = np.arange(10)


# In[6]:

arr


# In[8]:

np.load('myarray.npy')


# In[9]:

#you can also save multiple arrays


# In[10]:

arr1 = np.load('myarray.npy')


# In[11]:

arr1


# In[12]:

arr2 = arr


# In[17]:

arr1


# In[16]:

arr2


# In[22]:

np.savez('ziparray.npz',x=arr1,y=arr2)


# In[23]:

archive_array = np.load('ziparray.npz')


# In[24]:

archive_array('x')


# In[21]:

np.savez


# In[25]:

#you can also save and load text files, in case you don't want to save it as an array.
# making a matrix using array


# In[26]:

arr = np.array([[1,2,3],[4,5,6]])


# In[27]:

arr


# In[28]:

np.savetxt('mytextarray.txt',arr,delimiter=',')


# In[30]:

arr = np.loadtxt('mytextarray.txt',delimiter=',')
arr


# In[ ]:

# we learned to save array as npz or text files. in the future, excel files. 
