import math

def RSA(p:int, q:int, msg:str):

    # Calculate n = pq
    n = p*q 
    # Calculate the totient function, phi(n) = (q-1)(p-1) 
    phi = (q-1)*(p-1)

    #Calculate an e value that is coprime to phi(n)
    # e = euc_gcd(e, phi) -> this is your public key 
    e = calculate_e(phi)
    print("Your public key is: (" + str(e) + ", " + str(n) + ")")
    #Calculate d where e*d = 1mod(n), makes up the private key
    d = calculate_d(e, phi)
    print("Your private key is: (" + str(d) + ", " + str(n) + ")")

    cypher_txt = ''
    
    
    for ch in msg:
        #Converts message into cypher text 
        
        #Replaces all characters with ASCii symbols, encrypts characters 
        char = ord(ch); 
        print(str(ch) + ": " + str(char))

        # C = (P^e) mod n
        cypher_txt += chr((char ** e) % n)
    
    plain_txt = ''

    for ch in cypher_txt:
        #Decrypts encrypted text 

        #Convert to ASCii 
        char = ord(ch); 
        print(str(ch) + ": " + str(char))

        #Convert characters in order to reconstruct message
        # P = (C^d) mod n
        plain_txt += chr((char ** d) % n)


    return(cypher_txt, plain_txt)


def calculate_e(phi: int): 
    # Calculate the public key based on phi(n)
    # e must meet the conditions 1 < e < phi(n) and coprime to phi(n)

    e = 2
    while e < phi: 
        # If e is coprime to phi(n), gcd will be 1
        if euc_gcd(e, phi) == 1:
            return e
        e+=1

def calculate_d(e: int, phi: int): 
    # Calculate private key based on e and phi(n)
    # d = e^-1 mod phi(n)
    d = pow(e, -1, phi)
    return d

def euc_gcd(x: int, y: int):
    # Use the Euclidean algorithm to find the greatest 
    # common divisor of x and y
    
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