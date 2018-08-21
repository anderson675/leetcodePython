class solution:
    def numOfJewels(self,J,S):
        return sum(s in J for s in S)