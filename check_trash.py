#!/usr/bin/python

import os,sys
import time

time.sleep(1)

print sys.popen('')

R1=`cat /sys/class/net/$n/statistics/rx_bytes`
T1=`cat /sys/class/net/$n/statistics/tx_bytes`
sleep 1
R2=`cat /sys/class/net/$n/statistics/rx_bytes`
T2=`cat /sys/class/net/$n/statistics/tx_bytes`
TBPS=`expr $T2 - $T1`
RBPS=`expr $R2 - $R1`
TMBPS=`expr $TBPS / 1024 / 128`
RMBPS=`expr $RBPS / 1024 / 128`

if [[ $TMBPS -ge $c1 ]] || [[ $RMBPS -ge $c2 ]] ; then
    echo "Critical - current is ${TMBPS}, ${RMBPS}";
    exit 2;
fi
if [[ $TMBPS -ge $w1 ]] || [[ $RMBPS -ge $w2 ]] ; then
    echo "WARNING - current is ${TMBPS}, ${RMBPS}";
    exit 1;
fi
echo "OK - current is ${TMBPS}, ${RMBPS}";
exit 0;
~