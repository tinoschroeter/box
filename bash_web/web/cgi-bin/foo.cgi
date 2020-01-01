#!/bin/bash 
echo "X-Bash-On-Steroids: Because there's nothing you can't fix with a #!Bash Script."
echo Content-type: text/html
echo ""
## make POST and GET stings 
## as bash variables available
if [ ! -z $CONTENT_LENGTH ] && [ "$CONTENT_LENGTH" -gt 0 ] && [ $CONTENT_TYPE != "multipart/form-data" ]; then
read -n $CONTENT_LENGTH POST_STRING <&0
eval $(echo "${POST_STRING//;}"|grep '='|tr '&' ';')
fi
eval $(echo "${QUERY_STRING//;}"|grep '='|tr '&' ';')
## decode URL-encoding
urldecode() { : "${*//+/ }"; echo -e "${_//%/\x}"; }

echo "hallo"
echo $REQUEST_URI
#echo $REQUEST_URI|sed 's/\///'|sqlite3 /var/www/html/chinook.db
#echo $url

