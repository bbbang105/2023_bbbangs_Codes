word = input()

while(True):
    if len(word) < 10:
        print(word)
        break
    print(word[0:10])
    word = word[10:]
