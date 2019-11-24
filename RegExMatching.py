def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def reduce(pattern):
            index = 0
            output = ''
            while index+1 < len(pattern):
                if pattern[index+1]!='*':
                    output+=pattern[index]
                    index +=1
                else:
                    index += 2
            if index==len(pattern)-1:
                output+=pattern[index]
            return output
        if len(s)==0 and reduce(p)=='':
            return True
        def dp(i,j):
            #print(reduce(p))
            if j+1>len(p) or i+1>len(s):
                memo[(i,j)] = False
            if not (i,j) in memo:
                firstMatch = p[j] in {s[i],'.'}
                if i+1==len(s):
                    reduced = reduce(p[j:])
                    if len(reduced)==0 and (s[i] in p[j:] or '.' in p[j:]):
                        ans = True
                    elif len(reduced)==1 and reduced in {s[i],'.'}:
                        ans = True
                    else:
                        ans = False
                elif j+1==len(p):
                    ans = firstMatch and (i+1==len(s))
                elif j+1<len(p) and p[j+1]=='*':
                    ans = (firstMatch and dp(i+1,j)) or dp(i,j+2)
                else:
                    ans = firstMatch and dp(i+1,j+1)
                memo[(i,j)] = ans
            return memo[(i,j)]
        return dp(0,0)