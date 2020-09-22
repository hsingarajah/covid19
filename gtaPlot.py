
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

EOPH = "Eastern Ontario Health Unit"
HaltonPH ="Halton Region Health Department"
KingstonPH="Kingston, Frontenac and Lennox & Addington Public Health"
LanarkPH = "Leeds, Grenville and Lanark District Health Unit"
PeelPH = "Peel Public Health"
YorkPH = "York Region Public Health Services"

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
covidDf.set_index( ['Case_Reported_Date'])

# collect data for specific health units
OttawaOnly = covidDf[ covidDf['Reporting_PHU'] == OttawaPH]
TorontoOnly = covidDf[ covidDf['Reporting_PHU'] == TorontoPH]
DurhamOnly = covidDf[ covidDf['Reporting_PHU'] == DurhamPH]
HaltonOnly = covidDf[ covidDf['Reporting_PHU'] == HaltonPH]
PeelOnly = covidDf[ covidDf['Reporting_PHU'] == PeelPH]
YorkOnly = covidDf[ covidDf['Reporting_PHU'] == YorkPH]

#only GTA
GTAOnly = pd.concat([TorontoOnly, DurhamOnly, YorkOnly, PeelOnly,HaltonOnly])


Ottawa2Weeks = OttawaOnly.loc[(OttawaOnly['Case_Reported_Date'] >= pd2weeks) & (OttawaOnly['Case_Reported_Date'] <= pdYesterday)]
GTA2Weeks = GTAOnly.loc[(GTAOnly['Case_Reported_Date'] >= pd2weeks) & (GTAOnly['Case_Reported_Date'] < pdYesterday)]

Ottawa2WeeksActive = Ottawa2Weeks[ Ottawa2Weeks['Outcome1'] == "Not Resolved"]
Ottawa2WeeksActive = pd.DataFrame(Ottawa2WeeksActive, columns=['Case_Reported_Date','Outcome1'])
Ottawa2WeeksActive = Ottawa2WeeksActive.rename(columns={'Outcome1':'New Cases'})

GTA2WeeksActive = GTA2Weeks[ GTA2Weeks['Outcome1'] == "Not Resolved"]
#GTA2WeeksActive = pd.DataFrame(GTA2WeeksActive, columns=['Case_Reported_Date','Outcome1','Reporting_PHU'])
#GTA2WeeksActive = GTA2WeeksActive.rename(columns={'Outcome1':'New Cases'})


GTA2WeeksActive = pd.DataFrame(GTA2WeeksActive, columns=['Case_Reported_Date','Reporting_PHU'])
#GTA2WeeksActive.to_csv('gtatemp.csv',index=False)

#print (Ottawa2WeeksActive)

#GTAPlot = GTA2WeeksActive.groupby( GTA2WeeksActive['Case_Reported_Date'].dt.day).count().plot(kind='line')

fig,ax = plt.subplots()

print (GTA2WeeksActive[GTA2WeeksActive['Reporting_PHU'] == TorontoPH].groupby( GTA2WeeksActive['Case_Reported_Date'])['Reporting_PHU'].describe()   )
GTA2WeeksActive[GTA2WeeksActive['Reporting_PHU'] == TorontoPH].groupby( GTA2WeeksActive['Case_Reported_Date'])['Reporting_PHU'].count().plot(kind='line',ax=ax, label = 'Toronto',marker = '.')
GTA2WeeksActive[GTA2WeeksActive['Reporting_PHU'] == DurhamPH].groupby( GTA2WeeksActive['Case_Reported_Date'])['Reporting_PHU'].count().plot(kind='line',ax=ax,label = 'Durham Region',marker = '.')
GTA2WeeksActive[GTA2WeeksActive['Reporting_PHU'] == PeelPH].groupby( GTA2WeeksActive['Case_Reported_Date'])['Reporting_PHU'].count().plot(kind='line',ax=ax, label = 'Peel Region',marker = '.')
GTA2WeeksActive[GTA2WeeksActive['Reporting_PHU'] == YorkPH].groupby( GTA2WeeksActive['Case_Reported_Date'])['Reporting_PHU'].count().plot(kind='line',ax=ax, label = 'York Region',marker = '.')
GTA2WeeksActive[GTA2WeeksActive['Reporting_PHU'] == HaltonPH].groupby( GTA2WeeksActive['Case_Reported_Date'])['Reporting_PHU'].count().plot(kind='line',ax=ax, label = 'Halton',marker = '.')

ax.legend()
#print(GTA2WeeksActive)
plt.xlabel('Date')
plt.ylabel('Number of new cases')
plt.grid(True)
plt.title('New COVID19 Cases in GTA, the past 2 weeks')
plt.savefig('GTACovid2weekline.png')
plt.show()
