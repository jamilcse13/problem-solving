#include<iostream>
#include<string>
using namespace std;

int main()
{
    int n, i, x=0;
    string arr[150];

    cin>>n;

    for(i=0; i<n; i++)
    {
        cin>>arr[i];
    }

    for(i=0; i<n; i++)
    {
        if(arr[i] == "X++" || arr[i] == "++X")
        {
            x++;
        }
        else if(arr[i] == "X--" || arr[i] == "--X")
        {
            x--;
        }
    }

    cout<<x;
}
