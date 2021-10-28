'''print("A =", ord("A")) # turns letters into unicode
print("65 =", chr(65)) # turns unicode into letters'''
# a - z 97 - 122
# A -Z 65 - 90

word = input("Enter a word in Uppercase to hide: ")

secret_string = ""
for char in word:
    secret_string += str(ord(char))
print("Secret Message: ", secret_string)
word = ""

for i in range(0, len(secret_string)-1, 2):
    char_code =  secret_string[i] + secret_string[i+1]
    word += chr(int(char_code))
print("Original Message: ", word)