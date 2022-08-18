import sys
# Enter your code here. Read input from STDIN. Print output to STDOUT
heap = []
q = int(input())
minHeap = sys.maxsize
for i in range(q):
    query = input()
    if query[0] == "1":
        q,n = query.split()
        n = int(n)
        if  n < minHeap:
            minHeap = n
        heap.append(n)
    elif query[0] == "2":
        q,n = query.split()
        n = int(n)
        heap.remove(n)
        if minHeap == n and len(heap) > 0:
            minHeap = min(heap)
    elif query[0] == "3":
        print(minHeap)
""" 
1 3
1 65
2 65
3
2 3
1 7
3
1 -1
3
2 -1
3
2 7 """