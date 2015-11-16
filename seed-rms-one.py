import requests
import pprint
import json

pp = pprint.PrettyPrinter(indent = 2)

def getToken():
	headers = {'Authorization':'Basic mTpzZWNyZXQ='}
	payload = {'username': 'rmsUser', 'password': 'P@ssword1', 'grant_type':'password', 'tenant': 'rms'}
	response = requests.post('http://localhost:8080/tokens', data = payload, headers = headers)
	print(response)
	if response.status_code == 201:
		return response.json()["access_token"]

def getPortfolios(token):
	headers = {'Authorization' : 'bearer ' + token, 'ContentType' : 'application/json'}
	response = requests.get('http://localhost:8089/v1/databaseServers/1/databases/GBFL34Loc_SmokeTestR4_EDM_v1/edm?fields=portfolios', headers = headers)
	if response.status_code == 200:
		pp.pprint(response.json())

def postEDMUpload(token, database, portfolios, databaseServerId):
	headers = {'Authorization' : 'bearer ' + token, 'ContentType' : 'application/json'}
	payload = {
		"databaseId": databaseServerId,
  		"databaseName": database,
		"portfolioFilter": portfolios,
		"performImport": "true",
		"importSettings": {
			"submissionType": "",
		    "cedant": "",
		    "extractValidOnly": "",
		    "currency": "",
		    "structureName": "",
		    "submissionId": "",
		    "submissionYear": "",
		    "asOfDate": "",
		    "submittedDate": "",
		    "externalId": "123",
		    "comment": "",
		    "region": "",
		    "peril": "",
		    "scenario": "",
		    "status": "",
		    "lineOfBusiness": "COM",
		    "broker": "",
		    "underwriter": "",
		    "underwriterGroup": "",
		    "branch": "",
		    "legalEntity": "",
		    "costCenter": "",
		    "businessUnit": "",
		    "hub": "",
		    "office": "",
		    "accountingOrganization": "",
		    "jurisdiction": ""
		  }
	}
	response = requests.post('http://localhost:8089/v1/edmUpload', headers = headers, json = payload)
	if response.status_code == 202:
		pp.pprint(response.json())

token = getToken()
#getPortfolios(token)
postEDMUpload(token, "RL13_AVIVA_COM_EDM_updated", [4], "1")