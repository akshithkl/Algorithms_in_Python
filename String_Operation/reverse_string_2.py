# Using Recursion

def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  # Output: "olleh"





# ❌ Time Complexity: O(n²) (String slicing s[:-1] creates a new string in each call)
# ❌ Space Complexity: O(n) (Recursive stack depth is n)