//
//  main.c
//  back_joon_2839
//
//  Created by Minseop Kim on 13/08/2019.
//  Copyright © 2019 Minseop Kim. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int N, count;
    count = 0;
    scanf("%d", &N);
    
    while (N>0) {
        if (N>=5) {
            if (N%5 == 0) {
                count = count + N/5;
                
                break;
            }else{
                N = N-3; count++;
            }
        }else {N= N-3; count++;}
    }
    if(N <3 && N != 0) count = -1;
    printf("%d", count);
    return 0;
}
