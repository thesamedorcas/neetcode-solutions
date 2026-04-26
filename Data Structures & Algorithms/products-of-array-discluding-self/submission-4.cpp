class Solution {
   public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n);
        int left = 1;
        int right = 1;

        // calculate prefix
        // calculate suffix
        // multiply

        /*
        [1,1,2,6] pref
        [1, 2, 3, 4] nums
        [24,12,4,1] suf
        */

        for (int i = 0; i < n; i++) {
            result[i] = left;
            left *= nums[i];
        }
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= right;
            right *= nums[i];
        }
        return result;
    }
};
