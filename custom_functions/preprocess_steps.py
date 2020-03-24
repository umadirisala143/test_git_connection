#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
import pandas as pd
from xpms_file_storage.file_handler import XpmsResource, LocalResource


# In[2]:


all_columns = ['ClaimsTruncated', 'trainset', 'age_05', 'age_15', 'age_25', 'age_35', 'age_45', 'age_55', 'age_65', 'age_75', 'age_85', 'age_MISS', 'sexMALE', 'sexFEMALE', 'sexMISS', 'no_Claims', 'no_Providers', 'no_Vendors', 'no_PCPs', 'no_PlaceSvcs', 'no_Specialities', 'no_PrimaryConditionGroups', 'no_ProcedureGroups', 'PayDelay_max', 'PayDelay_min', 'PayDelay_ave', 'PayDelay_stdev', 'LOS_max', 'LOS_min', 'LOS_ave', 'LOS_stdev', 'LOS_TOT_UNKNOWN', 'LOS_TOT_SUPRESSED', 'LOS_TOT_KNOWN', 'dsfs_max', 'dsfs_min', 'dsfs_range', 'dsfs_ave', 'dsfs_stdev', 'CharlsonIndexI_max', 'CharlsonIndexI_min', 'CharlsonIndexI_ave', 'CharlsonIndexI_range', 'CharlsonIndexI_stdev', 'pcg1', 'pcg2', 'pcg3', 'pcg4', 'pcg5', 'pcg6', 'pcg7', 'pcg8', 'pcg9', 'pcg10', 'pcg11', 'pcg12', 'pcg13', 'pcg14', 'pcg15', 'pcg16', 'pcg17', 'pcg18', 'pcg19', 'pcg20', 'pcg21', 'pcg22', 'pcg23', 'pcg24', 'pcg25', 'pcg26', 'pcg27', 'pcg28', 'pcg29', 'pcg30', 'pcg31', 'pcg32', 'pcg33', 'pcg34', 'pcg35', 'pcg36', 'pcg37', 'pcg38', 'pcg39', 'pcg40', 'pcg41', 'pcg42', 'pcg43', 'pcg44', 'pcg45', 'pcg46', 'sp1', 'sp2', 'sp3', 'sp4', 'sp5', 'sp6', 'sp7', 'sp8', 'sp9', 'sp10', 'sp11', 'sp12', 'sp13', 'pg1', 'pg2', 'pg3', 'pg4', 'pg5', 'pg6', 'pg7', 'pg8', 'pg9', 'pg10', 'pg11', 'pg12', 'pg13', 'pg14', 'pg15', 'pg16', 'pg17', 'pg18', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7', 'ps8', 'ps9', 'drugCount_max', 'drugCount_min', 'drugCount_ave', 'drugcount_months', 'labCount_max', 'labCount_min', 'labCount_ave', 'labcount_months', 'labNull', 'drugNull']
reference_values = {'no_Claims': 12.0, 'no_Providers': 7.0, 'no_Vendors': 3.0, 'no_PCPs': 1.0, 'no_PlaceSvcs': 3.0, 'no_Specialities': 5.0, 'no_PrimaryConditionGroups': 3.0, 'no_ProcedureGroups': 5.0, 'PayDelay_max': 81.0, 'PayDelay_min': 30.0, 'PayDelay_ave': 50.0, 'PayDelay_stdev': 20.052015692526602, 'LOS_max': 0.0, 'LOS_min': 0.0, 'LOS_ave': 0.0, 'LOS_stdev': -1.0, 'LOS_TOT_UNKNOWN': 12.0, 'LOS_TOT_SUPRESSED': 0.0, 'LOS_TOT_KNOWN': 0.0, 'dsfs_max': 12.0, 'dsfs_min': 1.0, 'dsfs_range': 11.0, 'dsfs_ave': 6.0, 'dsfs_stdev': 4.4338573397315004, 'CharlsonIndexI_max': 2.0, 'CharlsonIndexI_min': 2.0, 'CharlsonIndexI_ave': 2.0, 'CharlsonIndexI_range': 0.0, 'CharlsonIndexI_stdev': 0.0, 'pcg1': 4.0, 'pcg2': 0.0, 'pcg3': 0.0, 'pcg4': 0.0, 'pcg5': 0.0, 'pcg6': 0.0, 'pcg7': 3.0, 'pcg8': 0.0, 'pcg9': 0.0, 'pcg10': 0.0, 'pcg11': 0.0, 'pcg12': 0.0, 'pcg13': 0.0, 'pcg14': 0.0, 'pcg15': 0.0, 'pcg16': 0.0, 'pcg17': 5.0, 'pcg18': 0.0, 'pcg19': 0.0, 'pcg20': 0.0, 'pcg21': 0.0, 'pcg22': 0.0, 'pcg23': 0.0, 'pcg24': 0.0, 'pcg25': 0.0, 'pcg26': 0.0, 'pcg27': 0.0, 'pcg28': 0.0, 'pcg29': 0.0, 'pcg30': 0.0, 'pcg31': 0.0, 'pcg32': 0.0, 'pcg33': 0.0, 'pcg34': 0.0, 'pcg35': 0.0, 'pcg36': 0.0, 'pcg37': 0.0, 'pcg38': 0.0, 'pcg39': 0.0, 'pcg40': 0.0, 'pcg41': 0.0, 'pcg42': 0.0, 'pcg43': 0.0, 'pcg44': 0.0, 'pcg45': 0.0, 'pcg46': 0.0, 'sp1': 4.0, 'sp2': 2.0, 'sp3': 1.0, 'sp4': 0.0, 'sp5': 1.0, 'sp6': 4.0, 'sp7': 0.0, 'sp8': 0.0, 'sp9': 0.0, 'sp10': 0.0, 'sp11': 0.0, 'sp12': 0.0, 'sp13': 0.0, 'pg1': 6.0, 'pg2': 1.0, 'pg3': 3.0, 'pg4': 1.0, 'pg5': 1.0, 'pg6': 0.0, 'pg7': 0.0, 'pg8': 0.0, 'pg9': 0.0, 'pg10': 0.0, 'pg11': 0.0, 'pg12': 0.0, 'pg13': 0.0, 'pg14': 0.0, 'pg15': 0.0, 'pg16': 0.0, 'pg17': 0.0, 'pg18': 0.0, 'ps1': 6.0, 'ps2': 2.0, 'ps3': 4.0, 'ps4': 0.0, 'ps5': 0.0, 'ps6': 0.0, 'ps7': 0.0, 'ps8': 0.0, 'ps9': 0.0, 'drugCount_max': 0.0, 'drugCount_min': 0.0, 'drugCount_ave': 0.0, 'drugcount_months': 0.0, 'labCount_max': 10.0, 'labCount_min': 10.0, 'labCount_ave': 10.0, 'labcount_months': 1.0, 'labNull': 0.0, 'drugNull': 1.0}


# In[15]:


def preprocess_steps(config,**doc_object):
    domain = doc_object["domain"][0]
    entities = domain["children"][0]["children"]
    attr_dict = {}
    for entity in entities:
        attributes = entity["children"]
        for attr in attributes:
            if attr['name'] in attr_dict.keys():
                if len(attr['value']) > 20:
                    pass
                else:
                    attr_dict[attr['name']] = attr['value']
            else:
                attr_dict.update({attr["name"]: attr['value']})

    input_dict = {}
    for column in all_columns:
        if column in reference_values.keys():
            input_dict.update({column: reference_values[column]})
        else:
            input_dict.update({column: 0})

    if "gender" in attr_dict.keys():
        if attr_dict["gender"].lower() == "male":
            input_dict["sexMALE"] = 1
        else:
            input_dict["sexFEMALE"] = 1
    else:
        input_dict["sexMISS"] = 1

    if "age" in attr_dict.keys():
        try:
            age = int(attr_dict["age"])
        except:
            age = 30
            
        if age <= 5:
            input_dict["age_05"] = 1
        elif age <= 15:
            input_dict["age_15"] = 1
        elif age <= 25:
            input_dict["age_25"] = 1
        elif age <= 35:
            input_dict["age_35"] = 1
        elif age <= 45:
            input_dict["age_45"] = 1
        elif age <= 55:
            input_dict["age_55"] = 1
        elif age <= 65:
            input_dict["age_65"] = 1
        elif age <= 75:
            input_dict["age_75"] = 1
        elif age <= 85:
            input_dict["age_85"] = 1
    else:
        input_dict["age_MISS"] = 1
    input_df = pd.DataFrame([input_dict])
    local_path = "/tmp/preprocessed.csv"
    input_df.to_csv(local_path, index=False)
    source_path = domain["solution_id"] + "/" + domain["doc_id"] + "/model/input/test.csv"
    source_res = XpmsResource.get(key=source_path)
    local_res = LocalResource(fullpath=local_path)
    local_res.copy(source_res)
    # input_dict = input_df.to_dict(orient='records')[0]
    model_json = {"dataset": {"data_format": "csv", "value": source_res.urn},
                  "root_id": domain["root_id"], "doc_id": domain["doc_id"]}
    return model_json

