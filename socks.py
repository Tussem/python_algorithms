'''
    there are given socks and shirts of red and green. 
    You need to get shirts and socks of the same color from wordbrobe.
    But you can see what you are getting that is why you need to give minimum number things to get them
    same color. 
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())
ans = []

if a > 0 and c > 0:
    ans.append([b + 1, d +1])
if b > 0 and d > 0:
    ans.append([a + 1, c + 1])
if a > 0 and b > 0:
    ans.append([max(a, b) + 1,1])
if c > 0 and d > 0:
    ans.append([1, max(c, d) +1])

m = min(ans, key=sum)
print(*m)