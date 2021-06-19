#include<iostream>
using namespace std;

int main()
{
    int num[5][5], i, j, a, b, ans;

    for(i=0; i<5; i++)
    {
        for(j=0; j<5; j++)
        {
            cin>>num[i][j];
        }
    }

    for(i=0; i<5; i++)
    {
        for(j=0; j<5; j++)
        {
            if(num[i][j] == 1)
            {
                a = i+1;
                b = j+1;
                break;
            }
        }
    }

    ans = abs(3-a) + abs(3-b);
    cout<<ans;
}
