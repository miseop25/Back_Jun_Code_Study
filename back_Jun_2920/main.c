//
//  main.c
//  back_Jun_2920
//
//  Created by Minseop Kim on 06/08/2019.
//  Copyright © 2019 Minseop Kim. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int i , buf, case_num;
    int num_save = 0;
    case_num = 0;
    for (i=0; i<8; i++) {
        scanf("%d", &buf);
        if (num_save > buf) {
            case_num--;
        }else if(num_save < buf){
            case_num++;
        }
        num_save = buf;
    }
    if (case_num == 8) {
        printf("ascending");
    }else if (case_num == -6){
        printf("descending");
    }else printf("mixed");
    return 0;
}
