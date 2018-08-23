import collections
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        c = collections.Counter()
        for str in cpdomains:
            index, content = str.split()
            c[content] += int(index)
            for i in range(len(content)):
                if content[i] =='.':
                    c[content[i+1:]] += int(index)
        return["%d %s" % (c[k],k)for k in c]
