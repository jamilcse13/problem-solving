#include<iostream>
using namespace std;

int main()
{
    int k, n, w, i, p=0, ans;

    cin>>k>>n>>w;

    for (i=1; i<=w; i++)
    {
        p = p + k*i;
    }

    if (p>n)
    {
        ans = p-n;
        cout<<ans;
    }
    else {
        cout<<0;
    }


}
