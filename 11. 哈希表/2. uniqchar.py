def firstUniqChar(s):
    letters = 'abddefghijklmnopqrstuvwxyz'
    index = [s.index(l) for l in letters if s.count(l) == 1]
    return min(index) if len(index) > 0 else -1

s = "givenastring"
print(firstUniqChar(s))