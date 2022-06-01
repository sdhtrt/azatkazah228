text = input()
numbers = [int(i) for i in text[text.find('{')+1:-1].split('|')]
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for i in numbers:
    print(alphabet[i-1], end='')