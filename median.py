def findMedian(arr):
    # Write your code here
    arr = sorted(arr)
    medianIndex = len(arr)//2
    
    return arr[medianIndex]

if __name__ == '__main__':

    result = findMedian([3,4,1,2,5])
    print(result)