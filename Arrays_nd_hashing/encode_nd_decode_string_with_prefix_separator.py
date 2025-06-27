from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            j += 1  # skip '#'
            res.append(s[j:j+length])
            i = j + length
        return res

# 🧪 Test
codec = Codec()
original = ["hello", "world"]
encoded = codec.encode(original)
print("Encoded:", encoded)
decoded = codec.decode(encoded)
print("Decoded:", decoded)
