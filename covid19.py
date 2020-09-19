#arcGIS for covid ottawa data
from arcgis import GIS

# Python Standard Library Modules
from pathlib import Path
from zipfile import ZipFile

from datetime import datetime
from datetime import timedelta

import itertools
import csv
import pandas as pd

#dictionary keys
dataDate= 'Date'
sporCase='Sporadic Cases'
comCase='Community Cases'
instCase='Institutional Cases'
cummCase='Cumulative Cases'
cummDeath='Cumulative Deaths'


#thresholds
newCaseThres=10

#get current date
#set days 0
currentDate=str(datetime.date(datetime.now() - timedelta(days=0) )) + " " + "00:00:00"
dateString = datetime.now().strftime("%A %B %d, %Y").replace(" 0", " ")

print (currentDate)


#email stuff
import smtplib
username="dailycovidalert@gmail.com"
password="Covid19Alert!2345"


print ("starting covid")
public_data_item_id = 'cf9abb0165b34220be8f26790576a5e7'
print (public_data_item_id)
#download daily data
anon_gis = GIS()

data_item = anon_gis.content.get(public_data_item_id)

data_path = Path('./data')

if not data_path.exists():
    data_path.mkdir()

data_item.download(save_path=data_path)


covidData = pd.read_csv("data\COVID19CasesandDeathsinOttawaEN.csv")
covidData.rename(columns={'Earliest of symptom onset, test or reported date for cases; date of death for deaths':'Date'}, inplace=True)

result= covidData[  covidData["Date"]==currentDate].to_dict('split')

myData = dict()
try:
	for (columnItr,dataItr) in zip (result["columns"], result["data"].pop()):
		myData.update({columnItr: dataItr})
except:
	print ("Data not update for " + dateString)
	quit()

#dictionary keys
dataDate= 'Date'
sporCase='Sporadic Cases'
comCase='Community Cases'
instCase='Institutional Cases'
cummCase='Cumulative Cases'
cummDeath='Cumulative Deaths'

activeCases = myData.get(cummCase) - myData.get(cummDeath)
newCases = myData.get(sporCase) + myData.get(comCase)

print ("Active Cases:" + str(activeCases))
print ("New Cases: " + str(newCases))





#email alert
sent_from = username
to = ['hsingarajah@gmail.com']
subject = '(test)Ottawa 	Covid Alert: ' + str(newCases) + " New Cases Today"
body = 'Covid Alert: ' + str(newCases) + " New Cases in Ottawa on " + dateString

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)


if(newCases>newCaseThres):
	try:
		
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(username, password)
		server.sendmail(sent_from, to, email_text)
		server.close()

		print ('Email sent!')
	except Exception as e: 
		print ('Something went wrong...')
		print (e)



		