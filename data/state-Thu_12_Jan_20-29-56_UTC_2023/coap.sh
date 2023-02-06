myip=`cat myip | head -n1 | awk -F ":" '{print $1":"$2":"$3":"$4":"$5":"$6":"$7":"$8}'`
myip=${myip::-1}
#echo $myip asd

#echo "coap-client -a $myip -m get -B 5 coap://[$1]/sensors/EUI"
coap-client -a $myip -m get -B 5 coap://[$1]/sensors/EUI
