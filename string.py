#string.py

#This program returns a the first two and last two chars from a string

def main():

    string = str(input("Enter a phrase"))


    length = len(string)

    output = string[:2] + string[length-2:]

    print (output)

main()
