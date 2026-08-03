class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded;

        for (const string& str : strs) {
            encoded += to_string(str.length());
            encoded += '#';
            encoded += str;
        }

        return encoded;
    }

    vector<string> decode(string encoded) {
        vector<string> result;

        int i = 0;

        while (i < encoded.length()) {
            int delim = i;

            while (encoded[delim] != '#') {
                delim++;
            }

            int length = stoi(encoded.substr(i, delim - i));

            int stringStart = delim + 1;

            result.push_back(encoded.substr(stringStart, length));

            i = stringStart + length;
        }
        return result;
    }
};
