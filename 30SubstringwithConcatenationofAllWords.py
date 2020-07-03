'''
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.



Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s == "" or words == []:
            return []
        k = len(words[0])
        result = []
        for i in range(len(s) - k * len(words) + 1):
            now = words[::]
            if self.findeone(s[i:(k * len(words) + i)], now, k):
                result += [i]
        return result

    def findeone(self, s, words, k):
        """
        :param s:str
        :param words:List[str]
        :param k: int
        """
        if s == '':
            return True
        if s[0:k] in words:
            words.remove(s[0:k])
            return self.findeone(s[k:], words, k)
        else:
            return False


A = Solution()
print(A.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
