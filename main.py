import bottle
from minimax_move import minimax
from extend_tree import extend
from DEPTH import dpth
def infinity():
  return float('inf')
@bottle.get('/')
def send():
  return {
    'apiversion':'1'
  }
@bottle.post('/move')
def move():
  data = bottle.request.json
  choice = minimax(data, dpth, -infinity(), infinity(), 0, len(data['board']['snakes']))
  choices = extend(data['you'], data, 0)[1]
  print('CHOICES:', choices)
  print('CHOICE:', choice)
  print('MYMOVE:', choices[choice])
  return {
    'move':choices[choice]
  }
bottle.run(host='0.0.0.0', port=1234)