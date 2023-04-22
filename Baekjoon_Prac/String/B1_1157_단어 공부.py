word = input().upper()
new_word = list(set(word))
count_lst = []

for i in new_word:
    count_lst.append(word.count(i))
    
if count_lst.count(max(count_lst)) > 1:
    print('?')
else:
    alpha = word[count_lst.index(max(count_lst))]
    print(alpha)

