def reverse_elements(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements
words = ["apple","mango","orange","grapes","banana"]
print(reverse_elements(words))
