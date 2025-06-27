import json
from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        return json.dumps(strs)

    def decode(self, s: str) -> List[str]:
        return json.loads(s)

# 🧪 Test
codec = Codec()
original = ["hello", "world"]
encoded = codec.encode(original)
print("Encoded:", encoded)
decoded = codec.decode(encoded)
print("Decoded:", decoded)
