import sys
input = sys.stdin.read
from collections import Counter

sen = input()
sen = sorted(sen)
check = Counter(sen)
print(check)