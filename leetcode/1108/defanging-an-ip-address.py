"""
convert an ip address into a defanged version
input:  address = "1.1.1.1"
output: "1[.]1[.]1[.]1"

logic:
1. replace the periods with "[.]"
2. return the defanged ip as a string

"""

def defangIPaddr(self, address: str) -> str:
    return address.replace('.', '[.]')
    
    # if built-in function is not allowed

    # defang = ''
    # for i in address:
    #     if i == '.':
    #         i = '[.]'
    #     defang += i
    # return defang