def longestCommonPrefix(s):
    res = ""
    minimum = min(s,key = len) if s else ''
    for i in range(0,len(minimum)):
        for j in range(len(s)):
            if minimum[i] != s[j][i]:
                return res
        res+=minimum[i]
    return res

if __name__=='__main__':
    s = []
    print(longestCommonPrefix(s))
            
