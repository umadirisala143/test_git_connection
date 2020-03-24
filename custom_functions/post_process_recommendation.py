#!/usr/bin/env python
# coding: utf-8

# In[5]:


from datetime import datetime


# In[15]:


def post_process_recommendation(config,**rec_object):
    recommendation = rec_object["recommendation"][0]
    prediction_score = recommendation["values"][0]["score"][0]
    model_name = recommendation["model_name"]
    if prediction_score > 0.5:
        result = "Patient will visit"
    else:
        result = "Patient will not visit"
    
    entities = {
              "doc_id": recommendation["doc_id"],
              "root_id": recommendation["root_id"],
              "entities": [
                {
                  "entity_type": "domain_object",
                  "entity_name": "patient",
                  "children": [
                    {
                      "entity_name": "revisit_recommendation",
                      "entity_type": "entity",
                      "attributes": [
                        {
                          "name": "model_name",
                          "value": model_name,
                          "confidence": 1,
                          "element_id": "11111111"
                        },
                        {
                          "name": "recommendation",
                          "value": result,
                          "confidence": prediction_score,
                          "element_id": "11111111"
                        }
                      ]
                    }
                  ]
                }
              ]
            }
    return entities

