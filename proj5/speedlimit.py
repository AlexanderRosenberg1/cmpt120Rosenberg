def main():
    speed = eval(input("Enter your speed"))
    speedlimit = eval(input("Enter the speed limit"))
    over = speed - speedlimit
    if speed > speedlimit:
        over = speed - speedlimit
        fine = 50
        for i in range(over):
            fine +=5
        print ("Your fine is $", +fine)
    elif speed > 90:
        print("Your fine $200")

    elif speed <= speedlimit:
        print("No ticket")

main()
