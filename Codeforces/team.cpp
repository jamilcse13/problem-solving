#include<iostream>
using namespace std;

int main()
{
    int n, x=0, i, j, arr[1000][3];
    cin>>n;

    for(i=0; i<n; i++)
    {
        for(j=0; j<3; j++)
        {
            cin>>arr[i][j];
        }
    }

    for(i=0; i<n; i++)
    {
        int sum = 0;

        for(j=0; j<3; j++)
        {
            sum = sum + arr[i][j];
        }

        if(sum>=2) {
            x++;
        }
    }

    cout<<x;

}
