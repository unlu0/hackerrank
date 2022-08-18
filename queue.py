q = list()
def query(n, m):
    
    if n == 1:
        q.append(m)
    elif n == 2:
        del q[0]
    elif n == 3:
        print(q[0])
    
if __name__ == '__main__':

    query(1,76)
    query(1,33)
    query(2,33)
    query(1,23)
    query(1,97)
    query(1,21)
    query(3,21)
    query(3,21)
    query(1,74)
    query(3,74)
