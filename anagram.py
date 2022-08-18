def anagramDif(a,b):

    result = []
    for i,j in zip(a,b):
        result.append(anagramDif2(i,j))

    return result

def anagramDif2(a,b):
    chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","0","1","2","3","4","5","6","7","8","9"]
    counts = []
    result = []

    for t in chars:
        counts.append(0)

    if len(a) != len(b):
        return -1
    
    for i in a:
        counts[chars.index(i)] +=1

    for j in b:
        counts[chars.index(j)] -=1

    result = 0

    for x in counts:
        result += abs(x)

    return int(result / 2)    

a = ["aaa","bafdas","fdasfasdgsgfsagdsgfdgsgfdsfg"]
b = ["bbb","asdsgd","afdsafasdfdasfsafsgdfsgdggre"]

print(anagramDif(a,b))