
# coding: utf-8

# In[1]:

import numpy as np


# In[3]:

arr = np.arange(0,11)


# In[4]:

arr


# In[5]:

arr[8]


# In[6]:

arr[1:5]


# In[7]:

arr(0:5)


# In[8]:

arr[0:5]


# In[9]:

arr[0:5] = 100


# In[10]:

arr


# In[14]:

arr = np.arange(0,11)


# In[15]:

slice_of_arr = arr[0:6]


# In[16]:

slice_of_arr


# In[17]:

slice_of_arr[:]=99


# In[18]:

slice_of_arr


# In[19]:

arr


# In[20]:

#in numpy this data isn't copied. It's just a view of the original array. You only have one copy of the array, and if you grab slices, it will affect original array.


# In[22]:

arr_copy = arr.copy()


# In[25]:

arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))


# In[27]:

arr_2d[1]


# arr_2d

# In[28]:

arr_2d


# In[29]:

arr_2d[1][0]


# In[30]:

arr_2d


# In[31]:

arr_2d[:2,1:]


# In[32]:

arr_2d[2]


# In[33]:

arr2d = np.zeros((10,10))


# In[34]:

arr2d


# In[35]:

#resetting array to a 10 x 10 of zeros


# In[36]:

arr_length = arr2d.shape[1]


# In[37]:

arr_length


# In[52]:

for i in range(arr_length):
    arr2d[i] = i


# In[53]:

#for every i in range arr_length (which is 10), set that element equal to i.


# In[54]:

arr2d


# In[57]:

arr2d([2,4,6,8])


# In[ ]:

# fancy indexing: you can call indexes out of order.

