echo "argument is filename of ips separated by newline"
while IFS= read -r line; do echo $line; ./coap.sh $line; echo "---"; done < $1
