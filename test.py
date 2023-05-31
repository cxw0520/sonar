#!/usr/bin/env python
# coding: utf-8

# In[1]:


from utility import load_dictionary






# In[2]:


def fully_segment(text, dic):
    word_list = []
    for i in range(len(text)):                  # i 從 0 到text的最後一個字的下標遍歷
        for j in range(i + 1, len(text) + 1):   # j 遍歷[i + 1, len(text)]區間
            word = text[i:j]                    # 取出連續區間[i, j]對應的字串
            if word in dic:                     # 如果在詞典中，則認為是一個詞
                word_list.append(word)
    return word_list
