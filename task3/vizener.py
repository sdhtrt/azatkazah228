text = input()
key = 'thekey'
alphabet = "qwertyuiopasdfghjklzxcvbnm_{}1234567890"
answer = ''

for i in range(len(text)):
    textNumber = alphabet.index(text[i])
    keyNumber = alphabet.index(key[i%len(key)])
    answer += alphabet[(textNumber + keyNumber + 1) % len(alphabet)]
print(answer)