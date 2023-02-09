import random

numbers = []

def Status():
  print(numbers)

def Generate():
  for i in range(0,1000):
    number = random.randint(-100,100)
    numbers.append(number)

def Organize():
  pass

def Analyze():
  pass




""" document = open("numbers.txt", mode='w')



  document.write("{} \n".format(number))

document.close() """