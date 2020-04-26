from rsa import rsa
from calculating_d import calculating_d
import binascii
import random
import math
import sys,time
from rsa_encryption import rsa_encryption

introfile = open("intro.txt",'r')
print(introfile.read())
introfile.close()
iwannaread = input()
if iwannaread.lower() == 'y':
        print("Great")
else:
        sys.exit()


def print_slow(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.01)

x = input("You are Alice, Enter a number for x(plaintext): ")
print_slow("GENERATING THE PRIVATE KEY/PUBLIC KEY PAIR-\n")
print_slow("STEP 1 -\nNow Bob will randomly generate a private key.\n His computer will generate two prime numbers\n and then multiply them together\nIn this case, I simply choose\n two random prime numbers from a txt file\n\n")
p = random.choice(open("2-to-200k.txt").readlines())
q = random.choice(open("2-to-200k.txt").readlines())
p = int(p)
q = int(q)
print_slow("P = {} and Q = {}".format(p,q))


print("\npress to continue..")
iwannaread = input()
if iwannaread.lower().islower():
    print("")
n = p*q
print_slow("STEP 2-\nOnce we have P and Q, we multiply those together to get n: {}\n\n".format(n))

print("\npress to continue..")
iwannaread = input()
if iwannaread.lower().islower():
    print("")

print_slow("STEP 3-\nNow Bob will have to find a value \nfor e(which is the exponent needed for encryption).\n e is a random number chosen within\n the domain of n: {}\n\n".format(n))
while True:
    e = random.randint(1,100)
    print("Testing...")
    print("Finding a value for e")
    print("Can e = {}?".format(e))
    test = calculating_d(p,q,e)
    phi_n = (p-1)*(q-1)
    if math.gcd(phi_n,e) == 1 and test.calculate != -1:
         break
print_slow("\n\nTo find e, it must meet certain conditions.\n It first has to have a gcd(phi(n),e) = 1 and\n there also must be an inverse of e\n in modulo phi(n) in order to\n decrypt.The Extended Eucledian Algorithm\n is used to find the inverse of e.\nNote: phi(n) = (P-1)*(Q-1)\n\n")

print("press to continue..")
iwannaread = input()
if iwannaread.lower().islower():
    print("")


print_slow("We found e: {}\n\n".format(e))
d = test.calculate()
print_slow("Now Bob found the inverse of e: {}.\n The inverse of e is d: {}\n. To check if d is correct, make sure e*d = 1 mod phi(n).\n[{}*{} = 1 mod {}]\n Note: d is private and not known to the public\nBonus: Notice that e is relatively small\n compared to d. That is because a smaller e\n value speeds up the encryption process!\n This does not hinder security because e is\n public. However, d must be signifcantly larger\n than e, specifically at least 0.3*n\n to be secured. d needs to be large\n because if this value is figured out,\n then a hacker can use analytical attacks\n to find phi(n) and then ultimately\n find the prime numbers and thus,\n crack RSA. SECURITY RELIES ON THE PRIME NUMBERS\n\n".format(e,d,e,d,phi_n))

print("Press to continue..")
iwannaread = input()
if iwannaread.lower().islower():
    print("")


print_slow("Great!, now Bob finally generated his private key\n (n,d) : ({},{}),\n and public key (n,e) : ({},{}) and sends over his\n public key to Alice\n\n".format(n,d,n,e))
print_slow("Alice   <---public_key({},{})--- Bob\n\n".format(n,e))

print("Press to continue..")
iwannaread = input()
if iwannaread.lower().islower():
    print("")


print_slow("ENCRYPTING PLAINTEXT:\n")
print_slow("Now Alice received Bob's public key (n,e) : ({},{})\n and now has the variables needed to encrypt her plaintext\n\n".format(n,e))
print_slow("Remember, the encryption function for RSA is y = x^e mod n\n\n")

print("Press to continue..")
iwannaread = input()
if iwannaread.lower().islower():
    print("")

alice_Ciphertext = rsa_encryption(x,e,n)
print_slow("Step-4\nThe square and multiply method can be used to speed up the encryption process.\ny={}^{} mod {}. As you can see\n Alice has the variables needed and computes y\n with the square and multiply method.\n\n".format(x,e,n,))
bine = bin(e)
print_slow("For sq and mul, we first must convert e: {}\n to binary which is : {}\n Then we simply iterate from MSB to LSB and square x if\n the processed bit is 0 and square and multiply if\n the bit is 1. (You can check code out to see the full process :)\n\n ".format(e,bine.replace("0b","")))

print("Press to continue..")
iwannaread = input()
if iwannaread.lower().islower():
    print("")


print_slow("Now Alice sends over the cipher text y: {}\n\n".format(alice_Ciphertext.encrypt()))
print_slow("Alice ----ciphertext(y = {}) ---> Bob\n\n".format(alice_Ciphertext.encrypt()))
y = alice_Ciphertext.encrypt()
print("Press to continue..")
iwannaread = input()
if iwannaread.lower().islower():
    print("")


print_slow("DECRYPTION PHASE:\n")
print_slow("Now Bob received the ciphertext y = {}, and then starts to\n decrypt the ciphertext with his\n private key (n,d): ({},{})\n\n".format(alice_Ciphertext.encrypt(),n,d))
print_slow("Usually, the decyption process is more computationally\n intensive due to the large size of d. We can use\n either the square and mulitply method or\n the CLT(Chinese Remainder Theorem). In this case,\n we will again use the Square and Multiply method.\nRemember: the decryption function is \ny^d mod n : {}^{} mod {}\n\n".format(y,d,n))

print("Press to continue..")
iwannaread = input()
if iwannaread.lower().islower():
    print("")

bob_decrypt = rsa_encryption(y,d,n)
print_slow("Step 5 -\nBob decrpyts y and gets the plaintext x = {}.\n As you can see, Alice started with a plaintext value\n and Bob received that same plaintext\n value.\nFeel free to run the code again and see different values :)\n\n".format(bob_decrypt.encrypt()))

