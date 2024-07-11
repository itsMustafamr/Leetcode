def Palindrome(word):
    L = 0
    R = len(word) - 1
    while L < R:
        print(f"Comparing {word[L]} and {word[R]}")  # Debug print
        if word[L] != word[R]:
            return False
        L = L + 1
        R = R - 1 
    return True

word = input("enter your word :").strip().lower()
print(Palindrome(word))

