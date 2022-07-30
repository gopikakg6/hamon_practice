def panagram(s):
    s=s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    b=sorted(set(s))
    b = "".join(b)
    b = b.strip()
    if alphabet==b:
        print("true")
    else:
        print("false")
panagram("ABCDEFGHIJKLMNOPQRSTUVWXYZ")      
panagram("hello HOW are u")
panagram("abcdefghijklmnopqrstuvwxyz")
panagram("aabbbabcdefghijklmnopqrstuvwxyz")