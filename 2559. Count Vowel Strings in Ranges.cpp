// https://leetcode.com/problems/count-vowel-strings-in-ranges/
class Solution {
public:
    bool isvowel(char c){
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
public:
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        int n = words.size();
        vector<int> pref(n+1, 0);
        for (int i = 0; i<n; i++){
            if (isvowel(words[i][0]) && isvowel(words[i].back())){
                pref[i+1] = pref[i] + 1;
            }
            else{
                pref[i+1] = pref[i];
            }
        }

        vector<int> ans;
        // Answer each query using the prefix sum array
        for (const auto& query : queries) {
            int l = query[0];
            int r = query[1];
            ans.push_back(pref[r + 1] - pref[l]);
        }
        
        return ans;
    }
};
