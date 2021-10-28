word = input("Enter a word here: ")

secret = ""

for char in word:
    secret += str(ord(char) - 23)
print("Secret String: ", secret)
word = " "

for i in range(0, len(secret)-1,2):
    char_code = secret[i] + secret[i+1]
    word += chr(int(char_code) + 23)
print("Word: ", word)
