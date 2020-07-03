'''
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
'''

'''
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while True:
            if s[0] == ' ':
                s = s[1:]
                if len(s) == 0:
                    return False
            else:
                break
        while True:
            if s[len(s) - 1] == ' ':
                s = s[0:(len(s) - 1)]
            else:
                break
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        if len(s) == 1:
            if s in num:
                return True
            else:
                return False
        else:
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            if s[0] == '.':
                s = s[1:]
                if len(s) == 0:
                    return False
            elif s[-1] == '.':
                s = s[0:(len(s)-1)]
                if len(s) == 0:
                    return False
            if 'e' in s:
                s = s.split('e')
                if len(s) != 2 or len(s[0]) == 0 or len(s[1]) == 0:
                    return False
                s0, s1 = s[0], s[1]
                if len(s0) == 0:
                    return False
                else:
                    if '.' in s0:
                        s0 = s0.split('.')
                        if len(s0) != 2 or len(s0[0]) == 0 or len(s0[1]) == 0:
                            return False
                        else:
                            s0 = s0[0] + s0[1]
                    for i in s0:
                        if i not in num:
                            return False
                    if s1[0] == '-':
                        if len(s1) == 1:
                            return False
                        else:
                            s1 = s1[1:]
                    for j in s1:
                        if j not in num:
                            return False
            else:
                if '.' in s:
                    s = s.split('.')
                    if len(s) != 2 or len(s[0]) == 0 or len(s[1]) == 0:
                        return False
                    else:
                        s = s[0] + s[1]
                for i in s:
                    if i not in num:
                        return False
        return True
'''


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            x = float(s)
            return True
        except ValueError:
            return False


A = Solution()
print(A.isNumber('53.5e93'))
