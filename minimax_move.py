from get_condition import evaluate
from utilities import getBodies, getBodiesTail, head_on_head
from extend_tree import extend
from debug_logs import debug
import copy
from DEPTH import dpth
def infinity():
  return float('inf')
def minimax(data, depth, alpha, beta, snakeindx, originalsnakes):
  DPTH = dpth
  you = data['you']
  board = data['board']
  snakes = data['board']['snakes']
  bodies = getBodiesTail(data)
  am_smallest = 0
  if snakeindx>=len(snakes):
    snakeindx=0
  for snake in snakes:
    if not-1<snake['head']['x']<board['width'] or not -1<snake['head']['y']<board['height'] or snake['head'] in bodies or head_on_head(snake, snakes) and not depth==DPTH:
      if snake['id'] == you['id']:
        return -500
      else:
        if debug:
          print('SOMEONE GOT DEFEATED:', snake['name'])
        snakes.pop(snakes.index(snake))
        return 500
        if snakeindx>=len(snakes):
          snakeindx=0
    if snake['length']>snakes[snakeindx]['length']:
      am_smallest +=1
  if am_smallest==len(snakes):
    am_smallest=True
  else:
    am_smallest=False
  if depth == 0:
    this = evaluate(data, you)
    #if not snakeindx==0:
      #this = this*-1
    #print('THIS:', this)
    return this
  if snakeindx==0:
    #print('MAX')
    maxEval = -infinity()
    extended_tree = extend(you, data, snakeindx)
    children = extended_tree[0]
    txtmoves = extended_tree[1]
    best_child = None
    just_for_debug_points=[]
    for child in children:
      if debug:
        print('DEPTH:', depth, '\nCHILD:', child, '\nMODE:MAX\n')
      datacopy = copy.deepcopy(data)
      datacopy['you']['head'] = child
      datacopy['you']['body'].pop(len(datacopy['you']['body']) -1)
      datacopy['you']['body'].insert(0, child)
      eating_points = 0
      if child in datacopy['board']['food']:
        datacopy['you']['body'].append(datacopy['you']['body'][len(datacopy['you']['body']) - 1])
        if am_smallest:
          eating_points = 60*depth
        datacopy['board']['food'].pop(datacopy['board']['food'].index(child))
      datacopy['board']['snakes'][0] = copy.deepcopy(datacopy['you'])
      condition = minimax(datacopy, depth-1, alpha, beta, snakeindx + 1, originalsnakes) + eating_points
      #print('DEPTH:', depth, '\nCONDITION:', condition)
      just_for_debug_points.append(condition)
      if condition>maxEval:
        maxEval=condition
        best_child=child
      alpha = max(alpha, condition)
      if beta<=alpha:
        break
    #if depth==DPTH:
      #print('DONE!')
      #return children.index(best_child)
    if debug:
      print('YAAY:', depth, '\nRETURNING:', maxEval, '\n')
      print('MOVING:', txtmoves[children.index(best_child)], '\n')
    if not depth == DPTH:
      return maxEval + ((originalsnakes - len(snakes))*150)
    else:
      print(just_for_debug_points)
      return children.index(best_child)
  else:
    minEval = infinity()
    extended_tree = extend(snakes[snakeindx], data, snakeindx)
    children = extended_tree[0]
    txtmoves = extended_tree[1]
    worst_child = None
    for child in children:
      if debug:
        print('DEPTH:', depth, '\nCHILD:', child, '\nMODE:MIN\n')
      datacopy = copy.deepcopy(data)
      thissnake = datacopy['board']['snakes'][snakeindx]
      thissnake['head'] = child
      thissnake['body'].pop(len(thissnake['body']) - 1)
      thissnake['body'].insert(0, child)
      eating_points = 0
      if child in datacopy['board']['food']:
        thissnake['body'].append(thissnake['body'][len(thissnake['body']) - 1])
        datacopy['board']['food'].pop(datacopy['board']['food'].index(child))
        if am_smallest:
          eating_points = 60*depth
      condition = minimax(datacopy, depth-1, alpha, beta, snakeindx+1, originalsnakes) + eating_points
      #print('DEPTH:', depth, '\nCONDITION:', condition)
      if minEval > condition:
        minEval = condition
        worst_child = child
      beta = min(beta, condition)
      if beta<=alpha:
        break
    if debug:
      print('\nMuahahah:', depth, '\nRETURNING:', minEval)
      try:
        print(thissnake['name'], 'IS MOVING:', txtmoves[children.index(worst_child)], '\n')
      except:
        print('OPPONENT HAS NO CHILDREN TO MOVE TO')
    return minEval
      