class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        fir = 'qwertyuiopQWERTYUIOP'
        sec = 'asdfghjklASDFGHJKL'
        tth = 'zxcvbnmZXCVBNM'
        list = [fir,sec,tth]
        result = []
        def sameRow(word,row):
            n = 0
            for ch in word:
                if ch not in row:
                    break
                n += 1
            if n == len(word):
                result.append(word)
        
        for word in words:
            if word[0] in fir:
                sameRow(word,fir)
            elif word[0] in sec:
                sameRow(word,sec)
            elif word[0] in tth:
                sameRow(word,tth)
            else:
                pass
            return result