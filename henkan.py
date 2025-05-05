def henkan_2to10(a):
  b=0
  c=0
  for i in range(len(str(a)),0,-1):
      b=2**(i-1)*(int(str(a)[i*-1]))
      c=b+c
  return c
def henkan_10to2(l):
  if l==0 or l==1:
      return l
  l1=l
  r=0
  l2=[]
  l3=[]
  while (1):
    if l==0 or l==1:
        break
    else:
        l=l//2
        r=r+1
  for i in range(r+1):
      l2.append(int(l1%2))
      l1=l1//2
  a=len(l2)
  for j in range(a-1,-1,-1):
      l3.append(str(l2[j]))
  a=l3[0]
  b=l3[1]
  c=a+b
  for i in range(2,len(l3)):
      a=l3[i]
      c=c+a
  return int(c)
def henkan_2to16(a):
    h = ["A","B","C","D","E","F"]
    l = []
    b = henkan_2to10(a)
    if b%16 >= 10 :
        l.append(h[b%16-10])
    while (1):
      if b < 16:
          break
    
    return l