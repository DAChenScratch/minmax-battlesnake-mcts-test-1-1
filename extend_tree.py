from utilities import getBodies
def extend(snake, data, snakeindx):
  bodies = getBodies(data)
  target = snake['head']
  u = {
    "x":target['x'],
    "y":target['y'] + 1,
  }
  d = {
    "x":target['x'],
    "y":target['y'] - 1,
  }
  r = {
    "x":target['x'] + 1,
    "y":target['y'],
  }
  l = {
    "x":target['x'] - 1,
    "y":target['y'],
  }
  x = []
  y = [u, d, l, r]
  text = ['up', 'down', 'left', 'right']
  x2 = []
  for move in y:
    if -1<move['x']<data['board']['width'] and -1<move['y']<data['board']['height']:
      if move in bodies:
        for snk in data['board']['snakes']:
          if move == snk['head'] and snake['length']>snk['length'] and snakeindx>data['board']['snakes'].index(snk):
            x.append(move)
            x2.append(text[y.index(move)])
      else:
        x.append(move)
        x2.append(text[y.index(move)])
  return x, x2