class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> m;
        int i=0, maxlength=0;        
        
        for (int j=0; j<s.length(); j++){
            
            // if found
            if (m.find(s[j]) != m.end()){
                i = max(m[s[j]], i);
            } 
                            
            maxlength = max( (j - i + 1), maxlength);

            // Store result
            m[s[j]] = j+1;
        }
        
        return maxlength;
    }
};