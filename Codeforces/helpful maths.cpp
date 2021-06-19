#include<iostream>
#include<cstring>
using namespace std;

int main()
{
    int l,i,j, temp;
    char str[100];

    cin>>str;
    l = strlen(str);

    for(i=0;i<l;i+=2)
    {
        for(j=0;j<l-i-2;j+=2)
        {
            if(str[j]>str[j+2]) {
                temp = str[j];
                str[j] = str[j+2];
                str[j+2] = temp;
            }
        }
    }
    cout<<str;
}
