"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.

Constraints:
    0 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.
"""


class Solution:
    # This approach has O(S) time complexity and O(S) space complexity. Since at worst scenario,
    # It compares all the strings with the newly created converted string array.
    def longestCommonPrefix(self, strs: list[str]) -> str:
        columns = [''.join(column) for column in tuple(zip(*strs))]
        result = ""
        if not columns:
            return result
        for column in columns:
            if not column == column[0] * len(strs):
                return result
            else:
                result += column[0]
        return result

    # Leetcode approach 1: horizontal scanning, with O(S) time complexity and O(1) space complexity.
    def longestCommonPrefix_v1(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix

    # Approach 2: Vertical scanning
    def longestCommonPrefix_v2(self, strs: list[str]) -> str:
        if not strs:
            return ""
        for i in len(strs[0]):
            letter = strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) < i + 1 or strs[j][i] != letter:
                    return strs[0][:i]
        return strs[0]


if __name__ == "__main__":
    strs = ['ab', 'abc', 'abcd', 'c']
    s = Solution()
    print(s.longestCommonPrefix(strs))
