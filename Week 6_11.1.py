#!/usr/bin/env python
# coding: utf-8

# In[6]:


fin = open("/Users/jg198/Desktop/words.txt")
line = fin.readline()
word = line.strip()
txtdictionary = dict()


# In[7]:


txtdictionary


# In[6]:


fin = open("/Users/jg198/Desktop/words.txt")

def words_dictionary():
    txtdictionary = dict()
    count = 0
    for line in fin:
        word = line.strip()
        txtdictionary[word] = count
        count +=1
    return txtdictionary
txtdictionary = words_dictionary()
txtdictionary


# In[ ]:




