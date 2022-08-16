#!/bin/bash
#var=$(grep -r "TddConfigCommon.PatternType" confChange.txt)
#echo $var
#echo $var | awk '{print $3}'

variable=`grep -r "TddConfigCommon.PatternType" confChange.txt | awk '{printf $3}'`
echo $variable
