with open('task1.txt') as file:
    text = file.read()

with open('words.txt') as file:
    words = file.read().split()

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
        for index in range(len(alphabet)):
            sentence = ''
            for char in part:
                if char in alphabet:
                    sentence += alphabet[(alphabet.index(char) - index) % len(alphabet)]
                elif char in bigAlphabet:
                    sentence += bigAlphabet[(bigAlphabet.index(char) - index) % len(bigAlphabet)]
                else:
                    sentence += char
            counter = 0
            for word in sentence.split():
                if word.lower() in words:
                    print(index, sentence[1:])
                    break



