#include<iostream>

using namespace std;
int main()
{
    char str[50];
    int n, i, a=0;

    cin>>n;
    for(i=0; i<n; i++)
    {
        cin>>str[i];
    }

    for (i=0; i<n; i++)
    {
        if (str[i] == str[i+1]) {
            a++;
        }
    }

    cout<<a;
}
