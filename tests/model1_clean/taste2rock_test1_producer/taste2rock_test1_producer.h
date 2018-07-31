/* This file was generated automatically: DO NOT MODIFY IT ! */

/* Declaration of the functions that have to be provided by the user */

#ifndef __USER_CODE_H_taste2rock_test1_producer__
#define __USER_CODE_H_taste2rock_test1_producer__

#include "C_ASN1_Types.h"

#ifdef __cplusplus
extern "C" {
#endif

void taste2rock_test1_producer_startup();

void taste2rock_test1_producer_PI_activator();

extern void taste2rock_test1_producer_RI_sendSporadic(const asn1SccWrappers_Vector3d *);

extern void taste2rock_test1_producer_RI_setProt(const asn1SccT_UInt32 *);

extern void taste2rock_test1_producer_RI_getUnprot(asn1SccT_UInt32 *);

extern void taste2rock_test1_producer_RI_sendEmpty();

#ifdef __cplusplus
}
#endif


#endif
