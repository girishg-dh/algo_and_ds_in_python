from collections import Counter
def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""
    t_counter = Counter(t)
    s_counter = Counter()
    min_len, min_window = len(s) + 1, ""
    left, right = 0, 0
    for right, chr in enumerate(s): # expand window
        s_counter[chr] += 1
        while s_counter >= t_counter: # shrink window
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left: right + 1]
            s_counter[s[left]] -= 1
            if s_counter[s[left]] == 0:
                del s_counter[s[left]]
            left += 1
    return min_window
           