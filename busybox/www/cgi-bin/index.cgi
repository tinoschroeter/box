#!/bin/sh
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

echo  "<!DOCTYPE html>"
echo  "<html>"
echo  "  <head>"
echo  "    <meta charset=\"utf-8\">"
echo  "    <title>Star Trek vs Star Wars!</title>"
echo  "    <meta name = \"viewport\" content = \"width=device-width, initial-scale = 1.0\">"
echo  "    <meta name=\"author\" content=\"Tino Schroeter\">"
echo  "    <link rel=\"stylesheet\" href=\"static/css/style.css\" />"
echo  "    <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css\">"
echo  " </head>"
    
   if [[ "$vote" = "a" ]];then
     c=$(cat /tmp/a)
     a=$(( $c +1 ))
     echo $a > /tmp/a
   elif [[ "$vote" = "b" ]];then 
     c=$(cat /tmp/b)
     b=$(( $c +1 ))
     echo $b > /tmp/b
   fi
   
echo  "  <body>"
echo  "    <div id=\"content-container\">"
echo  "      <div id=\"content-container-center\">"
echo  "        <h3>Star Trek vs Star Wars!</h3>"
echo  "        <p>"
uptime | sed 's/average//g' 
echo  "</p>"
echo  "        <form id=\"choice\" name='form' method=\"POST\" action=\"/\">"
echo  "          <button id=\"a\" type=\"submit\" name=\"vote\" class=\"a\" value=\"a\">Star Trek</button>"
echo  "          <button id=\"b\" type=\"submit\" name=\"vote\" class=\"b\" value=\"b\">Star Wars</button>"
echo  "        </form>"
echo  "        <div id=\"tip\">"
         
         trek=$(cat /tmp/a) || trek=0
           echo "Star Trek $trek votes<br>"
         wars=$(cat /tmp/b) || wars=0
           echo "Star Wars $wars votes<br>"
         
echo  "        </div>"
echo  "       </div>"
echo  "      </div>"
echo  "    </div>"
echo  "  </body>"
echo  "</html>"
