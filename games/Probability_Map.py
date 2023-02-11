# A script designed to ease mapping of probable outcomes to a given event

#import turtle as trtl    # <-- could draw out a probability tree
#import math              # <-- May be useful for prebuilt mathematical functions
#import tkinter           # <-- build a GUI for ease of use?
#import matplotlib        # <-- build graphs showing the Law of large numbers trend data
import random as rand    # <-- Random generation. The "luck" in the probability
#import time              # <-- could add a little fun to the game.

#-- Setup --#

numTries = None

#-- Functions --#
def numAttempts():
  global numTries
  numTries = int(input("How many times would you like the event to be cycled?  "))

def analyze(outcomes, results):
  analysis = dict()
  for i in range(len(outcomes)):
    analysis[outcomes[i]] = 0
  
  #for everything item in the results, check it with respect to the dictionary, then add 1 for each occurance 
  for key in analysis:
    for product in results:
      if product == key:
        newValue = analysis.get(key) + 1
        analysis[key] = newValue
  return analysis

def coinToss():
  # event showcasing a 50% equal probability
  
  outcomes = ["H","T"]
  results = []

  for i in range(numTries):
    result = rand.choice(outcomes)
    results.append(result)

  analysis = analyze(outcomes, results)

  return results, analysis


def D6roll():
  # event with a standard 6-sided die

  outcomes = [1,2,3,4,5,6]
  results = []

  for i in range(numTries):
    result = rand.choice(outcomes)
    results.append(result)

  return results


def cardPick():
  # event with standard deck of cards (A-K, SHCD)
  suits = ["S","H","C","D"]
  values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
  outcomes = []
  results = []

  for s in suits:
    for c in values:
      card = c + ":" + s
      outcomes.append(card)
  
  for i in range(numTries):
    result = rand.choice(outcomes)
    results.append(result)

  return results


def Roulette():
  # the odds of a roullette wheel (18 red, 18 black, 2 green)
  # blacks: 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35
  # reds: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
  # greens: 0, 00
  pass

def customEvent():
  # Build your own. Indicate the variables, and prefered outcome
  pass

def main():
  while True:
    print('''
    Probability Test Options:
    1. Coin Toss
    2. 6-sided die roll
    3. Card Pick
    4. Roulette Wheel
    5. Build your own!
    6. Exit program
    ''')
    try:
      selection = int(input("Please select a number!  "))
      if selection == 1:
        numAttempts()
        outcome = coinToss()
      elif selection == 2:
        numAttempts()
        outcome = D6roll()
      elif selection == 3:
        numAttempts()
        outcome = cardPick()
      elif selection == 4:
        numAttempts()
        outcome = Roulette()
      elif selection == 5:
        numAttempts()
        outcome = customEvent()
      elif selection == 6:
        break
      else:
        "Invalid Input detected"
      print(outcome)
    except: Exception

#-- Initialize --#
print("""
#########################################################
######### Welcome to the Probability Map v1.0! ##########
#########################################################


This utility is designed to GENERATE results for various
events in which there are equally probable outcomes.
Not only will it generate results, it will also provide
OPERATIONS for mathematical data, but also GRAPHICAL 
outcomes and VISUALLY AIDING designs.
                                          -- Tbird
""")
main()

