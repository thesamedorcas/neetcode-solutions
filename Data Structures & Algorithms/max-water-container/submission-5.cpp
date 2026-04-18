class Solution {
   public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;
        int max_area = 0;

        while (left < right) {
            int width = right - left;
            int height = min(heights[right], heights[left]);

            int area = width * height;

            if (area > max_area) {
                max_area = area;
            }
            if (left < right && heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        return max_area;
    }
};
