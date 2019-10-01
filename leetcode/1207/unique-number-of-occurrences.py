'''
with an array of integers
return true
ONLY if the # of occurences of each value is unique
otherwise return false

input: [1, 2, 2, 1, 1, 3]
output: true
reasoning: '1' occurs 3x, '2' occurs 2x, '3' occurs 1x

brainstorming:
could make a dictionary, if there are equivalent values, return False?
I don't think I should sort the array

'''


def uniqueOccurences(arr) -> bool:
    numdict = dict()

    for i in arr:
        if i in numdict:
            numdict[i] += 1
        else:
            numdict[i] = 1

    countList = []
 
    for count in numdict.values():
        if count not in countList:
            countList.append(count)
        else: 
            return False
    return True



print(uniqueOccurences([1,2]))