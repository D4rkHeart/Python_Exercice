word = 'abba' 
words = ['aabb', 'abcd', 'bbaa', 'dada']

# Search for anagrams in a list
def anagrams(word, words):
    anagramList = []
    for c in words:
        if anagram(word,c):
            anagramList.append(c)
        
    print(anagramList)

def anagram(word1, word2):
    compared = {} 
    for c in word1:
        if c in compared:
            compared[c] += 1
        else:
            compared[c] = 1
    for c in word2:

        if c in compared:
            compared[c] -= 1
        else:
            return False
    for c in compared:
        if compared[c] != 0:
            return False
    return True