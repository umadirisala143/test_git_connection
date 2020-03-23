#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime


# In[2]:


def convertpayload_getobjects(config,**doc_obj):
    json_data = {
          "doc_id": doc_obj["domain"][0]["doc_id"], "root_id": doc_obj["domain"][0]["root_id"]
    }
    return json_data

