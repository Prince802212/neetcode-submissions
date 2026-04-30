class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

    # Step 1: Clean the string
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

    # Step 2: Reverse the string
        reversed_str = cleaned[::-1]

    # Step 3: Compare
        return cleaned == reversed_str