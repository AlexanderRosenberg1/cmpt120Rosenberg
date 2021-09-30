#convert_list.py

def toNumbers(strList):

    myList = list(strList)
    
    for i in range(0,len(myList)):
        myList[i] = ord(myList[i])
        i += 1

    print(myList)

def main():

    toNumbers(input("Enter your string: "))

main()
