from maths import distance_between
def closest(origin, li, heads):
  closest_distance = 99999999
  #thisIndex = 0
  for dct in li:
    if distance_between(origin, dct) < closest_distance:
      closest_distance = distance_between(origin, dct)
      #thisIndex = li.index(dct)
  if not closest_distance == 99999999:
    return closest_distance
  else:
    return 0