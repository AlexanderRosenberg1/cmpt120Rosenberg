#sphere.py

def sphereVolume(radius):
    r3 = radius^3
    v = 4/3 * 3.14 * r3
    print(v)

def sphereArea(radius):
    r2 = radius^2
    a = 4 * 3.14 * r2
    print(a)

def main():
    sphereVolume(eval(input("Enter the volume radius: ")))
    sphereArea(eval(input("Enter the area radius: ")))
main()
