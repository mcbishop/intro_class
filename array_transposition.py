
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

arr = np.arange(50).reshape((10,5))


# In[3]:

arr


# In[4]:

#reshaped into a 10 x 5 matrix


# In[5]:

aarr.T


# In[6]:

arr.T


# In[7]:

#transposed to 5 x 10 matrix


# In[8]:

#so first row is transposed to first column


# In[9]:

np.dot(arr.T,arr)


# In[10]:

#.dot product multiplies the two matrixes by each other. (10 x 5) * (5 x 10). WE can only multiply if number of columns in first = number of rows in 2nd.                                                                                                          


# In[11]:

#so it's row multiplied by columns... until it runs out of columns? getting row from first matrix and column from sexond.  


# In[13]:

arr3d = np.arange(50).reshape((5,5,2))


# In[14]:

arr3d


# In[17]:

arr3d.transpose((1,0,2))


# In[18]:

#transposed first line rows and columns so that it's first row of every subsequent slice


# In[19]:

# take first set at index of zero and put all those pairs into 3d boxes: http://stackoverflow.com/questions/32034237/how-does-numpy-ndarray-transpose-permute-the-axis-of-n-d-array


# In[20]:

#to get specific to swap axis in an array you can swap it in particular


# In[21]:

arr = np.array([[1,2,3]])



# In[22]:

arr.swapaxes(0,1)


# In[23]:

arr


# In[ ]:



