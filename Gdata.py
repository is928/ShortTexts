hs = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
l = []
for _1 in hs:
    for _2 in hs:
        l.append(_1+_2)
d1 = {}
d2 = {}
for _ in range(len(l)):
    d1[l[_]] = chr(10000+_)
    d2[chr(10000+_)] = l[_]
file = open('data.py','w')
file.write('d1 = '+str(d1)+'\n')
file.write('d2 = '+str(d2))
file.close()
