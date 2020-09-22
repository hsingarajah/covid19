# get user input
# input sender email address and password:
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
import email.encoders as encoders
import smtplib
from datetime import datetime

myTimeStamp = datetime.now()
myDateString = myTimeStamp.strftime('%B %d, %Y')


from_addr = "dailycovidalert@gmail.com"
password = "Covid19Alert!2345"
# input receiver email address.
to_addr = "test@gmail.com"
# input smtp server ip address:
smtp_server = 'smtp.gmail.com'

# email object that has multiple part:
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = Header('Ottawa Covid-19 report: '+myDateString, 'utf-8').encode()


reportData = open('ottawaDailyData.txt').read()


# attache a MIMEText object to save email content
msg.attach(MIMEText('<html><body><h1>Ottawa Covid19 Report for ' +myDateString+'</h1>' +
"<h2>"+
reportData +
"</h2>"+
'<p><img src="cid:0"></p>' +
'<p><img src="cid:1"></p>' +
'</body></html>', 'html', 'utf-8'))

#msg.attach(msg_content)

# to add an attachment is just add a MIMEBase object to read a picture locally.
with open('OttawaCovid2weekPlot.png', 'rb') as f:
    # set attachment mime and file name, the image type is png
    mime = MIMEBase('image', 'png', filename='2week.png')
    # add required header data:
    mime.add_header('Content-Disposition', 'attachment', filename='2week.png')
    mime.add_header('X-Attachment-Id', '0')
    mime.add_header('Content-ID', '<0>')
    # read attachment file content into the MIMEBase object
    mime.set_payload(f.read())
    # encode with base64
    encoders.encode_base64(mime)
    # add MIMEBase object to MIMEMultipart object
    msg.attach(mime)

# to add an attachment is just add a MIMEBase object to read a picture locally.
with open('OttawaCovid2weekAgeHist.png', 'rb') as f:
    # set attachment mime and file name, the image type is png
    mime = MIMEBase('image', 'png', filename='2week.png')
    # add required header data:
    mime.add_header('Content-Disposition', 'attachment', filename='OttawaCovid2weekAgeHist.png')
    mime.add_header('X-Attachment-Id', '1')
    mime.add_header('Content-ID', '<1>')
    # read attachment file content into the MIMEBase object
    mime.set_payload(f.read())
    # encode with base64
    encoders.encode_base64(mime)
    # add MIMEBase object to MIMEMultipart object
    msg.attach(mime)


server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
