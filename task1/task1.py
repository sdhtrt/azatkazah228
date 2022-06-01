with open('task1.txt') as file:
    text = file.read()

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
bigAlphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
punctuation = '.!?'

parts = []
lastIndex = 0
for i in range(len(text)):
     if text[i] in punctuation:
         parts.append(text[lastIndex:i+1])
         lastIndex = i+1

for part in parts:
    if '?' in part:
        print()
        for index in range(len(alphabet)):
            print(index, end=' ')
            for char in part:
                if char in alphabet:
                    print(alphabet[(index + alphabet.index(char)) % len(alphabet)], end='')
                elif char in bigAlphabet:
                    print(bigAlphabet[(index + bigAlphabet.index(char)) % len(bigAlphabet)], end='')
                else:
                    print(char, end='')
            print('')



