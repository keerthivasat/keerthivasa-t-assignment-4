#!/usr/bin/env python
# coding: utf-8

# In[2]:


r = lambda a : a + 25
print(r(10))
r = lambda x, y : x * y
print(r(12, 4))


# In[4]:


num = (1, 2, 3, 4, 5, 6, 7) 
print("given list: ", num)
result = map(lambda x: x + x + x, num) 
print("\n")
print(list(result))


# In[5]:


def square_num(n):
  return n * n
nums = [4, 5, 2, 9]
print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements of the said list using map():")
print(list(result))


# In[ ]:




