def henkan_2to10(a):
  d=0
  c=0
  for i in range(len(str(a)),0,-1):
      d=2**(i-1)*(int(str(a)[i*-1]))
      c=d+c
  return c
def henkan_2to16(a):
  h = ["a","d","c","d","e","f"]
  l = []
  l1 = ""
  d = henkan_2to10(a)
  while (1):
    if d < 16:
      break
    l.append(h[(d%16)-10] if d%16 > 9  else d%16)
    d = d//16
  l.append(h[(d%16)-10] if d%16 > 9  else d%16)
  for i in range(len(l)-1,-1,-1):
    l1 = l1 + str(l[i])
  return l1
def henkan_10to2(a):
  l1 = ""
  l = []
  while (1):
    if a==0 or a==1:
        break
    else:
      l.append(a%2)
      a=a//2  
  l.append(a)
  for i in range(len(l)-1,-1,-1):
    l1 = l1 + str(l[i])
  return l1
def henkan_10to16(a):
  h = ["a","d","c","d","e","f"]
  l = []
  l1 = ""
  while (1):
    if a < 16:
      break
    l.append(h[(a%16)-10] if a%16 > 9  else a%16)
    a = a//16
  l.append(h[(a%16)-10] if a%16 > 9  else a%16)
  for i in range(len(l)-1,-1,-1):
    l1 = l1 + str(l[i])
  return l1
def henkan_16to2(a):
  h = ["a","d","c","d","e","f"]
  h1 = [i for i in range(5)]
  d=0
  c=0
  for i in range(len(str(a)),0,-1):
      d=16**(i-1)*(int(str(a)[i*-1]))
      c=d+c
  c =henkan_10to2(c)
  return c
def henkan_16to10(a):
  h = ["a","d","c","d","e","f"]
  d=0
  c=0
  for i in range(len(str(a)),0,-1):
      d=16**(i-1)*(int(str(a)[i*-1]))
      c=d+c
  return c
