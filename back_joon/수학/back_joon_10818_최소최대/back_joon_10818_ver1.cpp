#include <iostream>
#include <string>
using namespace std;

int main() 
{
    int N = 0;
    int temp = 0;

    // cin >> N;
    scanf("%d", &N);
    int minNum, maxNum = 0;
    for(int i=0; i<N; i++)
    {
        // cin >> temp;
        scanf("%d", &temp);
        if(i == 0)
        {
            minNum = temp;
            maxNum = temp;
            continue;
        }

        if(minNum > temp) 
            minNum = temp;
        
        if(maxNum < temp) 
            maxNum = temp;
    }
    

    // cout << minNum << " " << maxNum << "\n";
    printf("%d %d",minNum, maxNum);

    return 0;
};