# Enter your code here. Read input from STDIN. Print output to STDOUT
undoCache = []
def operationOld(n, t, undo):
    global s
    global undoCache
    if n == 1:
        if not undo:    
            undoCache.append([2,len(t)])
        s += t
    elif n == 2:
        if not undo:
            undoCache.append([1,s[-t:]]) 
        s = s[:-t]
    elif n == 3:
        print(s[t-1])
    elif n == 4:
        lenCache = len(undoCache)-1
        operation(undoCache[lenCache][0],undoCache[lenCache][1],True)
        undoCache.remove(undoCache[lenCache])

cache = []
s =""
def operation(n,t):
    global cache
    global s
    if n == 1:
        last = s
        s += t
        cache.append(last)
    elif n == 2:
        last = s
        s = s[:-t]
        cache.append(last)
    elif n == 3:
        print(s[t-1])
    elif n == 4:
        s = cache.pop()


count = int(input())
for i in range(count):
    inputString = input()
    if int(inputString[0]) < 4:
        n,t = inputString.split()
        n = int(n)
        if n == 1:
            operation(n,t)
        else:
            operation(n,int(t))
    else:
        operation(int(inputString[0]),0)
""" 
8
1 abc
3 3
2 3
1 xy
3 2
4
4
3 1

c
f"""