all = input()
word = input()

while(word in all):
    all = all.replace(word, '*')
    
cnt = all.count('*')
print(cnt)