class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        visited = [False] * n
        result = []

        for i in range(n):
            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True

            for j in range(i + 1, n):
                if not visited[j]:
                # check anagram using sorting
                    if sorted(strs[i]) == sorted(strs[j]):
                        group.append(strs[j])
                        visited[j] = True

            result.append(group)

        return result
        