/* User code: This file will not be overwritten by TASTE. */

#include "taste2rock_test1_consumer.h"
#include <stdio.h>

asn1SccT_UInt32 count = 0;

void taste2rock_test1_consumer_startup()
{
}

void taste2rock_test1_consumer_PI_sendSporadic(const asn1SccWrappers_Vector3d *IN_val)
{
    printf("[consumer] got vector (%f, %f, %f)\n", IN_val->data.arr[0], IN_val->data.arr[1], IN_val->data.arr[2]);
}

void taste2rock_test1_consumer_PI_setProt(const asn1SccT_UInt32 *IN_val)
{
    printf("[consumer] got count %lld\n", *IN_val);
    count = *IN_val;
}

void taste2rock_test1_consumer_PI_getUnprot(asn1SccT_UInt32 *OUT_val)
{
    printf("[consumer] queried count %lld\n", count);
    *OUT_val = count;
}

void taste2rock_test1_consumer_PI_sendEmpty()
{
    printf("[consumer] got empty message\n");
}

