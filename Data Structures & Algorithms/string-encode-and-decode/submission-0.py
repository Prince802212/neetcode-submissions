class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeString = ""
        for word in strs:
            encodeString += str(len(word)) + "#" + word
        return encodeString

    def decode(self, s: str) -> List[str]:
        decodedList = []
        currentIndex = 0
        while currentIndex < len(s):
            delimiterIndex = currentIndex
            while s[delimiterIndex] != '#':
                delimiterIndex += 1
            wordLength = int(s[currentIndex:delimiterIndex])
            currentIndex = delimiterIndex + 1
            wordEndIndex = currentIndex + wordLength
            decodedList.append(s[currentIndex:wordEndIndex])
            currentIndex = wordEndIndex

        return decodedList
