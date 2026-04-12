class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        int n= nums.size();
        unordered_map<int, int> count;
        vector<vector<int>> freq(n+1);

        for (int i: nums){
            count[i]++;
        }
  
        for (auto& [key, val] : count){
            freq[val].push_back(key);

        }

        vector<int> result;
        for (int i=n; i>0; i--){
            if (!freq[i].empty()) {
                for (int j: freq[i]){
                    if (result.size()==k){
                        return result;
                    }else{
                        result.push_back(j);
                    }
                }
            }
        
        }
    return result;
    }
};
