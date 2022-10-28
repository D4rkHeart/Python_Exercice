def to_weird_case(string):
    listWord = list(string.split(' '))
    outputList = []
    for word in listWord:
        listChar = []
        for i in range(len(word)):
            if (i%2==0):
                listChar.append(word[i].upper())
            else:
                listChar.append(word[i].lower())
        outputList.append(''.join(listChar))
    return ' '.join(outputList)