class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer={}
        for string in strs:
            sorted_text = "".join(sorted(string))
            if sorted_text in answer:
                answer[sorted_text].append(string)
            else:
                answer[sorted_text]=[string]
        return list(answer.values())