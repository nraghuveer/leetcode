# Longest common substring for given two strings

# Dynamic programming ..

# If( input1[i] == input2[j] ):
# 	T[i][j] = T[i-1][j-1] + 1
# Else:
# 	T[i][j] = 0


def longest_common_substring(s1: str, s2: str):
    T = [[0 for i in range(len(s2)+1)] for j  in range(len(s1)+1) ]
    result = 0
    # now iterate over the strings.
    for i in range(len(s1)):
        for j in range(len(s2)):
            if i == 0 or j == 0:
                T[i][j] = 0
            elif s1[i] == s2[j]:
                T[i][j] = T[i-1][j-1] + 1
                result = max(result, T[i][j])
            else:
                T[i][j] = 0
    return result


if __name__ == "__main__":
    X = 'OldSite:GeeksforGeeks.org'
    Y = 'NewSite:GeeksQuiz.com'
    print(longest_common_substring(X,Y))