"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:

    Input: s = "rat", t = "car"
    Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = [0] * 26
        for char in s:
            a[ord(char) - ord('a')] += 1
        for char in t:
            alphabet_index = ord(char) - ord('a')
            a[alphabet_index] -= 1
            if a[alphabet_index] < 0:
                return False
        return True


if __name__ == "__main__":
    str1 = 'abcd'
    str2 = 'adbc'
    str3 = 'a'
    s = Solution()
    print("Input: str1, str2, Output: ", s.isAnagram(str1, str2))
    print("Input: str1, str3, Output: ", s.isAnagram(str1, str3))
