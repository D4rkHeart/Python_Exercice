def to_weird_case(words):
    string = []
    string = words.lower().split(" ")
    outputlist = []
    for i in range(len(string)):
        countLetter = 0
        if countLetter == 0 and i != 0:
            outputlist.append(" ")
        for l in string[i]:
            for d in string[i][countLetter]:
                # Even number
                if countLetter % 2 == 0:
                    outputlist.append(str(d).upper())
                # Odd number
                else:
                    outputlist.append(str(d))
                countLetter += 1
    return "".join(outputlist)


to_weird_case("this is a test")
