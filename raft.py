'''
   You need to identify closest edge or corner of raft floating somewhere on x and y, 
   where x1, x2, y1, y2 are coordinats of the ragtangle raft corners
'''

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())
ans = ""

if y > y2:
   ans += "N"
if y < y1:
   ans += "S"
if x < x1:
   ans += "W"
if x > x2: 
   ans += "E"

print(ans)