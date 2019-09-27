'''
given a list of words (list of strings)
find the # of transformations ()

convert the words into morse code
    - array of strings, map them
    - create full morse by iterating each char of the word (for loop)
        - convert letter to matching morse value
    - 

    [a, a, a, a, a, b, c, c, d, d]
    a, b, c, d

'''

def uniqueMorseRepresentations(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    result = set()

    for word in words:
        val = ""
        for letter in word:
            val += morse[ord(letter)-ord('a')]
        
        result.add(val)
    return len(result)

wordlist = ["gin", "zen", "gig", "msg"]

print(uniqueMorseRepresentations(wordlist))