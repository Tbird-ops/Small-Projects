import socket
#import _thread

addr = input("Please provide an address to scan. ")

print("Scanning:", addr,".")

for port in range(1,65535):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = s.connect_ex((addr,port))
  if result == 0:
    print("port", port, "is open")
  else:
    print("port ", port, "is closed")
  s.close()