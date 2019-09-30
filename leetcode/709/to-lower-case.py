'''
return the given string in lowercase

logic:
i'm guessing you shouldn't just use the .lower() string method
convert to unicode integer
if within the range of uppercase, 
add 32 to make it lowercase 
'''

def toLowerCase(str: str) -> str:
    lowercase = ''
    for char in str:
        # ord returns an integer representing unicode
        if ord(char) >= 65 and ord(char) <= 90:
            # chr returns a character from unicode
            lowercase += chr(ord(char)+32)
        else:
            lowercase += char
    
    return lowercase