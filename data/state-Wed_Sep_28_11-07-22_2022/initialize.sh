#!/bin/bash
echo "include the keyword 'hard' to perform OT factory reset and/or noUSB to prevent USB reset"
get_crtime() {
  for target in "${@}"; do
    inode=$(stat -c %i "${target}")
    fs=/dev/mmcblk0p2
    crtime=$(sudo debugfs -R 'stat <'"${inode}"'>' "${fs}" 2>/dev/null | grep -oP 'crtime.*--\s*\K.*')
    printf "%s\t%s\n" "${target}" "${crtime}"
  done
    }
if [[ "$*" == *"noUSB"* ]]
  then
    echo "not resetting USB"
  else
    echo "reset USB"
    /home/pi/reset_USB.sh
fi
if [[ "$*" == *"hard"* ]]
  then
    echo "hard reset"
    sudo ot-ctl  factoryreset #questo manda un segnale di reset
fi

sudo ot-ctl  thread stop
sleep 10
sudo ot-ctl ifconfig down
sleep 10
echo "starting the agent"
sudo service otbr-agent restart
sleep 1
sudo ot-ctl dataset init new
sleep 1
sudo ot-ctl dataset panid 0x1234
sleep 1
sudo ot-ctl dataset extpanid 1111111122222222
sleep 1
sudo ot-ctl dataset channel 14
sleep 1
sudo ot-ctl  dataset networkname OpenThreadDemo
sleep 1
if [ ! -f "/home/pi/MLP" ]
then
	echo "MLP does not exist, creating a new one"
else
	MLP=`cat MLP | grep Mesh | awk '{print $4}'| awk -F  ":" '{print $1":"$2":"$3":"$4"::"}'`
	sudo ot-ctl dataset meshlocalprefix ${MLP}
	echo "we should have loaded ${MLP} and this is what I see " `sudo ot-ctl dataset meshlocalprefix`
fi
if [ ! -f "/home/pi/polled.csv" ]
then
	echo "polled.csv does not exist, creating a new one"
else
	echo "saving old polled"
#	filename=$(mktemp --tmpdir=/home/pi -t polled-XXXX -u)-$(get_crtime /home/pi/polled.csv | cut -f2 -).csv
	filename=polled-$(get_crtime /home/pi/polled.csv | cut -f2 -).csv
	mv /home/pi/polled.csv "${filename// /_}"
fi
#touch /home/pi/polled.csv
#sudo chown pi:pi /home/pi/polled.csv 
if [ ! -f "/home/pi/diagnostics.log" ]
then
        echo "diagnostics.log does not exist, creating a new one"
else
        echo "saving old diagnostics"
#       filename=$(mktemp --tmpdir=/home/pi -t polled-XXXX -u)-$(get_crtime /home/pi/polled.csv | cut -f2 -).csv
        filename=diagnostics-$(get_crtime /home/pi/diagnostics.log | cut -f2 -).log
        mv /home/pi/diagnostics.log "${filename// /_}"
fi
touch /home/pi/diagnostics.log
sudo chown pi:pi /home/pi/diagnostics.log
sleep 1
sudo ot-ctl dataset networkkey 00112233445566778899AABBCCDDEEFF
sleep 1
sudo ot-ctl dataset pskc -p TMPSENS1
sleep 1
sudo ot-ctl dataset commit active
sleep 1
sudo ot-ctl ifconfig up
sleep 1
sudo ot-ctl  thread start
sleep 1
sudo ot-ctl netdata register
sleep 20
if [ ! -f "/home/pi/MLP" ]
then
	sudo ot-ctl dataset meshlocalprefix > /home/pi/MLP
	echo "MLP saved"
fi
echo "becoming leader if we are not yet"
sudo ot-ctl state leader
sleep 10
#sudo ot-ctl parentpriority 1
/home/pi/get_IPs.sh > /home/pi/multicastIP
sudo ot-ctl routerupgradethreshold 1
sudo ot-ctl routerdowngradethreshold 32
sleep 10
sudo ot-ctl ipaddr mleid > /home/pi/myip
echo -e "\n\n---------------------------------------\nBoot completed at $(date --utc)" >>diagnostics.log
