marks = [',', '.', '!', '?', ':', ';', '[', ']',
         '(', ')', '-', '"', '...', '(", ")']

sentence = input("Enter sentence: ")

for mark in marks:
    sentence = sentence.replace(mark, '')

words = sentence.split()
print(words)
