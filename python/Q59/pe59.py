# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
#

from collections import Counter

with open('cipher.txt') as f:
	content = f.readlines()

codes = content[0].split(sep=',')
codes.pop()
codes.append('73')
key1 = []
key2 = []
key3 = []

counter = 1
for code in codes:
    if counter%3 == 1:
        key1.append(int(code))
    elif counter%3 == 2:
        key2.append(int(code))
    else:
        key3.append(int(code))
    counter = counter + 1

print('frequency outputs to determine the three characters of key:')
print(Counter(key1))
print(Counter(key2))
print(Counter(key3))

#using character frequency analysis we suggest that most common character is space. Determined keys manually from counter output:
#key1 = 103, key2 = 111, key3 = 100

decrypt1 = [key ^ 103 for key in key1]
decrypt2 = [key ^ 111 for key in key2]
decrypt3 = [key ^ 100 for key in key3]

print('sum of decrypted ascii codes:')
print(sum(decrypt1) + sum(decrypt2) + sum(decrypt3))