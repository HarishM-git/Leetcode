class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        from collections import Counter
        # ap = 0
        # cou = 0
        # mpp = Counter(words)
        # for w, freq in mpp.items():
        #     s = w[::-1]
        #     if w == s:
        #         cou += (freq // 2) * 4
        #         if freq % 2:
        #             ap = 1
        #     elif w < s and s in mpp:
        #         cou += min(freq, mpp[s]) * 4
        # return (cou + (ap * 2))

        from collections import Counter
        cnt=Counter(words)
        res=0
        center=False
        for w in list(cnt.keys()):
        	rev=w[::-1]
        	if w==rev:
        		res+=(cnt[w]//2)*2
        		if cnt[w]%2:
        			center=True
        	elif w<rev:
        		res+=2*min(cnt[w],cnt[rev])
        return (res+(1 if center else 0))*2
