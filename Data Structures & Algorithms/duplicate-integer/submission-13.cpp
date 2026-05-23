class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> track(nums.begin(), nums.end());
        return track.size() != nums.size();
        
    }
};