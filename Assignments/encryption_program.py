#Encrypter
#Maxwell Phillips
#16 May 2017
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Greeting and picture
#2)Delcare Vars
#3)Ask to encyrpt or decrypt
#4)Encrypt:
#5)Pick and print random 4 digit seed
#6)Take input and save it
#7)Print the pseudo-random new encrypted password
#8)Decrypt:
#9)Take input for the password and seed
#10)Use it to decrypt and then print that
#-------------------------------------------------------------------------------
#Import random
import random
#Print pretty key
print("="*80)
print("""

                   ENCRYPTION PROGRAM

 ad8888888888ba
dP\'         \`\"8b,
8  ,aaa,       \"Y888a     ,aaaa,     ,aaa,  ,aa,
8  8\' `8           \"8baaaad\"\"\"\"baaaad\"\"\"\"baad\"\"8b
8  8   8              \"\"\"\"      \"\"\"\"      \"\"    8b
8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
8  `\""\"\'       ,d8\"\"
Yb,         ,ad8\"
 \"Y8888888888P\"

""")
#Declare Chars
chars = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q", \
"r","s","t","u","v","w","x","y","z")
#Print Greeting
print("="*80)
print("This program will encyrpt and decrypt user passwords.")
#Ask to encyrpt or decrypt
choice = input("Please enter whether you would like to encyrpt or decrypt(1,2): ")
if(choice == "1"):
    print("\nYou have chosen to encrypt.")
    #Encrypt
    passwd = input("Please enter the password to encyrpt: ")
    #Get seed
    seed = random.randint(1000,9999)
    print("Your encryption seed is:",seed,"\nWrite this down, you will need it to decrypt your password.")
    random.seed(seed)
    #Create list to hold resulting password
    result = []
    #Create a pseudo-random list of encryption characters
    enc_chars = random.sample(chars,len(chars))
    #Loop over each character in the user's password
    for letter in passwd:
        #If that letter is in the list of characters
        if letter in chars:
            #Find the index of the letter in the list of characters
            index = chars.index(letter)
            #Find the cooresponding chracter in the random list of custom characters
            enc = enc_chars[index]
            #Append the new character to the resulting password list
            result.append(enc)
        else:
            result.append(letter)

    resulting_passwd = str(''.join(result))
    print("Your encrypted password is:",resulting_passwd)
if(choice == "2"):
    #decrypt
    print("\nYou have chosen to decrypt.")
    #Get password
    passwd = input("Please enter the password to decyrpt: ")
    #Get seed
    seed = int(input("Please enter the encryption seed: "))
    random.seed(seed)
    result = []
    #Create a pseudo-random list of encryption characters
    enc_chars = random.sample(chars,len(chars))
    #Loop over each character in the user's password
    for letter in passwd:
        #If that letter is in the list of characters
        if letter in enc_chars:
            #Find the index of the letter in the list of characters
            index = enc_chars.index(letter)
            #Find the cooresponding chracter in the random list of custom characters
            de_enc = chars[index]
            #Append the new character to the resulting password list
            result.append(de_enc)
        else:
            result.append(letter)

    resulting_passwd = str(''.join(result))
    print("Decrypted Passoword:",resulting_passwd)

else:
    print("Please run again and enter whether you would like to encyrpt or decrypt(1,2)")
