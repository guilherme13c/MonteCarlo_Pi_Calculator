from matplotlib import pyplot as plt
import numpy as np

tries = 1000
points = []

def point():
  
  x = np.random.random()*2-1
  y = np.random.random()*2-1
  
  return (x, y)

def solve_y(point:tuple):
  
  x = point[0]
  y = (1-(x**2))**(1/2)
  
  return [-y, y]
  
def check_point(point:tuple):
  
  y = point[1]
  Py = solve_y(point)
  
  if y >= Py[0] and y <= Py[1]:
    return 1
  else:
    return 0

for i in range(tries):
  
  p = point()
  points.append(check_point(p))
  
  if check_point(p) == 1:
    plt.scatter(p[0], p[1], color='c')
  else:
    plt.scatter(p[0], p[1], color='r')
  
print(4*(points.count(1)/len(points)))

plt.show()