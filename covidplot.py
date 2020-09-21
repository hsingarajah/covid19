
import pandas as pd
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt

import logging
import itertools
import csv

#healthUnit Tags
OttawaPH = "Ottawa Public Health"
TorontoPH = "Toronto Public Health"
DurhamPH = "Durham Region Health Department"

EOHU = "Eastern Ontario Health Unit"
HaltonHU ="Halton Region Health Department"
KingstonHU="Kingston, Frontenac and Lennox & Addington Public Health"
LanarkHU = "Leeds, Grenville and Lanark District Health Unit"
PeelHU = "Peel Public Health"
YorkHU = "York Region Public Health Services"

# get current date
# set days 0
currentDate = str(datetime.date(datetime.now() - timedelta(days=0))) + " " + "00:00:00"
dateString = datetime.now().strftime("%A %B %d, %Y").replace(" 0", " ")
localDataFilename = 'OntarioCovid19Data.csv'

#times
pdToday = pd.to_datetime('today').floor('D')
pdYesterday = pdToday + pd.offsets.Day(-1)
pd2weeks = pdYesterday + pd.offsets.Day(-14)

covidData = pd.read_csv(localDataFilename, parse_dates=[2,3,4])
covidDf = pd.DataFrame(covidData, columns=['Case_Reported_Date', 'Age_Group','Case_AcquisitionInfo','Outbreak_Related','Outcome1', 'Reporting_PHU','Reporting_PHU_City'])


# last 2 weeks
OttawaOnly = covidDf[ covidDf['Reporting_PHU'] == OttawaPH]
OttawaOnly.set_index( ['Case_Reported_Date'])
print (OttawaOnly.dtypes)
print (type(pd2weeks.to_datetime64()))
print (type(pdYesterday.to_datetime64()))
Ottawa2Weeks = OttawaOnly.loc[(OttawaOnly['Case_Reported_Date'] > pd2weeks) & (OttawaOnly['Case_Reported_Date'] < pdYesterday)]

Ottawa2WeeksActive = Ottawa2Weeks[ Ottawa2Weeks['Outcome1'] == "Not Resolved"]
Ottawa2WeeksActive = pd.DataFrame(Ottawa2WeeksActive, columns=['Case_Reported_Date','Outcome1'])
Ottawa2WeeksActive = Ottawa2WeeksActive.rename(columns={'Outcome1':'New Cases'})


print (Ottawa2WeeksActive)
OttawaPlot = Ottawa2WeeksActive.groupby( Ottawa2WeeksActive['Case_Reported_Date'].dt.day).count().plot(kind='line')
plt.xlabel('Date')
plt.ylabel('Number of new cases')
plt.grid(True)
plt.title('New COVID19 Cases in Ottawa, the past 2 weeks')
plt.savefig('OttawaCovid2weekPlot.png')
plt.show()