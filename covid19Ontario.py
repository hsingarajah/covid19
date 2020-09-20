
# Python Standard Library Modules
from pathlib import Path
from zipfile import ZipFile

import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import logging
import itertools
import csv

# dictionary keys
dataDate = 'Date'
sporCase = 'Sporadic Cases'
comCase = 'Community Cases'
instCase = 'Institutional Cases'
cummCase = 'Cumulative Cases'
cummDeath = 'Cumulative Deaths'

# thresholds
newCaseThres = 10

# get current date
# set days 0
currentDate = str(datetime.date(datetime.now() - timedelta(days=0))) + " " + "00:00:00"
dateString = datetime.now().strftime("%A %B %d, %Y").replace(" 0", " ")
localDataFilename = 'OntarioCovid19Data.csv'


print (currentDate)

# email stuff
import smtplib

data_path = Path('./data')
dataURL = 'https://data.ontario.ca/datastore/dump/455fd63b-603d-4608-8216-7d8647f43350'


try:
    covidRequest = requests.get(dataURL, verify=True, timeout=10)
except requests.ConnectionError as e:
    print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
    print(str(e))
    print (e.request)

    print (e.response)

except requests.Timeout as e:
    print("OOPS!! Timeout Error")
    print(str(e))
except requests.RequestException as e:
    print("OOPS!! General Error")
    print(str(e))

covid19csvFile = open(localDataFilename, "wb")
covid19csvFile.write (covidRequest.content)
covid19csvFile.close()

#covidData.rename(
 #   columns={'Earliest of symptom onset, test or reported date for cases; date of death for deaths': 'Date'},
 #   inplace=True)

#result = covidData[covidData["Date"] == currentDate].to_dict('split')


