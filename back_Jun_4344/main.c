//
//  main.c
//  back_Jun_4344
//
//  Created by Minseop Kim on 07/08/2019.
//  Copyright © 2019 Minseop Kim. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    double  student_num, score_sum, buf, count;
    int score_array[1000];
    int i,k,N;
    double avg, how_many;
    
    scanf("%d", &N);
    
    for(k =0; k<N ; k++) {
        buf = 0;
        score_sum =0;
        count = 0;
        scanf("%lf", &student_num);
        fflush(stdin);
        
        for (i=0; i< student_num; i++) {
            scanf("%lf", &buf);
            //fflush(stdin);
            score_sum = score_sum + buf;
            score_array[i] = buf;
        }
        avg = score_sum/student_num;
        for (i=0; i< student_num; i++) {
            if (score_array[i] > avg) {
                count++;
            }
        }
        how_many = (count/student_num)*100;
        printf("%.3f%%\n", how_many);
    }
    
    return 0;
}
