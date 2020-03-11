try:
    import data
except:
    import Gdata
    import data
d1,d2 = data.d1, data.d2

def ecut(t):
    r,x,y = '', 0, 2
    while x < len(t):
        s = t[x:y]
        if s in d1:r +=d1[s]
        else:r+=s
        x,y = x+2, y+2
    return r

def dcut(r):
    t = ''
    for _ in r:
         if _ in d2:t+=d2[_]
         else:t+=_
    return t
