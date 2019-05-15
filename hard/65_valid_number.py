# https://leetcode.com/problems/valid-number/

"""
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
"""


"""
start with e - False
end with e - False
start with . - True
end with . - False

start with single - False

sign after the e - True

more than two e's - False
more than two signs - False
dot after e - False
e after dot - True

space middle - False

"""

class Solution:

    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        signs = ['+', '-']

        found_e = False
        found_dot = False

        l = len(s)

        for i, c in enumerate(s):
            if c == ' ':
                return False
            if c == 'e':
                # we cannot have only one e
                if i == 0:
                    return False
                if i == l-1:
                    return False
                # if already found e - False
                if found_e:
                    return False
                # if found dot, it cannot be first number
                if found_dot and s[0] == '.':
                    return False

                # e cannot be the last digit
                if i == l - 1:
                    return False

                found_e = True
                continue

            if c in signs:
                # we cannot only one sign
                if i == 0 and l == 1:
                    return False

                if i != 0 and not found_e:
                    return False

                # consequitive signs are not allowed
                if s[i-1] in signs:
                    return False

                continue

            if c == '.':
                if i == 0 and l == 1:
                    return False

                if found_dot or found_e: return False;

                found_dot = True
                continue

            try:
                int(c)
            except ValueError:
                return False

        return True

if __name__ == "__main__":
    s = Solution()
    test_cases = [
        ("-1.", True),
        (".1e", False),
        ("", False),
        ("0", True),
        (" 0.1 " , True),
        ("abc", False),
        ("1 a", False),
        ("2e10", True),
        (" -90e3   ", True),
        (" 1e", False),
        ("e3", False),
        (" 6e-1", True),
        (" 99e2.5 ", False),
        ("53.5e93", True),
        (" --6 " ,False),
        ("-+3", False),
        ("95a54e53" ,False),
        ("e", False),
        (".", False),
        ("++", False),
        ("+", False),
        ( "..", False),
        (".e1", False),
        ("e2", False),
        ("1.e2", True),
        (".1", True)
    ]
    for t in test_cases:
        print(t)
        assert s.isNumber(t[0]) == t[1]
