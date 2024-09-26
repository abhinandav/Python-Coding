s="hellollheh"

def pali(s):
    i=0
    n=len(s)
    longest=''
    while i<n:
        j=i+1
        while j<n:
            substring=s[j:n]
            if substring==substring[::-1] and len(substring)>len(longest):
                longest=substring
            n-=1
        n=len(s)
        i+=1
    return longest

print(pali(s))