
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
Ottawa2Weeks = OttawaOnly.loc[(OttawaOnly['Case_Reported_Date'] >= pd2weeks) & (OttawaOnly['Case_Reported_Date'] <=  pdYesterday)]

Ottawa2WeeksActive = Ottawa2Weeks[ Ottawa2Weeks['Outcome1'] == "Not Resolved"]
Ottawa2WeeksActive = pd.DataFrame(Ottawa2WeeksActive, columns=['Case_Reported_Date','Age_Group','Reporting_PHU'])


fig,ax = plt.subplots()
age_order = ['<20','20s','30s','40s','50s','60s','70s','80s','90s']

Ottawa2WeeksActive.groupby('Age_Group')['Age_Group'].count().loc[age_order].plot(kind='bar',ax=ax, label="COVID19 Age Distribution")

ax.legend()
plt.xlabel('Age Group')
plt.ylabel('Number of new cases')
plt.title('Ottawa New COVID cases by Age group (Past 2 weeks)')
plt.savefig('OttawaCovid2weekAgeHist.png')
plt.show()

print (Ottawa2WeeksActive)
