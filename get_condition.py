from utilities import assign, getBodies, getHeads, getPossibleMoves, indvBodies, areas_near_heads, smaller_snakes_get_heads, get_dangerous_heads
#from get_closest import closest
from corner_snake import tryCorner, can_trap
from maths import distance_between
from try_other_snakes import other_can_trap
from get_closest import closest
def evaluate(data, snake):
  moves = ['up', 'down', 'left', 'right']
  dict_moves = [data['you']['head']]
  a=0
  points_moves = [300]
  #print('DICT MOVES:', dict_moves)
  bodies = getBodies(data)
  heads = getHeads(data)
  myhead = snake['head']
  mybody = snake['body'].copy()
  health = snake['health']
  #mytail = data['you']['body'][len(data['you']['body']) - 1]
  food = data['board']['food']
  height = data['board']['height']
  width = data['board']['width']
  snakes = data['board']['snakes']
  small_heads = smaller_snakes_get_heads(data)
  indv_bodies = indvBodies(data)
  head_areas = areas_near_heads(small_heads, indv_bodies, mybody, myhead)
  danger_heads = get_dangerous_heads(data)
  '''
  me_smallest = 0
  second_smallest = 0
  can_eat = 0
  for snake in snakes:
    if len(snake['body']) >= len(mybody):
      me_smallest +=1
  if me_smallest == len(snakes):
    me_smallest = 2
  else:
    me_smallest = 1/3
  if me_smallest == 2:
    points_moves[a] -=100
  '''
  can_eat=0
  if dict_moves[a] in bodies or not -1<dict_moves[a]['x']<width or not -1<dict_moves[a]['y']<height:
    points_moves[a] = -1000 #350
  else:
    first_time = getPossibleMoves(bodies, dict_moves[a], data, mybody, True)-len(mybody)
    if first_time <1:
      points_moves[a] -=400
    else:
      can_eat +=1
    free_to_move = getPossibleMoves(bodies, dict_moves[a], data, mybody, True, depth=1)
    if free_to_move == 1:
      points_moves[a] -=70
    points_moves[a] -= closest(dict_moves[a], small_heads, heads) * 17
    if tryCorner(data, myhead, snakes):
      points_moves[a] +=140
    if dict_moves[a] in head_areas:
      #60
      points_moves[a] +=80
    for danger in danger_heads:
      if distance_between(danger, dict_moves[a]) <1.5:
        points_moves[a] += distance_between(danger, dict_moves[a]) * 170
      else:
        points_moves[a] += 260
    if can_eat == 1:
      points_moves[a] -= closest(dict_moves[a], food, heads) * 14
  return max(points_moves)