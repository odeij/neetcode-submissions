class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequency;

        for (int number : nums) {
            frequency[number]++;
        }

        vector<vector<int>> buckets(nums.size() + 1);

        for (const auto& entry : frequency) {
            int number = entry.first;
            int count = entry.second;

            buckets[count].push_back(number);
        }

        vector<int> result;

        for (int count = nums.size(); count >= 1; count--) {
            for (int number : buckets[count]) {
                result.push_back(number);

                if (result.size() == k) {
                    return result;
                }
            }
        }

        return result;
    }
};
