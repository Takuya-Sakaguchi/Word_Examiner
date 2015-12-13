


import matplotlib.pyplot as plt

fo = open("unknown_words.txt", "r")


unknownWords = fo.readlines()



def removeNewLine (inputwords):
    if inputwords[-1:] == "\n":
        return inputwords[:-1]
    else:
        return inputwords

trimmedUnknownWord = []
numbers = []

for item in unknownWords:
    trimmedUnknownWord.append(removeNewLine(item))

for item in trimmedUnknownWord:
    print(item, trimmedUnknownWord.count(item))
    numbers.append(trimmedUnknownWord.count(item))
plt.style.use('ggplot')
plt.hist(numbers, color = 'blue')
plt.show()