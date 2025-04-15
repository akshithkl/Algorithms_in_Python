#  Optimized Recursion (Using List & Join)

def reverse_string(s, rev=[]):
    if not s:
        return "".join(rev)
    rev.append(s[-1])
    return reverse_string(s[:-1], rev)
print(reverse_string("hello")) 

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)