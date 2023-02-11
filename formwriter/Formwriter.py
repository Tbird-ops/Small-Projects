import requests
import datetime as date

today = date.datetime.now()
year = today.strftime('%Y')
month = today.strftime('%m')
day = today.strftime('%d')

print("Building request")
url = '<GOOGLE FORM POST URL HERE>'
form_data = {
  'entry.1268423644':'<FNAME>', #First Name
  'entry.504710437':'<LNAME>', #Last Name
  'entry.1332939157':'<OTHER DATA>', #Class Period Selection
  'entry.1241243991_year':year, #Grab year from computer
  'entry.1241243991_month':month, #grab month
  'entry.1241243991_day':day,  #grab day
  'emailAddress':'<EMAIL>', #email
  'emailReceipt':'',
  'g-recaptcha-response':'',
  'fvv':'1',
  'draftResponse':[],
  'pageHistory':'0',
  'fbzx':''}
print("request complete")
print("sending...")
user_agent = {
  'referer':'<GOOGLE FORM HEADER REFERER',
  'user-agent':'<USER AGENT>'}
r = requests.post(url, data=form_data, headers=user_agent)
print("sent!")