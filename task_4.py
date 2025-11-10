marks = [',', '.', '!', '?', ':', ';', '[', ']',
         '(', ')', '-', '"', '...', '(", ")']

sentence = input("Enter sentence: ")

for mark in marks:
    sentence = sentence.replace(mark, '')

words = sentence.split()
unique_words = set()

for word in words:
   unique_words.add(word)

print(unique_words)
