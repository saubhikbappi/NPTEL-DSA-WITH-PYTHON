#Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is,
#every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols that appear in s.
#Your function should return True if s has matched brackets and False if it does not.

def matched(s):
    j = 0
    for c in s:
        if c == ')':
            j -= 1
            if j < 0:
                return False
        elif c == '(':
            j += 1
    return j == 0
s="(7)(a"
print(matched(s))