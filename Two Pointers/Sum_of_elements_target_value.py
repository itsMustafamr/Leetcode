def two_sum_brute_force(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return i, j # or True
    return None # or False

arr = list(map(int,input("Enter your preferred array and the target string ").split()))
target = int(input("enter your target value"))
#result = two_sum_brute_force(arr, target)
#print(f"indices: {result}")  - same output
print(two_sum_brute_force(arr, target))

