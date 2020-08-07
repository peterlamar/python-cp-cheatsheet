class Solution {
public:
    int myAtoi(string str) {
        long result=0;  
        int multiplier=1;
        
        if (str.length() == 0) return 0;
        
        int x = str.find_first_not_of(" ");

        if (x == -1) return 0;
        
        if (str[x] == '-' || str[x] == '+'){
            multiplier = ((str[x]=='-') ? -1 : 1);  
            x++;
        }
 
        
        for (int y=x; y<str.length(); y++){

            if (str[y] >= '0' and str[y] <= '9'){
                result = result*10 + (str[y] - '0') * multiplier;
                
                if (result > INT_MAX) result = INT_MAX;
                if (result < INT_MIN) result = INT_MIN;

            } else {
                break;
            }
            
            
        }
                
        return result;
    }
};