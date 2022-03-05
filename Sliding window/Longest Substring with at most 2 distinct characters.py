def lengthOfLongestSubstringTwoDistinct(s):
    visited = {}
    l = 0
    max_len = 0

    for r in range(len(s)):
        visited[s[r]] = r

        if len(visited) > 2:
            left_idx = min(visited.values())
            visited.pop(s[left_idx])
            l = left_idx + 1
        max_len = max(max_len, r - l + 1)
    return max_len


if __name__ == "__main__":
    print(lengthOfLongestSubstringTwoDistinct("Yoaoonah"))