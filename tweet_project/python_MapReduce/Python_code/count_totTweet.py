f = open("res3ORDINATO.txt", "r")
c = 0
res = 0
tz = 0
print '[',
for line in f.readline().split():
     c+=1
     if(c%2)==0:
             print line[:-1] +',',
             #print 'Time Zone', tz,' Numero tweet' ,int(line[:-1])
             res += int(line[:-1])
             tz += 1
print ']'
print 'Tweet totali: ', res
