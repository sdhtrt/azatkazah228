text = input()
key = 'thekey'
alphabet = "qwertyuiopasdfghjklzxcvbnm_{}1234567890"
answer = ''
print(alphabet.index(text[0]), alphabet.index(key[0]))
for i in range(len(text)):
    answer += alphabet[(alphabet.index(text[i]) ^ alphabet.index(key[i%len(key)])) % len(alphabet)]
print(answer)