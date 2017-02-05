# set up
from PIL import Image
from math import sqrt
import sys
img = Image.open("maze" + sys.argv[1] + ".png")
pix = img.load()
w, h = img.size
class Point:
    def __init__(self, x, y, p):
        self.x = x
        self.y = y
        self.p = p

# find bounding box and starting/ending points
l = Point(0, 0, None)
r = Point(0, 0, None)
for i in range(w):
    for j in range(h):
        if pix[i, j] == (0, 0, 0, 255):
            if l.x == 0 and l.y == 0 and l.p == None:
                l = Point(i, j, None)
            r = Point(i, j, None)
s = Point(0, 0, None)
e = Point(0, 0, None)
for i in range(l.x, r.x+1):
    if pix[i, l.y] != (0, 0, 0, 255):
       # print(i, l.y)
        e = Point(i, l.y, None)
        if s.x == 0 and s.y == 0 and s.p == None:
            s = Point(i, l.y, None)
    if pix[i, r.y] != (0, 0, 0, 255):
        #print(i, r.y)
        e = Point(i, r.y, None)
        if s.x == 0 and s.y == 0 and s.p == None:
            s = Point(i, r.y, None)
# BFS algorithm
s.x += 5
visited = []
for i in range(1000):
    visited.append([False] * 1000)
q = [s]
#visited[s.x][s.y] = True
target = None
mind = 100000000000
def inbounds(x, y):
    if x >= l.x and x <= r.x:
        if y >= l.y and y <= r.y:
            return True
    return False

while len(q) > 0:
    node = q.pop(0)

    if node.x == e.x and node.y == e.y:
        target = node
        break
    #north
    if inbounds(node.x, node.y-1) and pix[node.x, node.y - 1] != (0, 0, 0, 255) and visited[node.x][node.y-1] == False:
        q.append(Point(node.x, node.y - 1, node))
        visited[node.x][node.y-1] = True
    #south
    if inbounds(node.x, node.y+1) and pix[node.x, node.y+1] != (0, 0, 0, 255) and visited[node.x][node.y+1] == False:
        q.append(Point(node.x, node.y+1, node))
        visited[node.x][node.y+1] = True
    #east
    if inbounds(node.x+1, node.y) and pix[node.x+1, node.y] != (0, 0, 0, 255) and visited[node.x+1][node.y] == False:
        q.append(Point(node.x+1, node.y, node))
        visited[node.x+1][node.y] = True
    #west
    if inbounds(node.x-1, node.y) > 0 and pix[node.x-1, node.y] != (0, 0, 0, 255) and visited[node.x-1][node.y] == False:
        q.append(Point(node.x-1, node.y, node))
        visited[node.x-1][node.y] = True
#trace steps
while target:
    pix[target.x, target.y] = (255, 0 ,0 ,0)
    if target:
        target = target.p
# show solution
img.save("solved.png")
solve = Image.open("solved.png")
solve.show()

