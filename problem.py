def palindrome(s):
    return s==str(s[ ::-1])

string=palindrome(s)
if string:
    return True
else:
    return False





def panagram(s):
    s=s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    b=sorted(set(s))
    b = "".join(b)
    b = b.strip()
    if alphabet==b:
        return True
    else:
        return False
panagram("ABCDEFGHIJKLMNOPQRSTUVWXYZ")      
panagram("hello HOW are u")
panagram("abcdefghijklmnopqrstuvwxyz")
panagram("aabbbabcdefghijklmnopqrstuvwxyz")







def prime(n):
    if n < 2:
        return False
    for numbers in range(2,n):
        if n % numbers == 0:
            return False
    return True







def freq(s):
    dict={}
    for i in s:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    return dict
freq("happy")