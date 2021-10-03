#convert_list.py

def toNumbers(strList):

    myList = list(strList)
    
    for i in range(0,len(myList)):
        myList[i] = int(myList[i]) # JA: You need to convert a string into a number
        i += 1

    print(myList)

def main():

    toNumbers(input("Enter your string: "))

main()
