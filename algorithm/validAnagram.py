# Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically 
# using all the original letters exactly once.
# Input: s = "anagram", t = "nagaram"
# Output: true
# Input: s = "rat", t = "car"
# Output: false
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_set = {}
        for alpha in s:
            if alpha not in hash_set.keys():
                hash_set[alpha] = 1
            else:
                hash_set[alpha] += 1
        
        for alpha in t:
            if alpha not in hash_set.keys():
                return False
            hash_set[alpha] -= 1
            if hash_set[alpha] == 0:
                del hash_set[alpha]
            
        if len(hash_set) > 0:
            return False
        return True