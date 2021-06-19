#include<iostream>
#include<string>
using namespace std;

int main()
{
    string str1, str2;

   cin>>str1>>str2;

   for(int i=0; i<str1.size(); i++)
   {
        str1[i] = tolower(str1[i]);
        str2[i] = tolower(str2[i]);
   }

   if(str1==str2)
   {
        cout<<"0";
   }
   else if(str1>str2)
   {
        cout<<"1";
   }
   else if(str1<str2)
   {
        cout<<"-1";
   }


}
