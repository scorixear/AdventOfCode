import os, sys, re, time
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

match = re.search("target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)..(-?\d+)", lines[0].strip())
minX = int(match.group(1))
maxX = int(match.group(2))
minY = int(match.group(4))
maxY = int(match.group(3))

def step(x, y, velocityX, velocityY):
  x += velocityX
  y += velocityY
  if velocityX > 0:
    velocityX -= 1
  elif velocityX < 0:
    velocityX += 1
  velocityY -= 1
  return (x, y, velocityX, velocityY)

def isInTarget(x, y, minX, minY, maxX, maxY):
  returnBool = x >= minX and x <= maxX and y <= minY and y >= maxY
  isPossible = x <= maxX and y >= maxY
  return (returnBool, isPossible)

maxHeight = 0
velocityCounts = 0
for veloY in range(maxY,(maxY*-1)+1):
  for veloX in range(1, maxX+1):
    x,y,currentVeloX,currentVeloY = 0,0,veloX,veloY
    currentHeight = 0
    while True:
      x,y,currentVeloX,currentVeloY = step(x,y,currentVeloX,currentVeloY)
      inTarget,isPossible = isInTarget(x,y,minX,minY,maxX,maxY)
      currentHeight = currentHeight if y <= currentHeight else y
      if inTarget:
        velocityCounts += 1
        break
      elif not isPossible:
        break

print(velocityCounts)

