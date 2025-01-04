#["flower", "flow", "flight"] → "fl"
# "flow".startswith("flo")  # True
# "flow".startswith("flower")  # False

def longest_Common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

print(longest_Common_prefix(["flower", "flow", "floght"]))