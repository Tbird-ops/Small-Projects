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
url = "<GOOGLE FORM HERE OR OTHER WEB HOOK THING"
# Data to fill
form_data = {
    '<BASED ON GOOGLE FORM ENTRY POINTS':ip_address  # Push the ip address
}
print("Request complete.\nSending...")
user_agent = {
    "referer":"<HEADER DATA>",
    "user-agent":"<HEADER DATA"
}