class Solution {
public:
    int romanToInt(string s) {
        int total = 0;        
        if (s.length() == 0){
            return 0;
        }
        
        if (s.length() == 1){
            if (s[0] == 'M'){total+=1000;}
            if (s[0] == 'D'){total+=500;}
            if (s[0] == 'C'){total+=100;}
            if (s[0] == 'L'){total+=50;}
            if (s[0] == 'X'){total+=10;}
            if (s[0] == 'V'){total+=5;}
            if (s[0] == 'I'){total+=1;}
            
            return total;
        }
        
        for (int x=0; x<s.length(); x++){
            if (s[x] == 'M'){total+=1000;}
            if (s[x] == 'D'){total+=500;}
            if (s[x] == 'C'){
                if ((s.length() > x+1) && s[x+1]=='D'){
                    total += 400;
                    x++;
                }                
                else if ((s.length() > x+1) && s[x+1]=='M'){
                    total += 900;
                    x++;
                } else{
                    total+=100;
                }
                            }
            if (s[x] == 'L'){total+=50;}
            if (s[x] == 'X'){
                if ((s.length() > x+1) && s[x+1]=='L'){
                    total += 40;
                    x++;
                }                
                else if ((s.length() > x+1) && s[x+1]=='C'){
                    total += 90;
                    x++;
                } else{
                    total+=10;
                }
            }
            if (s[x] == 'V'){total+=5;}
            if (s[x] == 'I'){
                if ((s.length() > x+1) && s[x+1]=='V'){
                    total += 4;
                    x++;
                }                
                else if ((s.length() > x+1) && s[x+1]=='X'){
                    total += 9;
                    x++;
                } else{
                    total+=1;
                }
            }
            
        }
        
        
        return total;
    }
};