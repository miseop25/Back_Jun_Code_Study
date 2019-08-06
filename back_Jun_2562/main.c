//
//  main.c
//  back_Jun_2562
//
//  Created by Minseop Kim on 06/08/2019.
//  Copyright © 2019 Minseop Kim. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int i,count,max_num, buf;
    count =0;
    max_num = 0;
    for (i=0; i<9; i++) {
        scanf("%d",&buf);
        if (max_num < buf) {
            max_num = buf;
            count = i+1;
        }
    }
    printf("%d\n%d", max_num,count);

    return 0;
}
