from collections import Counter
print("Please answer the following questions.")

# Here user enter two short sentences
sen_1 = input("Where are you now? ")
sen_2 = input("What are you doing? ")
print ("\n", sen_1 + sen_2)

# Program splits two sentences into two lists and prints out each 
list_1 = sen_1.split()
list_2 = sen_2.split()
print("Sentence 1 as a list: \t\t\t ", list_1)
print("Sentence 2 as a list: \t\t\t ", list_2)
list_3 = list_1 + list_2
print("Both sentences as a list: \t\t ", list_3)

# Program prints lists's words in alphabetical order
print("\nSentence 1 in alphabetical order: \t ", sorted(list_1))
print("Sentence 2 in alphabetical order: \t ", sorted(list_2))
print("2 Sentences in alphabetical order: \t ", sorted(list_3))

# Program prints lists's lenth
print("\nNumber of words in sentence 1: \t\t ", len(list_1))
print("Number of words in sentence 2: \t\t ", len(list_2))
print("Number of words in 2 sentences: \t ", len(list_3))

# A new dictionary, which has sentences's words as keys and their frequencies as values
dictionary = dict(Counter(list_3))
print("\nDictionary, which has sentences's words as keys and their frequencies as values: \n", dictionary)
  
count = 0

# A new dictionary, which has sentence's 1 words as keys and their position in sentence as values
while count < len(list_1):
    count = count + 1
a = len(list_1) + 1 
dictionary_1 = dict(zip(list_1, range(0, a)))
print("\nDictionary, which has sentence's 1 words as keys and their position in sentence as values: \n",dictionary_1)
    
# A new dictionary, which has sentence's 2 words as keys and their position in sentence as values    
while count < len(list_2):
    count = count + 1
b = len(list_2) + 1
dictionary_2 = dict(zip(list_2, range(0, b)))
print("\nDictionary, which has sentence's 2 words as keys and their position in sentence as values: \n",dictionary_2)
