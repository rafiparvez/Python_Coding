'''
We have two special characters. The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Now given a string represented by several bits. Return whether the last character must be a one-bit character or not.
The given string will always end with a zero.
'''

def isOneBitCharacter(bits):
    assert len(bits)>0 and bits[-1]==0 , "Input 'bits' must have last integer 0"
    i=0
    while(i < len(bits)-1):
        if bits[i]==0:
            i+=1
        elif bits[i]==1:
            i+=2
    if i==len(bits): return False
    else: return True

bits=[1,0,1,1,1,0]
print(isOneBitCharacter(bits))


'''
Method 2:
The second-last 0 must be the end of a character (or, the beginning of the array if it doesn't exist).
Looking from that position forward, the array bits takes the form [1, 1, ..., 1, 0] where there are zero or more 1's present in total.
It is easy to show that the answer is true if and only if there are an even number of ones present.
'''


def isOneBitCharacter2(bits):
    parity = bits.pop()
    while bits and bits.pop():
        parity ^= 1
    return parity == 0

print(isOneBitCharacter2(bits))