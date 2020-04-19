"""
Leetcode question 925
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
 

Note:

name.length <= 1000
typed.length <= 1000
The characters of name and typed are lowercase letters.

"""


def isLongPressedName(name: str, typed: str) -> bool:
        pointer1 = 0
        pointer2 = 0
        stack = []

        while (pointer1 < len(name) and pointer2 < len(typed)):
            if name[pointer1] == typed[pointer2]: 
                stack.append(name[pointer1])
                pointer1 += 1
                pointer2 += 1
            else: 
                if stack == []: 
                    return False
                elif typed[pointer2] == stack[-1]:
                    pointer2 += 1
                else: 
                    pointer1 += 1
                    pointer2 += 1
        

        return ''.join(stack) == name
        
        

if __name__ == "__main__":
    flag = isLongPressedName("leelee", "lleeele")
    print(flag)
