class Solution {
   public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n);
        vector<int> pref(n);
        vector<int> suf(n);

        // calculate prefix
        // calculate suffix
        // multiply

        /*
        [1,1,2,6] pref
        [1, 2, 3, 4] nums
        [24,12,4,1] suf
        */
        pref[0] = 1;
        suf[n - 1] = 1;

        for (int i = 1; i < n; i++) {
            pref[i] = pref[i - 1] * nums[i - 1];
        }
        for (int i = n - 2; i >= 0; i--) {
            suf[i] = suf[i + 1] * nums[i + 1];
        }
        for (int i = 0; i < n; i++) {
            result[i] = pref[i] * suf[i];
        }
        return result;
    }
};
