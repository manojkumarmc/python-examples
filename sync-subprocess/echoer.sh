#!/bin/sh

a=0

while [ $a -lt 5 ]
do
   echo 'Long running: ' $a
   a=`expr $a + 1`
   sleep 1
done

{ sleep 5; echo waking up after 5 seconds; } &
{ sleep 1; echo waking up after 1 second; } &

wait
echo all jobs are done!

exit 0
