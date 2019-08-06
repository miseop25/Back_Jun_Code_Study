//
//  main.c
//  back_Jun_10818
//
//  Created by Minseop Kim on 06/08/2019.
//  Copyright © 2019 Minseop Kim. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    unsigned long N,i;
    long min_num, max_num,buf;
    min_num =0;
    max_num =0;
    buf =0;
    scanf("%ld",&N);
    
    for(i=0 ; i<N; i++){
        scanf("%ld",&buf);
        if (i ==0) {
            min_num = buf;
            max_num = buf;
        }else{
            if (min_num > buf) {
                min_num = buf;
            }
            if (max_num < buf) {
                max_num = buf;
            }
        }
    }
    printf("%ld %ld", min_num, max_num);
    return 0;
}
