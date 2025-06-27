from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        return ''.join(s.replace('\\', '\\\\').replace('#', '\\#') + '#' for s in strs)

    def decode(self, s: str) -> List[str]:
        res, curr = [], ''
        escape = False
        for c in s:
            if escape:
                curr += c
                escape = False
            elif c == '\\':
                escape = True
            elif c == '#':
                res.append(curr)
                curr = ''
            else:
                curr += c
        return res

# 🧪 Test
codec = Codec()
original = ["he#llo", "wo\\rld"]
encoded = codec.encode(original)
print("Encoded:", encoded)
decoded = codec.decode(encoded)
print("Decoded:", decoded)
