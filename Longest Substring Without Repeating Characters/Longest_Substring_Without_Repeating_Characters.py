class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if(s==""):
            return 0
        final=1
        initial=2
        for k in range(initial, len(s)+1):
            if k<=len(s):
                if self.window(s,k)==self.window(s,k+1):
                    break
                else:
                    final=self.window(s,k)
            else:
                final=self.window(s ,k)
        return final
    def window(self,word, k):
        temp=""
        maximum=0
        for i in range (0, len(word)-k+1):
            temp=word[i:i+k]
            if(self.noduplicate(temp)==True):
                maximum=len(temp)
                break
        return maximum

    def noduplicate(self,lists):
        check=False
        for i in range(0,len(lists)-1):
            for j in range (i+1,len(lists)):
                if(lists[i]==lists[j]):
                    check=False
                    break
                else:
                    check=True
            if check==False:
                break
        return check