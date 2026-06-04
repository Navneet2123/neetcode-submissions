class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        number_of_char = {}
        
        if len(s) != len(t):
            return False
        
        for char1, char2 in zip(s, t):
            number_of_char[char1] = number_of_char.get(char1, 0) + 1
            number_of_char[char2] = number_of_char.get(char2, 0) - 1
        
        for value in number_of_char.values():
            if value != 0:
                return False
        
        return True