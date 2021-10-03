#sphere.py

def sphereVolume(radius):
    r3 = radius**3
    v = 4/3 * 3.14 * r3
    #print(v)
    return v

def sphereArea(radius):
    r2 = radius**2
    a = 4 * 3.14 * r2
    #print(a)
    return a

def main():
    radius = eval(input("Enter the sphere radius:"))
    print("The volume of the sphere is:",sphereVolume(radius))
    print("The area of the sphere is:",sphereArea(radius))

main()
