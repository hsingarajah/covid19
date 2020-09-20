
# Python Standard Library Modules
from pathlib import Path
from zipfile import ZipFile

import pandas as pd
from datetime import datetime
from datetime import timedelta

import logging
import itertools
import csv

#healthUnit Tags
OttawaPH = "Ottawa Public Health"
TorontoPH = "Toronto Public Health"
DurhamPH = "Durham Region Health Department"


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


covidData = pd.read_csv(localDataFilename)

covidDf = pd.DataFrame(covidData, columns=['Case_Reported_Date', 'Age_Group','Case_AcquisitionInfo','Outbreak_Related','Outcome1', 'Reporting_PHU','Reporting_PHU_City'])

#city specific data
TorontoOnly = covidDf[ covidDf['Reporting_PHU'] == TorontoPH]
OttawaOnly = covidDf[ covidDf['Reporting_PHU'] == OttawaPH]
DurhamOnly = covidDf[ covidDf['Reporting_PHU'] == DurhamPH]

#torontoNotResolved
torontoActive = TorontoOnly[ TorontoOnly['Outcome1'] == "Not Resolved"]
ottawaActive = OttawaOnly[ OttawaOnly['Outcome1'] == "Not Resolved"]
durhamActive = DurhamOnly [DurhamOnly['Outcome1'] == "Not Resolved"]


print (ottawaActive)
print ("Active COVID19 Cases in Toronto: ", torontoActive.shape[0])
print ("Active COVID19 Cases in Durham: ",  durhamActive.shape[0])
print ("Active COVID19 Cases in Ottawa: ",  ottawaActive.shape[0])
#print (pd.DataFrame(covidData, columns=['Case_Reported_Date','Outcome1', 'Reporting_PHU']).tail(10))


#sampleTail = pd.DataFrame(covidData, columns=['Case_Reported_Date','Outcome1', 'Reporting_PHU']).tail(10)
#print (covidData.tail(1))