import requests
import datetime as date

today = date.datetime.now()
year = today.strftime('%Y')
month = today.strftime('%m')
day = today.strftime('%d')

print("Building request")
url = 'https://docs.google.com/forms/d/e/1FAIpQLSdCSHjYHAK_DSevvbRM6Q4uhPduCoK1elYYDZvOfbNQkROw1g/formResponse'
form_data = {
  'entry.1268423644':'Tristan', #First Name
  'entry.504710437':'Stapert', #Last Name
  'entry.1332939157':'3rd Period AP Computer Science Principles', #Class Period Selection
  'entry.1241243991_year':year, #Grab year from computer
  'entry.1241243991_month':month, #grab month
  'entry.1241243991_day':day,  #grab day
  'emailAddress':'tristan.stapert.21@stu.tumwater.k12.wa.us', #email
  'emailReceipt':'',
  'g-recaptcha-response':'',
  'fvv':'1',
  'draftResponse':[],
  'pageHistory':'0',
  'fbzx':''}
print("request complete")
print("sending...")
user_agent = {'referer':'https://docs.google.com/forms/d/e/1FAIpQLSdCSHjYHAK_DSevvbRM6Q4uhPduCoK1elYYDZvOfbNQkROw1g/viewform','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'}
r = requests.post(url, data=form_data, headers=user_agent)
print("sent!")