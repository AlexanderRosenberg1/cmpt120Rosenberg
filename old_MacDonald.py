#old_MacDonald.py

def mcd(animal,sound):
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print("And on the farm he had a",animal + ", Ee-igh, Ee-igh, Oh!")
    print("With a",sound + ",",sound,"here and a",sound + ",",sound,"there.\nHere a",sound + ", there a",sound +", everywhere a",sound + ",",sound + ".")
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    
def main():
    # JA: You can decompose this into better functions
    mcd("cow","moo" )
    print("======================================================================")
    mcd("pig","oink" )
    print("======================================================================")
    mcd("hen","cluck" )
    print("======================================================================")
    mcd("dog","woof" )
    print("======================================================================")
    mcd("sheep","bah" )
main()

