from main import *
from static_values import *
from copy import *

GENOSIZE = 10
TOPSIZE = 3
var = 200
amp = 3

def modify(v):
    w=copy(v)
    for i in range(len(w)):
        r=randrange(-var,var+1)
        r+=1000
        r/=1000

        w[i]*=r
    return w

base = [0,1,5,20,1000000000]
old = []

for i in range(GENOSIZE):
    old.append(modify(base))

def new_generation():
    global old
    new = []
    points = [0 for i in range(GENOSIZE)]
    for i in range(GENOSIZE):
        for j in range(GENOSIZE):
            print("{} against {}".format(i,j))
            if(i==j):
                continue
            outcome=main(old[i],old[j])
            if(outcome==1):
                print("{} wins".format(i))
                points[i]+=1
            if(outcome==2):
                print("{} wins".format(j))
                points[j]+=2
    sort=sorted(points)
    low=sort[-TOPSIZE]
    sum=0
    old2 = []
    points2 = []
    best_p = 0
    for i in range(GENOSIZE):
        if(points[i]>=low):
            sum+=points[i]**amp
            old2.append(old[i])
            points2.append(points[i]**amp)
        if(points[i]>best_p):
            best_p=points[i]**amp
            best=old[i]
    for i in range(GENOSIZE-1):
        r=randint(1,sum)
        for j in range(len(old2)):
            if(r>points2[j]):
                r-=points2[j]
            else:
                new.append(modify(old2[j]))
                break
    new.append(best)
    old = new
it=0
while(True):
    filename="gen/gen"+str(it)+".txt"
    file=open(filename,mode="w")
    file.write(str(old))
    file.close()
    it+=1
    new_generation()