#include<iostream>
using namespace std;

int main()
{
    int n;
    cin>>n;
    string output = (n<=2 || n%2 != 0) ? "NO" : "YES";
    cout<<output<<endl;
}

