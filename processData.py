
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


covidData = pd.read_csv(localDataFilename, parse_dates=[2,3,4])
covidDf = pd.DataFrame(covidData, columns=['Case_Reported_Date', 'Age_Group','Case_AcquisitionInfo','Outbreak_Related','Outcome1', 'Reporting_PHU','Reporting_PHU_City'])


#times
pdToday = pd.to_datetime('today').floor('D')
pdYesterday = pdToday + pd.offsets.Day(-1)
#city specific data
TorontoOnly = covidDf[ covidDf['Reporting_PHU'] == TorontoPH]
OttawaOnly = covidDf[ covidDf['Reporting_PHU'] == OttawaPH]
DurhamOnly = covidDf[ covidDf['Reporting_PHU'] == DurhamPH]

#torontoNotResolved
torontoActive = TorontoOnly[ TorontoOnly['Outcome1'] == "Not Resolved"]
ottawaActive = OttawaOnly[ OttawaOnly['Outcome1'] == "Not Resolved"]
durhamActive = DurhamOnly [DurhamOnly['Outcome1'] == "Not Resolved"]

torontoNew = TorontoOnly[ TorontoOnly['Case_Reported_Date'] == pdYesterday]
ottawaNew = OttawaOnly[ OttawaOnly['Case_Reported_Date'] == pdYesterday]
durhamNew = DurhamOnly [DurhamOnly['Case_Reported_Date'] == pdYesterday]


print (ottawaActive)

print ("New COVID19 Cases in Toronto:\t", torontoNew.shape[0], "\t   Active cases: ", torontoActive.shape[0])
print ("New COVID19 Cases in Durham:\t",  ottawaNew.shape[0], "\t   Active cases: ", durhamActive.shape[0])
print ("New COVID19 Cases in Ottawa:\t",  durhamNew.shape[0], "\t   Active cases: ", ottawaActive.shape[0])


#print (covidDf.dtypes)
#print (pdToday)
#print (pdYesterday)
#print (pd.DataFrame(covidData, columns=['Case_Reported_Date','Outcome1', 'Reporting_PHU']).tail(10))


#sampleTail = pd.DataFrame(covidData, columns=['Case_Reported_Date','Outcome1', 'Reporting_PHU']).tail(10)
#print (covidData.tail(1))