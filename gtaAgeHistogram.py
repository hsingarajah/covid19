
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
TorontoOnly = covidDf[ covidDf['Reporting_PHU'] == TorontoPH]
DurhamOnly = covidDf[ covidDf['Reporting_PHU'] == DurhamPH]
HaltonOnly = covidDf[ covidDf['Reporting_PHU'] == HaltonHU]
PeelOnly = covidDf[ covidDf['Reporting_PHU'] == PeelHU]
YorkOnly = covidDf[ covidDf['Reporting_PHU'] == YorkHU]

TorontoOnly.set_index( ['Case_Reported_Date'])
DurhamOnly.set_index( ['Case_Reported_Date'])
HaltonOnly.set_index( ['Case_Reported_Date'])
PeelOnly.set_index( ['Case_Reported_Date'])
YorkOnly.set_index( ['Case_Reported_Date'])

Toronto2Weeks = TorontoOnly.loc[(TorontoOnly['Case_Reported_Date'] >= pd2weeks) & (TorontoOnly['Case_Reported_Date'] <=  pdYesterday)]
Durham2Weeks = DurhamOnly.loc[(DurhamOnly['Case_Reported_Date'] >= pd2weeks) & (DurhamOnly['Case_Reported_Date'] <=  pdYesterday)]
Halton2Weeks = HaltonOnly.loc[(HaltonOnly['Case_Reported_Date'] >= pd2weeks) & (HaltonOnly['Case_Reported_Date'] <=  pdYesterday)]
Peel2Weeks = PeelOnly.loc[(PeelOnly['Case_Reported_Date'] >= pd2weeks) & (PeelOnly['Case_Reported_Date'] <=  pdYesterday)]
York2Weeks = YorkOnly.loc[(YorkOnly['Case_Reported_Date'] >= pd2weeks) & (YorkOnly['Case_Reported_Date'] <=  pdYesterday)]



Toronto2WeeksActive = Toronto2Weeks[Toronto2Weeks['Outcome1'] == "Not Resolved"]
Durham2WeeksActive = Durham2Weeks[Durham2Weeks['Outcome1'] == "Not Resolved"]
Halton2WeeksActive = Halton2Weeks[Halton2Weeks['Outcome1'] == "Not Resolved"]
Peel2WeeksActive = Peel2Weeks[Peel2Weeks['Outcome1'] == "Not Resolved"]
York2WeeksActive = York2Weeks[York2Weeks['Outcome1'] == "Not Resolved"]


Toronto2WeeksActive = pd.DataFrame(Toronto2WeeksActive, columns=['Case_Reported_Date','Age_Group','Reporting_PHU'])
Durham2WeeksActive = pd.DataFrame(Durham2WeeksActive, columns=['Case_Reported_Date','Age_Group','Reporting_PHU'])
Halton2WeeksActive = pd.DataFrame(Halton2WeeksActive, columns=['Case_Reported_Date','Age_Group','Reporting_PHU'])
Peel2WeeksActive = pd.DataFrame(Peel2WeeksActive, columns=['Case_Reported_Date','Age_Group','Reporting_PHU'])
York2WeeksActive = pd.DataFrame(York2WeeksActive, columns=['Case_Reported_Date','Age_Group','Reporting_PHU'])


fig,ax= plt.subplots()
ax2=ax.twinx()
ax3=ax.twinx()
ax4=ax.twinx()
ax5=ax.twinx()
age_order = ['<20','20s','30s','40s','50s','60s','70s','80s','90s']
#
# Toronto2WeeksActive.groupby('Age_Group')['Age_Group'].count().loc[age_order].plot(kind='bar',ax=ax, label="Toronto")
# Durham2WeeksActive.groupby('Age_Group')['Age_Group'].count().loc[age_order].plot(kind='bar',ax=ax, label="Durham")
# Halton2WeeksActive.groupby('Age_Group')['Age_Group'].count().loc[age_order].plot(kind='bar',ax=ax, label="Halton")
# Peel2WeeksActive.groupby('Age_Group')['Age_Group'].count().loc[age_order].plot(kind='bar',ax=ax, label="Peel")
# York2WeeksActive.groupby('Age_Group')['Age_Group'].count().loc[age_order].plot(kind='bar',ax=ax, label="York")
#

Toronto2WeeksActive.groupby('Age_Group')['Age_Group'].count().loc[age_order].plot(kind='bar',ax=ax, label="Toronto", color='aqua')
Durham2WeeksActive.groupby('Age_Group')['Age_Group'].count().loc[age_order].plot(kind='bar',ax=ax, label="Durham", color='blue')
Halton2WeeksActive.groupby('Age_Group')['Age_Group'].count().loc[age_order].plot(kind='bar',ax=ax, label="Halton",color='coral')
Peel2WeeksActive.groupby('Age_Group')['Age_Group'].count().loc[age_order].plot(kind='bar',ax=ax, label="Peel",color='green')
York2WeeksActive.groupby('Age_Group')['Age_Group'].count().loc[age_order].plot(kind='bar',ax=ax, label="York",color='indigo')



ax.legend()
plt.xlabel('Age Group')
plt.ylabel('Number of new cases')
plt.title('GTA New COVID cases by Age group (Past 2 weeks)')
plt.savefig('GTACovid2weekAgeHist.png')
plt.show()


