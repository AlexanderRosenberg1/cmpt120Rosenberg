def and_g(a,b):
    
    if a == 1 and b == 1:
        return True
    else:
        return False
    if __name__=='__main__':
        print(and_g(1, 1))
 
    
def or_g(a,b):
    
    if a == 1 or b ==1:
        return True
    else:
        return False
    if __name__=='__main__':
        print(or_g(0, 0))

def not_g(a):

    return not(a)
    if __name__=='__main__':
        print(not_g(0))

def xor_g(a, b):
    if a != b:
        return 1
    else:
        return 0
    if __name__=='__main__':
        print(xor_g(5, 5))

def nand_g(a, b):
    if a == 1 and b == 1:
        return False
    else:
        return True
if __name__=='__main__':
    print(nand_g(1, 0))

    
