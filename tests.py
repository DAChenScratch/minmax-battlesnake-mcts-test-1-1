from minimax_move import minimax
from extend_tree import extend
from DEPTH import dpth
from datetime import datetime
def getretDate():
  this = datetime.now()
  this = str(this)
  this = this.split(" ")
  this = this[1].split(":")
  for i in range(len(this)):
    this[i] = float(this[i])
  return this
#Compares date
def comparedate(one, two):
  diff =  [
    two[2] - one[2],
    two[1] - one[1],
    two[0] - one[0]
  ]
  diff.reverse()
  return diff

def infinity():
  return float('inf')
data = {"game":{"id":"80186","ruleset":{"name":"standard","version":"v.1.2.3"},"timeout":500},"turn":200,"you":{"health":100,"id":"you","name":"#22aa34","body":[{"x":3,"y":4},{"x":3,"y":3},{"x":3,"y":2}],"head":{"x":3,"y":4},"length":3},"board":{"food":[{"x":3,"y":5},{"x":7,"y":2}],"height":11,"width":11,"snakes":[{"health":100,"id":"you","name":"#22aa34","body":[{"x":3,"y":4},{"x":3,"y":3},{"x":3,"y":2}],"head":{"x":3,"y":4},"length":3},{"health":100,"id":"#FFc187","name":"#FFc187","body":[{"x":3,"y":6},{"x":3,"y":7},{"x":3,"y":8},{"x":3,"y":9},{"x":3,"y":10}],"head":{"x":3,"y":6},"length":5}]}}
first=getretDate()
choice = minimax(data, dpth, -infinity(), infinity(), 0, len(data['board']['snakes']))
second=getretDate()
time_spent = comparedate(first, second)
for thing in time_spent:
  print(thing)
choices = extend(data['you'], data, 0)[1]
print(choices)
print(choice)
print('MYMOVE:', choices[choice])
#print('SCORE:', choice)