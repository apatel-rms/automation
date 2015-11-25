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

def postRiskAnalysis(token, analysisName, structureId, portfolioId, lossSettings, currencyExchangeRateId, currencyCode, reportingWindowStartDate, reportingWindowEndDate):
	headers = {'Authorization' : 'bearer ' + token, 'ContentType' : 'application/json'}
	payload = {
      "name": analysisName,
      "description": "",
      "position": "/structures/"+ structureId + "/portfolios/" + portfolioId,
      "lossSettings": lossSettings,
      "currencySettings": [
        {
            "setting": "currencyExchangeRateID",
            "value": currencyExchangeRateId
        },
          {
            "setting": "currencyCode",
            "value": currencyCode
        }
      ],
      "outputSettings": [
        {
            "setting": "ReportingWindowStartDate",
            "value": reportingWindowStartDate
        },
        {
            "setting": "ReportingWindowEndDate",
            "value": reportingWindowEndDate
        }
      ],
      "overriddenModelSettings": [
      ] 
  }
	response = requests.post('http://localhost:8080/riskanalyses', headers = headers, json = payload)
	print(response)

token = getToken()
analysisName = "Test1"
structureId = "10000000001"
portfolioId = "10000000001"
lossSettings = "/losssettings/test_uk_fl"
currencyExchangeRateId = "1"
currencyCode = "USD"
reportingWindowStartDate = "25 NOV 2015"
reportingWindowEndDate = "25 NOV 2016"
postRiskAnalysis(token, analysisName, structureId, portfolioId, lossSettings, currencyExchangeRateId, currencyCode, reportingWindowStartDate, reportingWindowEndDate)