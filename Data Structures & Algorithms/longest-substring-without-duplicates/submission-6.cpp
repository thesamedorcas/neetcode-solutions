class Solution {
   public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        int left = 0;
        int max_length = 0;
        unordered_set<char> my_set;

        if (n == 0) {
            return max_length;
        }
        if (n == 1) {
            return 1;
        }
        my_set.insert(s[left]);
        max_length = 1;
        for (int right = 1; right < n; right++) {
            while (my_set.contains(s[right])) {
                my_set.erase(s[left]);
                left++;
            }

            my_set.insert(s[right]);

            int sz = my_set.size();
            max_length = max(max_length, sz);
        }

        return max_length;
    }
};
