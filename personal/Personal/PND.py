#Use this program to determine a prime numbers in a given range.

#THIS CONTAINS A FILE DEPENDENCY!!!

#functions
def get_all_factors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors

def range_numbers():
  file = open("prime.csv", mode='w')
  r1 = int(input("Lowest number?"))
  r2 = int(input("Highest number?"))
  for i in range(r1, r2):
    list_of_factors = get_all_factors(i)
    prime = len(list_of_factors)
    print("factors of {} are: {}".format(i,list_of_factors))
    if prime == 1:
      num = str(i)
      print("PRIME")
      file.write("{} \n".format(num))
    elif prime == 2:
      num = str(i)
      print("PRIME")
      file.write("{} \n".format(num))
  file.close()

def single_prime():
  num = int(input("What is your number? "))
  list_of_factors = get_all_factors(num)
  prime = len(list_of_factors)
  print("factors of {} are: {}".format(num,list_of_factors))
  if prime == 1:
    print("PRIME")
  elif prime == 2:
    print("PRIME")
  else:
    print("NOT PRIME")

def read_prime():
  file = open("prime.csv", mode="r")
  for line in file:
    print(line)
  file.close()

#Initiation
inquery = True
while inquery == True:
  print("Would you like a single determination or range?")
  response = input("(single/range/read/quit): ")
  response_checked = response.lower()

  if response_checked == "single":
    single_prime()
  elif response_checked == "range":
    range_numbers()
    print("See all determined prime numbers in prime.csv\n")
  elif response_checked == "read":
    read_prime()
  elif response_checked[0] == "q":
    inquery = False
  else:
    print("Sorry, something when wrong. Would you like to try again?\n")
    userin = input("(y/n): ")
    if userin == "n":
      inquery = False
print("Have a nice day")


