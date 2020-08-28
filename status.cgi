#!/bin/bash

array=("all" "TheIsland" "CrystalIsles" "TheCenter" "ScorchedEarth_P" "Ragnarok" "Aberration_P" "Extinction" "Valguero_P")

if [[ " ${array[@]} " =~ " $QUERY_STRING " ]]; then
  instance=$QUERY_STRING
else
  instance="all"
fi

echo "Content-type: text/html"
echo ""
echo "<html><head>"
echo "<meta http-equiv='refresh' content='30'>"
echo "<style>body { font-family: calibri }</style>"
echo "<title>ARK Server Status</title>"
echo "</head><body>"
echo "<h1>ARK Server Status - ${instance}</h1><pre>"
readarray -t strarr < <(arkmanager status @${instance} | sed -r "s/\x1B\[([0-9]{1,3}(;[0-9]{1,2})?)?[mGK]//g")

for val in "${strarr[@]}";
do
  beginsWith=$(echo "$val" | cut -c1-21)

  if [[ $beginsWith == "Running command 'stat" ]]; then
    arkInstance=$(echo "$val" | awk '/Running/{{gsub("\047","",$6)}; print $6}')
  fi

  if [[ $beginsWith == " Server running:   No" ]]; then
    echo " Server running:   No <a href='start.cgi?$arkInstance'>Start</a>"
  elif [[ $beginsWith == " Server running:   Ye" ]]; then
    echo " Server running:   Yes <a href='stop.cgi?$arkInstance'>Stop</a>"
  else
    echo "$val"
  fi
done

echo "</pre>"
#echo "<a href='/cgi-bin/theislandstart.cgi'>Start Server</a> <a href='/cgi-bin/theislandstop.cgi'>Stop Server</a>"
echo "</body></html>"
