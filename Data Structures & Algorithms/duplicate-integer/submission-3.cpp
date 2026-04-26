class Solution {
private:
    std::map<int, int> dict;
public:
    bool hasDuplicate(vector<int>& nums) {
        int arraySize = nums.size();
        for(int a = 0; a < arraySize; a++){
            if(dict[nums[a]] == 0){
                dict[nums[a]] = 1;
            } else {
                dict[nums[a]] += 1;
            }
        }
        
        for (const auto& pair : dict) {
        // If any value is not 0, return false immediately
        if (pair.second > 1) {
            return true;
        }}

        return false;
    }
    
};