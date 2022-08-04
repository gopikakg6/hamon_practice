def palindrome(s):
    return s==str(s[ ::-1])




from string import ascii_lowercase
def panagram(s):
    for letter in ascii_lowercase:
        if letter not in s.lower():
            return False
    return True





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


if __name__ == '__main__':
    print(panagram("gopika"))
    print(palindrome("python"))
    print(prime(3))
    print(freq("happy"))