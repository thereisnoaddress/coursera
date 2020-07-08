def lengthOfLongestSubstring(s):
    maxLength = 0
    sub = ''

    for char in s: 
        if char in sub: 
            sub = sub[sub.find(char) + 1:]
        sub += char
        if len(sub) > maxLength: 
            maxLength = len(sub)
    return maxLength

if __name__ == "__main__":
    x = lengthOfLongestSubstring('dvdf')