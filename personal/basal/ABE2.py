#introduction to program:
#This program is used to calculate a person's
#Basal metabolic rate (BMR), determined by the Harris Benedict formula

redo = "y"
while (redo == "y"):

  print("Hello there! Welcome to the Automated BMR estimator.\nI am going to ask you a series of questions.\nAnswer to the best of your abilities")

  #info collection
  name = input("What is your name? ")
  print("Ok ", name, " Let's determine your daily calories ")
  weight = int(input("\nWhat is your weight in lbs? "))
  height = float(input("\nWhat is your height in inches? "))
  age = int(input("\nHow old are you? "))
  sex = input("\nAre you male or female? ")

  # metric conversion
  kg = weight/2.2
  cm = height*2.54

  #Harris Benedict formula Adapted by Rose and Shizgal
  m = (88.362 + (13.397 * kg) + (4.799 * cm) - (5.677 * age))
  f = (447.593 + (9.247 * kg) + (3.098 * cm) - (4.330 * age))

  #Activity level factors
  activity_levels = [1.2, 1.375, 1.55, 1.725, 1.9]

  print("""What is your activity level? Decide from the following:
  1. Sedentary:low activity or simple living activity
  2. Light: 1-3 days of light exercise 30-60 min
  3. Moderate: 3-5 days of 60 min of moderate exercise
  4. High: 5-7 days of 60+ minutes
  5. Extreme: 6-7 days of multiple 60+ minute of high activity exercise""")

  index = (int(input("Please select a number ")) - 1)

  # BMR & Activity
  if sex == "male":
    print("\nYou require ", m * activity_levels[index], " Calories daily, give or take around 200")
  elif sex == "female":
    print("\nYou require ", f * activity_levels[index], " Calories daily, give or take around 200")
  else:
    print("\nSorry, invalid input detected")
  redo = input("Would you like to start over? (y/n): ")

print("\nThank you for using Tristan's Automated BMR Estimator")
input("Please hit enter to continue")
