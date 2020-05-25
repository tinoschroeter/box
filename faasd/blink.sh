#!/bin/bash

function getData() { sudo wc -l /var/log/nginx/access.log|awk '{print $1}'; }
old=$(getData)
while :;do
  new=$(getData)
  echo $(( $new - $old ))
  old=$new
  sleep 2
done
