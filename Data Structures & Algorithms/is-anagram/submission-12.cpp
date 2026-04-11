#include <bits/stdc++.h> 
using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> sdic;
        unordered_map<char, int> tdic;

        for (char i : s){
            sdic[i]++;
        }
        for (char i : t){
            tdic[i]++;
        }

        return sdic==tdic;

        
    }
};
