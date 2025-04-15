# Using Slicing (Fastest & Simplest Method)
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  # Output: "olleh"

# ✅ Time Complexity: O(n) (Python internally creates a new reversed string)
# ✅ Space Complexity: O(n) (A new string is created in memory)