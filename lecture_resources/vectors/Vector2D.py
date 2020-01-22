from __future__ import print_function
import random
import math

class Vector2D:
  def __init__(self, vx, vy):
    self.vx = vx
    self.vy = vy

  @staticmethod
  def get_random():
    return Vector2D(random.uniform(-5, 5), random.uniform(-5, 5))

  @staticmethod
  def add(v1, v2):
    return Vector2D(v1.vx + v2.vx, v1.vy + v2.vy)

  @staticmethod
  def subtract(v1, v2):
    return Vector2D(v1.vx - v2.vx, v1.vy - v2.vy)

  def get_mag(self):
    return math.sqrt(self.vx*self.vx + self.vy*self.vy)

  def get_theta(self):
    th = 180.0*math.atan2(self.vy, self.vx)/math.pi
    if th < 0: th = 360.0 + th
    return th

  def show_random_basis(self):
    rand = random.randint(0, 3)
    if rand == 0: print ("Vx =", self.vx, "and Vy =", self.vy)
    elif rand == 1: print ("magnitude =", self.get_mag(), "and theta =", self.get_theta())
    elif rand == 2: print ("Vx =", self.vx, "and theta =", self.get_theta())
    elif rand == 3: print ("Vy =", self.vy, "and theta =", self.get_theta())
