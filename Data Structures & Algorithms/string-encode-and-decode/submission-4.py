class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([f'{len(s)}#{s}' for s in strs])

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # Find the '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract length
            length = int(s[i:j])
            
            # Extract string of that length
            string = s[j+1:j+1+length]
            result.append(string)
            
            # Move pointer past this string
            i = j + 1 + length
        
        return result
