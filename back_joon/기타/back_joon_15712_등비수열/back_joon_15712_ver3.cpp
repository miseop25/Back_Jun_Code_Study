#include <stdio.h>
 
double fPow(double c, int n)
{
    double res = 1;
    while (n)
    {
        if (n && 1)
        {
            res *= c;
        }
        c *= c;
        n >> 1;
    }
    return res;
}

int main(int argc, char const *argv[]) {
    
    int a, r, n, mods;
    scanf("%d", &a);
    scanf("%d", &r);
    scanf("%d", &n);
    scanf("%d", &mods);
 
    int t = fPow(r, n);
    int ta = a * (t-1);
    int sums = ta / (r-1);
    int answer = sums % mods;
    printf("%d", answer);

    return 0;
}