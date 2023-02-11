#introduction to program:
#This program is used to calculate a person's
#Basal metabolic rate, determined by the Harris Benedict formula
#Adapted by Rose and Shizgal

redo = "y"
while (redo == "y"):

  print("Hello there! Welcome to the Automated BMR estimator.\nI am going to ask you a series of questions.\nAnswer to the best of your abilities")

  name = input("What is your name? ")



  #info collection
  print("Ok ", name, " Let's determine your daily calories ")
  weight = int(input("\nWhat is your weight in lbs? "))
  height = float(input("\nWhat is your height in inches? "))
  age = int(input("\nHow old are you? "))
  sex = input("\nAre you male or female? ")

  kg = weight/2.2
  cm = height*2.54

  #Harris Benedict formula
  m = (88.362 + (13.397 * kg) + (4.799 * cm) - (5.677 * age))
  f = (447.593 + (9.247 * kg) + (3.098 * cm) - (4.330 * age))

  if sex == "male":
    print("The number of Calories your body requires to live (without even adding in exercising) is ", m, "\n\n")
  elif sex == "female":
    print("The number of Calories your body requires to live (without even adding in exercising) is ", f, "\n\n")
  else:
    print("I'm sorry, You missed something. Please start over!")

  print("What is your activity level? Decide from the following: \n1. Sedentary:low activity or simple living activity \n2. Light: 1-3 days of light exercise 30-60 min \n3. Moderate: 3-5 days of 60 min of moderate exercise \n4. High: 5-7 days of 60+ minutes \n5. Extreme: 6-7 days of multiple 60+ minute of high activity exercise\n")
  activity = input("Please select a number ")

  if activity == "1" and sex == "male":
    print("\nYou require ", m * 1.2, " Calories daily, give or take around 200")
  elif activity == "1" and sex == "female":
    print("\nYou require ", f * 1.2, " Calories daily, give or take around 200")
  elif activity == "2" and sex == "male":
    print("\nYou require ", m * 1.375, " Calories daily, give or take around 200")
  elif activity == "2" and sex == "female":
    print("\nYou require ", f * 1.375, " Calories daily, give or take around 200")
  elif activity == "3" and sex == "male":
    print("\nYou require ", m * 1.55, " Calories daily, give or take around 200")
  elif activity == "3" and sex == "female":
    print("\nYou require ", f * 1.55, " Calories daily, give or take around 200")
  elif activity == "4" and sex == "male":
    print("\nYou require ", m * 1.725, " Calories daily, give or take around 200")
  elif activity == "4" and sex == "female":
    print("\nYou require ", f * 1.725, " Calories daily, give or take around 200")
  elif activity == "5" and sex == "male":
    print("\nYou require ", m * 1.9, " Calories daily, give or take around 200")
  elif activity == "5" and sex == "female":
    print("\nYou require ", f * 1.9, " Calories daily, give or take around 200")
  else:
    print("\nSorry, invalid input detected")
  redo = input("Would you like to start over? (y/n): ")

print("\nThank you for using Tristan's Automated BMR Estimator")
input("Please hit enter to continue")
