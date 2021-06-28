# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:46:08 2021

@author: HP
"""


import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "yytM9ZbPkkDZ_PWyKzXdHuJvFctkkZUdgcNhP6Caz_U7"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["FL_NUM","MONTH","DAY_OF_MONTH","DAY_OF_WEEK","CRS_ARR_TIME","DEP_DEL15","ORIGIN_ATL","ORIGIN_DTW","ORIGIN_JFK","ORIGIN_MSP","ORIGIN_SEA","DEST_ATL","DEST_DTW","DEST_JFK","DEST_MSP","DEST_SEA"]], "values": [[1399,1,1,5,21,0,1,0,0,0,0,0,0,0,0,1]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/4dd381d7-6e94-47f4-b00c-f01a781d53cb/predictions?version=2021-06-28', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions = response_scoring.json()

print(predictions['predictions'][0]['values'][0][0])