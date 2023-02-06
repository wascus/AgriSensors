MLP=`cat MLP | grep Mesh | awk '{print $4}'| awk -F  ":" '{print $1":"$2":"$3":"$4}'`
multicast=ff33:40:${MLP}:0:1
echo $multicast
