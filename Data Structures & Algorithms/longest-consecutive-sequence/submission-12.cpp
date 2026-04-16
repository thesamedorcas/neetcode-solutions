class Solution {
   public:
    int longestConsecutive(vector<int>& nums) {
        /*
        (1, 2, 3, 4)
        [1, 2, 3, 4]

        for i in nums:
        check if i ++ in this, increment

        */
        int result = 0;
        unordered_set<int> my_set(nums.begin(), nums.end());
        for (const auto& i : my_set) {
            int curr_max = 1;
            int curr_num = i;

            while (my_set.contains(curr_num + 1)) {
                curr_max++;
                curr_num++;
            }
            result = max(result, curr_max);
        }
        return result;
    }
};
