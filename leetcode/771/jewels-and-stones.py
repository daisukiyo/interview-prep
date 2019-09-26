'''
given two strings
J = stones that are jewels
S = stones you have

J will not contain duplicates
Assume all characters in J and S are letters
Assume letterrs are case sensitive a != A

logic:
1. init count at 0
2. iterate through each letter
3. increment count at every occurance

this seems rather inefficient
why iterate through the entire string for every character in J

maybe i could use a dictionary?

1. create a dictionary (key:value = character: count)
2. if the key is in the dictionary, summate the count?

'''

def numJewelsInStones(J: str, S: str) -> int:

    counts = dict()
    jewels = 0

    for stone in S:
        if stone in counts:
            counts[stone] += 1
        else:
            counts[stone] = 1
    
    for jewel in J:
        if jewel in counts:
            jewels += counts[jewel]
    
def numJewelsInStones2(J: str, S: str) -> int:
    jewelSet = set(J)
    jewels = 0

    for stone in S:
        if stone in jewelSet:
            jewels += 1
            
    return jewels
