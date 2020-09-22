
# Python Standard Library Modules
from pathlib import Path
from zipfile import ZipFile

import pandas as pd
from datetime import datetime
from datetime import timedelta

myTimeStamp = datetime.now()



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
covidDf.set_index( ['Case_Reported_Date'])

#times
pdToday = pd.to_datetime('today').floor('D')
pdYesterday = pdToday + pd.offsets.Day(-2)

#city specific data
TorontoOnly = covidDf[ covidDf['Reporting_PHU'] == TorontoPH]
OttawaOnly = covidDf[ covidDf['Reporting_PHU'] == OttawaPH]
DurhamOnly = covidDf[ covidDf['Reporting_PHU'] == DurhamPH]
PeelOnly = covidDf[ covidDf['Reporting_PHU'] == PeelHU]
YorkOnly = covidDf[ covidDf['Reporting_PHU'] == YorkHU]
HaltonOnly = covidDf[ covidDf['Reporting_PHU'] == HaltonHU]

#torontoNotResolved
torontoActive = TorontoOnly[ TorontoOnly['Outcome1'] == "Not Resolved"]
ottawaActive = OttawaOnly[ OttawaOnly['Outcome1'] == "Not Resolved"]
durhamActive = DurhamOnly [DurhamOnly['Outcome1'] == "Not Resolved"]
peelActive = PeelOnly [PeelOnly['Outcome1'] == "Not Resolved"]
yorkActive = YorkOnly [YorkOnly['Outcome1'] == "Not Resolved"]
haltonActive = HaltonOnly [HaltonOnly['Outcome1'] == "Not Resolved"]





torontoNew = TorontoOnly[ TorontoOnly['Case_Reported_Date'] == pdYesterday]
ottawaNew = OttawaOnly[ OttawaOnly['Case_Reported_Date'] == pdYesterday]
durhamNew = DurhamOnly [DurhamOnly['Case_Reported_Date'] == pdYesterday]
peelNew = PeelOnly[ PeelOnly['Case_Reported_Date'] == pdYesterday]
yorkNew = YorkOnly[ YorkOnly['Case_Reported_Date'] == pdYesterday]
haltonNew = HaltonOnly [HaltonOnly['Case_Reported_Date'] == pdYesterday]


torontoActiveCaseCount =torontoActive['Case_Reported_Date'].count()
ottawaActiveCaseCount =ottawaActive['Case_Reported_Date'].count()
durhamActiveCaseCount =durhamActive['Case_Reported_Date'].count()
peelActiveCaseCount =peelActive['Case_Reported_Date'].count()
yorkActiveCaseCount =yorkActive['Case_Reported_Date'].count()
haltonActiveCaseCount =haltonActive['Case_Reported_Date'].count()

GTActiveCaseCount = torontoActiveCaseCount+durhamActiveCaseCount+peelActiveCaseCount+yorkActiveCaseCount+haltonActiveCaseCount


torontoNewCaseCount =  torontoNew['Case_Reported_Date'].count()
ottawaNewCaseCount = ottawaNew['Case_Reported_Date'].count()
durhamNewCaseCount = durhamNew['Case_Reported_Date'].count()
peelNewCaseCount =  peelNew['Case_Reported_Date'].count()
yorkNewCaseCount = yorkNew['Case_Reported_Date'].count()
haltonNewCaseCount = haltonNew['Case_Reported_Date'].count()
GTANewCaseCount = torontoNewCaseCount+durhamNewCaseCount+peelNewCaseCount+yorkNewCaseCount+haltonNewCaseCount


#print (ottawaActive.tail(50))
print (ottawaNew['Case_Reported_Date'].count())
print ("New COVID19 Cases in Ottawa:\t", ottawaNewCaseCount, "\t   Active cases: ", ottawaActiveCaseCount)
print ("New COVID19 Cases in GTA:\t", GTANewCaseCount, "\t   Active cases: ", GTActiveCaseCount)
print('-------------------------------------------------------------------------------------------------------')
print ("New COVID19 Cases in Toronto:\t\t", torontoNewCaseCount, "\t   Active cases: ", torontoActiveCaseCount)
print ("New COVID19 Cases in Durham Region:\t",  durhamNewCaseCount, "\t   Active cases: ", durhamActiveCaseCount)

print ("New COVID19 Cases in Peel Region:\t", peelNewCaseCount, "\t   Active cases: ", peelActiveCaseCount)
print ("New COVID19 Cases in York Region:\t",  yorkNewCaseCount, "\t   Active cases: ", yorkActiveCaseCount)
print ("New COVID19 Cases in Halton Region:\t", haltonNewCaseCount, "\t   Active cases: ", haltonActiveCaseCount)

file = open('ottawaDailyData.txt', 'w')

file.write("New COVID19 Cases in Ottawa:\t" + str(ottawaNewCaseCount)+ "\nActive cases:\t" +str(ottawaActiveCaseCount))

file.close()

file = open('GTADailyData.txt', 'w')

file.write("New COVID19 Cases in GTA:\t" + str(GTANewCaseCount)+ "\nActive cases:\t" +str(GTActiveCaseCount))

file.close()
file = open('TorontoDailyData.txt', 'w')

file.write("New COVID19 Cases in Toronto:\t" + str(torontoNewCaseCount)+ "\nActive cases:\t" +str(torontoActiveCaseCount))

file.close()
file = open('DurhamDailyData.txt', 'w')

file.write("New COVID19 Cases in Durham Region:\t" + str(durhamNewCaseCount)+ "\nActive cases:\t" +str(durhamActiveCaseCount))

file.close()
file = open('PeelDailyData.txt', 'w')

file.write("New COVID19 Cases in Peel Region:\t" + str(peelNewCaseCount)+ "\nActive cases:\t" +str(peelActiveCaseCount))

file.close()
file = open('YorkDailyData.txt', 'w')

file.write("New COVID19 Cases in York Region:\t" + str(yorkNewCaseCount)+ "\nActive cases:\t" +str(yorkActiveCaseCount))

file.close()
file = open('HaltonDailyData.txt', 'w')

file.write("New COVID19 Cases in Halton Region:\t" + str(haltonNewCaseCount)+ "\nActive cases:\t" +str(haltonActiveCaseCount))

file.close()

print('test')
txt = open('ottawaDailyData.txt').read()
print (txt)
#print (covidDf.dtypes)
#print (pdToday)
#print (pdYesterday)
#print (pd.DataFrame(covidData, columns=['Case_Reported_Date','Outcome1', 'Reporting_PHU']).tail(10))


#sampleTail = pd.DataFrame(covidData, columns=['Case_Reported_Date','Outcome1', 'Reporting_PHU']).tail(10)
#print (covidData.tail(1))