# Enter your code here. Read input from STDIN. Print output to STDOUT
def printString(string):
    for i in string:
        if i not in camelCaseLetters:
            print(i,end="")
        else:
            print(" ",end="")
            print(i.lower(),end="") 
    print()
def printStringSingular(stringList):
    for s in stringList:
        print(s.title(),end="")
    
    
camelCaseLetters = "ABCDEFGHIJKLMNOPRSTUVYZ"
while True:
    try:
        inp = input()
        firstCommand,secondCommand,string = inp.split(";")
        if firstCommand == 'S':
            if secondCommand == 'M':
                string = string.rstrip("()")
                printString(string)
            elif secondCommand == 'V':
                printString(string)
            else:
                print(string[0].lower(),end="")
                printString(string[1:])
        else:
            stringList = string.split(" ")
            if secondCommand == 'M':                
                print(stringList[0],end="")
                printStringSingular(stringList[1:])
                print("()")
            elif secondCommand == 'V':
                print(stringList[0],end="")
                printStringSingular(stringList[1:])
                print()
            else:
                printStringSingular(stringList)
                print()
                       
    except EOFError:
        break    
