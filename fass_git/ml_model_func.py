#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pickle
import pandas as pd
import json
import os
from xpms_file_storage.file_handler import XpmsResourceFactory, LocalResource
import inspect
import traceback
from xpms_helper.model.data_schema import DatasetFormat, DatasetConvertor
from xpms_helper.model import model_utils
from sklearn.metrics.scorer import SCORERS


# In[20]:


def calculate_metrics(scorers, y_labels, y_preds):
   model_scores = dict()
   if isinstance(scorers,str):
       scorers = [scorers]
   for scorer_type in scorers:
       try:
            score = SCORERS[scorer_type]._sign
            score_args = inspect.getfullargspec(SCORERS[scorer_type]._score_func).args
            if "average" in score_args:
               score *= SCORERS[scorer_type]._score_func(y_labels, y_preds, average="weighted")
            else:
                score *= SCORERS[scorer_type]._score_func(y_labels, y_preds)
            model_scores[scorer_type] = score
       except ValueError as e:
            model_scores[scorer_type] = traceback.format_exc(e)
   return model_scores


# In[15]:


def train(datasets,config):
    from sklearn import svm
    dataset = DatasetConvertor.convert(datasets,DatasetFormat.DATA_FRAME , None)
    clf = svm.SVC(probability=True)
    train_df = dataset["value"]
    target_column = "class"
    X = train_df.loc[:, train_df.columns != target_column]
    Y = train_df[target_column]
    model_obj = clf.fit(X, Y)
    train_info = {"name" : "SVC"}
    predictions = model_obj.predict_proba(X)
    result_df = pd.DataFrame(data=predictions, columns=model_obj.classes_)
    model_utils.save("model1.pkl",model_obj,config)
    result_dataset = {"value": result_df, "data_format": "data_frame"}
    return train_info, result_dataset


# In[30]:


def run(datasets,config):
    dataset = DatasetConvertor.convert(datasets, DatasetFormat.DATA_FRAME, None)
    run_df = dataset["value"]
    target_column = "class"
    X = run_df.loc[:, run_df.columns != target_column]
    file_name = "model1.pkl"
    model_obj = model_utils.load(file_name=file_name,config=config)
    predictions = model_obj.predict_proba(X)
    result_df = pd.DataFrame(data=predictions,columns=model_obj.classes_)
    result_dataset = {"value": result_df, "data_format": "data_frame"}
    return result_dataset


# In[40]:


def evaluate(datasets,config):
    dataset = DatasetConvertor.convert(datasets, DatasetFormat.DATA_FRAME, None)
    if "scorers" in config:
        scorers = config["scorers"]
    else:
        scorers = ["accuracy"]
    eval_df = dataset["value"]
    target_colum = "class"
    y = eval_df[target_colum]
    model_output = run(datasets,config)
    y_pred = model_output["value"].idxmax(axis=1).values
    score = calculate_metrics(scorers, y, y_pred)
    return score, model_output


# In[50]:


def test_template():
    config={}
    config["storage"] = "local"
    config["src_dir"] = os.getcwd()
    dataset_obj = json.load(open(os.path.join(os.getcwd(),"datasets_obj/dataset_obj.json")))
    dataset_format = dataset_obj["data_format"]
    if dataset_format != "list":
       dataset_obj["value"] = LocalResource(key= os.path.join(os.getcwd(),"datasets")).urn
    train(dataset_obj,config)
    run(dataset_obj,config)
    evaluate(dataset_obj,config)

