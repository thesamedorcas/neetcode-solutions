class Solution {
   public:
    int maxProfit(vector<int>& prices) {
        int min_price = prices[0];
        int max_diff = 0;
        int n = prices.size();

        for (int i = 1; i < n; i++) {
            int curr_diff = prices[i] - min_price;
            max_diff = max(max_diff, curr_diff);
            min_price = min(min_price, prices[i]);
        }
        return max_diff;
    }
};
