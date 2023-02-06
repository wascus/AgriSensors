#!/bin/bash
multicastIP=`cat /home/pi/multicastIP`
#freq=`tail -n1 /home/pi/parameters.csv | awk -F "," '{print $6}'`
echo "--------------------------------------" >> /home/pi/diagnostics.log
date --utc >> /home/pi/diagnostics.log
sudo ot-ctl networkdiagnostic get $multicastIP 0 1 2 3 4 5 6 7 8 9 16 >> /home/pi/diagnostics.log
echo -e "\nRouter Table:" >> /home/pi/diagnostics.log
sudo ot-ctl router table >> /home/pi/diagnostics.log
echo "Neighbor Table:" >> /home/pi/diagnostics.log
sudo ot-ctl neighbor table >> /home/pi/diagnostics.log
echo -e "\nPoll log (CAREFUL, timezone is $(date +'%Z')):" >> /home/pi/diagnostics.log
sudo service poll status >> /home/pi/diagnostics.log
echo -e "\nPing log(CAREFUL, timezone is $(date +'%Z')):" >> /home/pi/diagnostics.log
sudo service pingnodes status >> /home/pi/diagnostics.log
echo -e "\nTo poll file (might not be 100% in sync):" >> /home/pi/diagnostics.log
cat /home/pi/to_poll.csv >> /home/pi/diagnostics.log
echo -e "\n\n\n\n" >> /home/pi/diagnostics.log
