#задача про грядки
'''
s = общее пройденое расстояние
к = количество грядок
L = расстояние от колодца до первой грядки
m = ширина грядки
n = выстота грядки
формула
s = (2(L+n)+(2+k-1)m)k
'''

m = 10
n = 5
l = 7
k = 20
s = 0
i = 1
while i <= k:
  s += n*2 + l*2 + m*2*i
  i += 1
print(s)