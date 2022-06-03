with open('task1.txt') as file:
    text = file.read()

punctuation = '.!?'
parts = []
lastIndex = 0
for i in range(len(text)):
     if text[i] in punctuation:
         parts.append(text[lastIndex:i+1])
         lastIndex = i+1

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
bigAlphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

with open('keys.txt') as file:
    keys = file.read()
part = 0
keys = keys[keys.find('{')+1:-1].split(', ')

def a(keys):
    global part
    if i == 0:
        for char in parts[part]:
            if char in alphabet:
                print(alphabet[alphabet.index(char) - int(keys[i])], end='')
            elif char in bigAlphabet:
                print(bigAlphabet[bigAlphabet.index(char) - int(keys[i])], end='')
            else:
                print(char, end='')
        part += 1
    while True:
        if part > len(parts):
            break
        if '?' in parts[part]:
            break
        for char in parts[part]:
            if char in alphabet:
                print(alphabet[alphabet.index(char) - int(keys[i])], end='')
            elif char in bigAlphabet:
                print(bigAlphabet[bigAlphabet.index(char) - int(keys[i])], end='')
            else:
                print(char, end='')
        part += 1
    part += 1

for i in range(len(keys)):
    a(keys)

