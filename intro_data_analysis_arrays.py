
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')

import pandas as pd
import numpy as np
import matplotlib

from matplotlib import pyplot as plt
import seaborn as sns

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
plt.figure(); df.plot(); plt.legend(loc='best')


# In[3]:

print "this is not neat"


# In[4]:

import numpy as np


# In[5]:

var = np.arange(1, 25)
print var


# In[6]:

print "This is a code cell"


# In[7]:

print "Run cell with shift-enter"


# This is a markdown cell for comments - regular text, not code. 

# In[9]:

# Let's make this a header.


# In[10]:

1+2


# In[11]:

my_list1 = [1,2,3,4]


# In[12]:

my_array1 = np.array(my_list1)


# In[13]:

my_array1


# In[14]:

my_list2 = (11,22,33,44)


# In[15]:

my_lists = (my_list1,my_list2)


# In[16]:

my_lists


# In[17]:

my_list2= [11,22,33,44
          ]


# In[18]:

my_lists


# In[19]:

my_array2 = np.array(my_lists)


# In[20]:

my_array2


# In[21]:

my_array2.shape


# In[22]:

my_array2.dtype


# In[23]:

np.zeros(5)


# In[24]:

my_zeros_array = np.zeros(5)


# In[25]:

my_zeros_array.dtype


# In[26]:

np.ones([5,5])


# In[27]:

np.empty(5)


# In[28]:

np.eye(5)


# In[29]:

# identity matrix is a diagonal of a one with everything else filled in with zeros


# In[30]:

np.arange(5,50,2)


# In[ ]:

7

