def palIndrome(s):
    if len(s) == 0:
        return True
    if s[0] != s[-1]:
        return False
    return palIndrome(s[1:-1])

print (palIndrome('kuda'))
print (palIndrome('gohangasalamiimalasagnahog'))