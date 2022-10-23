#include <iostream>
using namespace std;

int main() 
{
    int maxNum = -1;
    int i,temp, index = 0;
    for(i=0; i < 9; i++)
    {
        cin >> temp;
        if (temp > maxNum)
        {
            maxNum = temp;
            index = i + 1;
        }
    }
    cout << maxNum << "\n";
    cout << index << "\n";


    return 0;
};