#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    char str[100];
    int n, i, a=0;

    cin>>str;
    n= strlen(str);

    for (i=0; i<n; i++)
    {
        if (str[0] =! str[i+1]) {
            a++;
        }
    }

    if (a/2==0) {
        cout<<"CHAT WITH HER!";
    }
    else {
        cout<<"IGNORE HIM!";
    }
}

