#!/bin/bash
freq_diag=`tail -n1 /home/pi/parameters.csv | awk -F "," '{print $6}'`
last_seen_time=`tail -n1 /home/pi/parameters.csv | awk -F "," '{print $2}'`
c=0
while :
do
    for i in $(seq 1 $freq_diag)
    do
	c=$((c+1))
        if [[ $c = $last_seen_time ]]; then
            c=0
            : > /home/pi/toparse.txt
        fi
        freq=`tail -n1 /home/pi/parameters.csv | awk -F "," '{print $3}'`
	sudo ot-ctl networkdiagnostic get `cat /home/pi/multicastIP` 8 16 >> /home/pi/toparse.txt
	python3 /home/pi/parser.py
	sleep $freq
    done
/home/pi/diagnostics.sh
done

