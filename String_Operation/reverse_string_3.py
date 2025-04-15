# Using reversed() and join()

def reverse_string(s):
    return "".join(reversed(s))

print(reverse_string("hello"))  # Output: "olleh"

# ✅ Time Complexity: O(n) (reversed() iterates through n characters, and join() concatenates them)
# ✅ Space Complexity: O(n) (A new string is created in memory)