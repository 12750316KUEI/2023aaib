class Solution {
public:
    string addBinary(string a, string b) {
        int carry=0;
        int i=a.length()-1, j=b.length()-1;
        vector<int> ans;
        while(i>=0 || j>=0)
        {
            if(j<0)
            {
                int now=a[i]-'0'+carry;
                ans.push_back(now%2);
                carry=now/2;
            }
            else if(i<0)
            {
                int now=b[j]-'0'+carry;
                ans.push_back(now%2);
                carry=now/2;
            }
            else
            {
                int now=a[i]-'0'+b[j]-'0'+carry;
                ans.push_back(now%2);
                carry=now/2;
            }
            i--;
            j--;
        }
        if(carry>0) ans.push_back(carry);
        int N=ans.size();
        string ans2(N,'0');
        for(int i=0;i<N;i++)
        {
            ans2[i]=ans[N-1-i]+'0';
        }
        return ans2;
    }
};
