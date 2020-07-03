'''
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        length_sum = -1
        num = 0
        result = []
        while True:
            if num == len(words):
                if num != 0:
                    result += self.fullJustify_one_alter(words[0:num], maxWidth)
                return result
            elif length_sum + len(words[num]) + 1 > maxWidth:
                result += self.fullJustify_one(words[0:num], maxWidth, num, length_sum - num + 1)
                words = words[num: len(words)]
                num = 0
                length_sum = -1
            else:
                length_sum += len(words[num]) + 1
                num += 1

    def fullJustify_one_alter(self, words, maxWidth):
        result = ' '.join(words)
        return [result + ' ' * (maxWidth - len(result))]

    def fullJustify_one(self, words, maxWidth, num, length_sum):
        if num == 1:
            return [words[0] + ' ' * (maxWidth - length_sum)]
        space_num = maxWidth - length_sum
        s = ''
        avg = space_num // (num - 1)
        more_num = space_num % (num - 1)
        for i in range(more_num):
            s = s + words[i] + ' ' * (avg + 1)
        for i in range(more_num, len(words) - 1):
            s = s + words[i] + ' ' * avg
        return [s + words[-1]]


A = Solution()
text = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(A.fullJustify(text, maxWidth))
print(A.fullJustify_one(["This", "is", "an"], maxWidth, 3, 8))
