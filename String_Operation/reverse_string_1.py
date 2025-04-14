#  Using a Loop (Manual Method)

def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

print(reverse_string("hello"))  # Output: "olleh"

# ❌ Time Complexity: O(n²) (String concatenation creates a new string each time, making it slow)
# ❌ Space Complexity: O(n) (A new string is created, but inefficiently)