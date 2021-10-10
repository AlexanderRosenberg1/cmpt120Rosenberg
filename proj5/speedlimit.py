def main():
    speed = eval(input("Enter your speed"))
    speedlimit = eval(input("Enter the speed limit"))
    over = speed - speedlimit
    if speed > speedlimit:
        over = speed - speedlimit
        fine = 50
        for i in range(over):
            fine +=5
        if speed > 90:
            fine += 200
        print ("Your fine is $", +fine)

    else:
        print("No ticket")

main()
