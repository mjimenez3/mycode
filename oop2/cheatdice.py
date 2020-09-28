#!/usr/bin/env python3

from random import randint

class Player:
  def __init__(self):
    self.dice = []

  def roll(self):
    self.dice = [] # clears current dice
    for i in range(3):
      self.dice.append(randint(1,6))

  def get_dice(self):
    return self.dice #shares dice

class Cheat_Swapper(Player): # new class
  def cheat(self):  
    self.dice[-1] = 6  # last die is = 6

class Cheat_Loaded_Dice(Player):
  def cheat(self):
    i = 0
    while i < len(self.dice): # i is less than length of list (3)
      if self.dice[i] < 6:  # if first die is less than 6
        self.dice[i] += 1 #then add 1 to die
      i += 1  # add 1 to i, and loop again.

