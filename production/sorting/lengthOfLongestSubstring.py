def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    longest = 0
    longest_substring = ""  # To store the longest substring
    sett = set()
    n = len(s)

    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1

        sett.add(s[r])
        current_length = (r - l) + 1

        # Update longest substring and its length
        if current_length > longest:
            longest = current_length
            longest_substring = s[l:r + 1]  # Slice the substring

    print(f"Longest substring: {longest_substring}, Length: {longest}")
    return longest

# Test the function
input_str = 'abcdecadeded'
lengthOfLongestSubstring(input_str)