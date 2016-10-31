from collections import Counter
sen1 = "My name is James Bond."
a = dict(Counter(sen1.split()))
print(a)
