#include <iostream>
#include <string>
using namespace std;

int main() 
{
    int N = 0;
    float scoreSum = 0.0;
    float answer = 0.0;
    scanf("%d", &N);
    float temp = 0;
    float arr[1001];

    float maxNum = 0;
    for(int i=0; i<N; i++)
    {
        scanf("%f", &temp);
        arr[i] = temp;
        if(temp > maxNum)
            maxNum = temp;
    }

    for(int i=0; i<N; i++)
    {
        temp = (arr[i] / maxNum)*100;
        scoreSum += temp;
    }

    answer = scoreSum / N;
    
    printf("%f", answer);

    return 0;
};