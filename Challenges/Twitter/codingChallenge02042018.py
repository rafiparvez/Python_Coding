#University 2018 - Test 7

###Question 2

def maxLength(a, k):
    maxlen = 0
    arr = []
    sum_arr = 0
    for elt in a:
        arr.append(elt)
        sum_arr += elt
        if sum_arr <= k:
            maxlen = max(maxlen, len(arr))
        else:
            sum_arr -= arr[0]
            del arr[0]

        return maxlen

###Question 3


def decrypt(encrypted_message, keystring):
    keylen = len(keystring)

    result = ""
    i = 0
    for char in encrypted_message:
        if i == keylen: i = 0

        key = keystring[i]
        # Upper case char
        if ord(char) in range(65, 91):
            firstalphabet = 'A'
        # lower case char
        elif ord(char) in range(97, 123):
            firstalphabet = 'a'
            # not an alphabet
        else:
            firstalphabet = None

        # if character is an alphabet
        if (firstalphabet):
            new_char = chr(ord(char) - int(key))
            if new_char < firstalphabet:
                new_char = chr(ord(new_char) + 26)
            i += 1
        else:
            new_char = char
        result += new_char
    return result

message = 'Atvt hrqgse, Cnikg'
key = "2208251"

#keystring = "8251220"
print(decrypt(message, key))