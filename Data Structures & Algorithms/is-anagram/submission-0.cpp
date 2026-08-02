class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;

        int frequency[26] = {0};

        for (int i = 0; i < s.length(); i++) {
            frequency[s[i] - 'a']++;
            frequency[t[i] - 'a']--;
        }

        for (int count : frequency) {
            if (count != 0)
                return false;
        }
        return true;
    }
};
