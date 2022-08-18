from mimetypes import init
from operator import indexOf

def printTower(t1,t3,t2,t1Name,t3Name,t2Name,x):
    if t1Name == x:
        print(t1)
    elif t2Name == x:
        print(t2)
    elif t3Name == x:
        print(t3)

def printTowersInOrder(t1,t3,t2,t1Name,t3Name,t2Name):
    printTower(t1,t2,t3,t1Name,t3Name,t2Name,"A")
    printTower(t1,t2,t3,t1Name,t3Name,t2Name,"B")
    printTower(t1,t2,t3,t1Name,t3Name,t2Name,"C")

def solveHanoi(t1,t2,t3,t1Name,t2Name,t3Name,k):
    if k <= 0:
        return

    solveHanoi(t1,t3,t2,t1Name,t3Name,t2Name,k-1)
    print(k,"from",t1Name,"->",t3Name)
    t3.insert(0,t1[t1.index(k)])
    del t1[t1.index(k)]
    printTowersInOrder(t1,t2,t3,t1Name,t3Name,t2Name)
    solveHanoi(t2,t1,t3,t2Name,t1Name,t3Name,k-1)

def solveHanoiNew(t1,t2,t3,k):
    if k <= 0:
        return

    solveHanoiNew(t1,t3,t2,k-1)
    print(f"{k} {t1}from->{t3}")
    solveHanoiNew(t2,t1,t3,k-1)

t1 = [1,2,3,4,5,6,7]
t2 = []
t3 = []

solveHanoi(t1,t2,t3,"A","B","C",len(t1))