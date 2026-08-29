"""
classic pattern:
expand right until valid -> shrink left while valid -> repeat
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        need = {}
        window = {}

        for c in t:
            need[c] = need.get(c, 0) + 1
        
        have = 0
        need_count = len(need)

        left = 0

        best_length = float("inf")
        best_start = 0
        
        for right in range(len(s)):
            c = s[right]

            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1
            while have == need_count:
                current_length = right - left + 1

                if current_length < best_length:
                    best_length = current_length
                    best_start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                
                left += 1
        if best_length == float("inf"):
            return ""
        
        return s[best_start:best_start + best_length]

