s = []
v = []
m = []
for x in range(10):
  a = x**2
  s.append(a)
for i in range(13):
  b = 2**i
  v.append(b)
for x in s:
  if x%2==0:
    m.append(x)
print(s)
print(v)
print(m)