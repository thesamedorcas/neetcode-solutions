class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> dic;

        for (int i=0; i< nums.size(); i++){
            int diff= target- nums[i];
            if (dic.contains(diff)){
                return {dic[diff], i};
            }

            dic[nums[i]]= i;

        }
    }
};
