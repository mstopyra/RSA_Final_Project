import math

def RSA(p:int, q:int, msg:str):

    n = p*q 
    phi = (q-1)*(p-1)

    e = calculate_e(phi)
    print("Your public key is: ", e)
    d = calculate_d(e, phi)
    print("Your private key is: ", d)

    cypher_txt = ''
    
    for char in msg:

        char = ord(char); 
        cypher_txt += chr((char ** e) % n)
    
    plain_txt = ''

    for char in cypher_txt:

        char = ord(char); 

        plain_txt += chr((char ** d) % n)

    return(cypher_txt, plain_txt)


def calculate_e(phi: int): 

    e = 2
    while e < phi: 
        if euc_gcd(e, phi) == 1:
            return e
        e+=1

def calculate_d(e: int, phi: int): 
    d = pow(e, -1, phi)
    return d
    
def euc_gcd(x: int, y: int):
    
    small,large = (x,y) if x<y else (y,x)

    while small != 0:
        rem = large % small
        large = small
        small = rem

    return large


if __name__ == "__main__":
    print
    p = int(input("Input a p value "))
    q = int(input("Input a q value "))
    msg = input("Enter a message you would like to be encrypted/decrypted: ")

    cypher_text, plain_text = RSA(p, q, msg)

    print("Encrypted: ", cypher_text)
    print("Decrypted: ", plain_text)