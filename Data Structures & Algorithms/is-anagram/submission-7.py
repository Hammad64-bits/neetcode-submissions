class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        lookup = dict()
        for char in s:
            if lookup.get(char) == None :
                lookup[char] = 1
            else: 
                lookup[char] += 1
        for char in t:
            if char in lookup:
                if lookup[char] == 0: return False
                lookup[char] -= 1
            else:
                return False
        return True

        
