def bigSorting(unsorted):
    # Write your code here
    lenDict = dict()
    for i in unsorted:
        if len(i) in lenDict:
            lenDict[len(i)].append(i)
        else:
            lenDict[len(i)] = [i]
    result = []
    for i in sorted(lenDict.keys()):
        result.extend(sorted(lenDict[i]))
            
    return result

if __name__ == '__main__':

    unsorted = ["31415926535897932384626433832795","1","3","10","3","5"]

    result = bigSorting(unsorted)