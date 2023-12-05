#Jack Lester Pd:8

import math
# 1
def getHypotenuse(arg1,arg2):
    product = 3**2 + 4**2 
    product = math.sqrt(product)
    
    return f"{product:.2f}"

# 2
def binaryconverter(num):
    binarystr = ""
    for x in range(8):
        binarystr = str(num % 2) + binarystr
        num = num // 2
    
    return binarystr
       
# 3
def getCapLetter():
    gettingUpletter = input("Enter a capital letter: ")
    while len(gettingUpletter) != 1 or not gettingUpletter.isupper():
        gettingUpletter = input("Enter a capital letter: ")
    return gettingUpletter

# 4
def getLowerLetter():
    getlowletter = input("Enter a lowercase letter: ")
    while len(getlowletter) != 1 or not getlowletter.islower():
        getlowletter = input("Enter a lowercase letter: ")
    return getlowletter

# 5
def getInteger():
    getint = input("Enter an Integer: ")
    while getint.isalpha() == True:
        getint = input("Enter an Integer: ")
    return getint

#6
def getNum(a, b):
    gettingNumber = input(f"Enter a number between {a} and {b}: ")
    while "1" < gettingNumber < "10":
        return float(gettingNumber)
    while not "1" < gettingNumber < "10":
        gettingNumber = input(f"Enter a number between {a} and {b}: ")
        return float(gettingNumber)

#7
def summation(*args):
    total = 0
    for num in args:
        total += num
    return float(total)

#8
def formatName(firstName,lastName,middleName):
    namestr = f"{lastName}, {firstName}, {middleName}"
    return(namestr)

#9
def findSomething(subString, aString):
    for x in range(len(aString) - len(subString) + 1):
        found = True
    for y in range(len(subString)):
        if aString[x + y] != subString[y]:
            found = False
            break
    if found: 
        return x
    else:
        return None


if __name__ == "__main__":
    #1
    Hypotenuse = getHypotenuse(3, 4)
    print(f"Hypotenuse is: {Hypotenuse}")
    #2
    Variable = binaryconverter(num = 12)
    print(Variable)
    #3
    gettingUpletter = getCapLetter()
    print(f"Capital Letter is : {gettingUpletter}")
    #4
    gettinglowletter = getLowerLetter()
    print(f"Lowercase is : {gettinglowletter}")
    #5
    getint = getInteger()
    print(f"Integer is : {getint}")
    #6
    a,b = 1,10
    gettingNumber = getNum(a,b)
    print(f"Your number is {gettingNumber}")
    #7
    sum = summation(1,2,3,4,5)
    print(f"The sum is {sum}" )
    #8
    lastn = "Crest"
    firstn = "Lester"
    middlen = "John"
    name = formatName(lastn,firstn,middlen)
    print(f"Your name is {name}")
    #9
    subString = "Light"
    aString = "Light weight ... Yeah buddy!"
    answer = findSomething(subString, aString)
    if answer is not None:
        print(f"The substring is {aString} and is found at index: ", answer)
    else:
        print("The substring was not found in the phrase")
    