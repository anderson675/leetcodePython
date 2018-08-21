class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        key = [chr(i) for i in range(97,123)]
        value = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dic={}

        output = []

        for i in range(len(key)):
            dic[key[i]] = value[i]

        for i in words:
            cur = ''
            for j in i:
                cur += dic[j]
            output.append(cur)

        return len(set(output))