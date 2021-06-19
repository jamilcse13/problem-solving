#include<iostream>
using namespace std;

int main()
{
    int n,k,i, p=0, arr[50];

    cin>>n>>k;

    if(n>=k)
    {
        for(i=0; i<n; i++)
        {
            cin>>arr[i];
        }

        for(i=0; i<n; i++)
        {
            if(arr[i] >= arr[k-1] && arr[i]>0)
            {
                p++;
            }
        }

        cout<<p;
    }
}
