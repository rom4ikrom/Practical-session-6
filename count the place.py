print("This program count the world place in your sentence.")
user_input = input("Please write a sentence: ")
a = user_input.split()
count = 0
while count < len(a):
    print(a[count], "\t", count)
    count = count + 1
b = len(a) + 1
dictionary = dict(zip(a, range(0, b)))
print(dictionary)

