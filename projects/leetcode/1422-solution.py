def maxScore(s: str) -> int:
    # 0 on the left += 1
    # 1 on the right += 1
    m = 0
    s = list(s)
    for i in range(1, len(s)):
        # left: s[0:i] | right: s[i:]
        m = max(s[0:i].count("0") + s[i:].count('1'), m)
    return m

print(maxScore("011101"))

