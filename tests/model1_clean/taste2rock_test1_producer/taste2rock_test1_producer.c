/* User code: This file will not be overwritten by TASTE. */

#include "taste2rock_test1_producer.h"
#include <stdio.h>

void taste2rock_test1_producer_startup()
{
}

void taste2rock_test1_producer_PI_activator()
{
    static int count = 0;
    asn1SccT_UInt32 countMsg;
    asn1SccWrappers_Vector3d vectorMsg;
    vectorMsg.data.nCount = 3;
    vectorMsg.data.arr[0] = 0.0;
    vectorMsg.data.arr[1] = 0.0;
    vectorMsg.data.arr[2] = 0.0;
    
    if (count % 2)
    {
        vectorMsg.data.arr[0] += count;
        vectorMsg.data.arr[1] += count;
        vectorMsg.data.arr[2] += count;
        printf("[producer] send vector (%f, %f, %f)\n", vectorMsg.data.arr[0], vectorMsg.data.arr[1], vectorMsg.data.arr[2]);
        taste2rock_test1_producer_RI_sendSporadic(&vectorMsg);

        taste2rock_test1_producer_RI_getUnprot(&countMsg);
        printf("[producer] read count %lld\n", countMsg);
    }
    else
    {
        printf("[producer] send empty\n");
        taste2rock_test1_producer_RI_sendEmpty();
        printf("[producer] set count %d\n", count);
        countMsg = count;
        taste2rock_test1_producer_RI_setProt(&countMsg);
    }
    
    count++;
}

