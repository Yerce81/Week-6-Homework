#!/usr/bin/env python
# coding: utf-8

# In[1]:


def histrogram(s):
    d= dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


# In[3]:


x = histrogram('Supercalifragilisticexpialidocious')
x


# In[5]:


def most_frequent(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


# In[7]:


inverse = invert_dict(x)
inverse


# In[ ]:




