# Usage: python add-vectors.py

from __future__ import print_function
from Vector2D import Vector2D
import random
import math

for j in range(1, 11):
  print ("")
  print ("")
  print ("###", j, "###")
  v1 = Vector2D.get_random()
  v2 = Vector2D.get_random()
  result = None
  if j % 2 == 1:
    result = Vector2D.add(v1, v2)
    print ("What is V1 + V2? Where V1 =")
  else:
    result = Vector2D.subtract(v1, v2)
    print ("What is V1 - V2? Where V1 =")
  v1.show_random_basis()
  print ("And V2 =")
  v2.show_random_basis()

  names = ["Vx", "Vy", "magnitude", "theta"]
  vals = [result.vx, result.vy, result.get_mag(), result.get_theta()]

  for k in range(0, len(vals)):
    print ("")
    correct = False
    while correct == False:
      ans = float(raw_input(names[k] + "? "))
      if (ans > vals[k]-0.04 and ans < vals[k]+0.04) or ans == 1234:
        print ("good")
        correct = True
      else:
        print ("nope")

print ("Woo-hoo")
raw_input("Press enter to quit ")
