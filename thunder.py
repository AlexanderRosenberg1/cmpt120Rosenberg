#thunder.py
#This program calculates the distance to a lightning strike based
#the time elapsed between the flash and the thunder.

time = eval(input("How much time between the lighting and thunder? (In Seconds)"))

feet = (time * 1100)

miles = (feet/5280)

print("The distance is ", miles," mi. and ", feet, "ft."  )
