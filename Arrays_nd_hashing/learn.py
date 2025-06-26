macha = set()
macha.add(1)
macha.add(2)
macha.add(3)
macha.add(4)
macha.add(5)
macha.add(6)
macha.add(7)
macha.add(8)
macha.add(9)
macha.add(10)
print(macha)

macha.clear()
print(macha)

macha.update([11, 12, 13, 14, 15])
print(macha)

macha.remove(11)
print(macha)

macha.discard(12)
print(macha)

macha.pop()
print(macha)

macha.contains(13)
print(macha)

macha.contains(14)
print(macha)

macha.contains(15)
print(macha)

macha.contains(16)