import requests
import socket

### Semantics to getting current IP
# Get hostname
hostname = socket.gethostname()
# Get IP address from hostname
ip_address = socket.
print(ip_address)

print("Building request...")
### Pushing current IP to form
# Form URL
url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfh_E8dP0uW0UxRNB3zillmLIXM0kOJS09kKehwjtMutoMQzQ/formResponse"
# Data to fill
form_data = {
    'entry.1463770785':ip_address  # Push the ip address
}
print("Request complete.\nSending...")
user_agent = {
    "referer":"https://docs.google.com/forms/d/e/1FAIpQLSfh_E8dP0uW0UxRNB3zillmLIXM0kOJS09kKehwjtMutoMQzQ/viewform?fbzx=1873801810042486645",
    "user-agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0"
}