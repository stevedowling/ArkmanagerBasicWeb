#!/bin/bash
array=("all" "TheIsland" "CrystalIsles" "TheCenter" "ScorchedEarth_P" "Ragnarok" "Aberration_P" "Extinction" "Valguero_P")

if [[ " ${array[@]} " =~ " $QUERY_STRING " ]]; then
  instance=$QUERY_STRING
else
  instance="all"
fi

echo "Content-type: text/html"
echo ""
echo "<html><head><style>body { font-family: calibri }</style><title>ARK - Start Server"
echo "</title></head><body>"
echo "<h1>ARK Server Starting - ${instance}</h1><pre>"
output=`arkmanager start @${instance} | sed -r "s/\x1B\[([0-9]{1,3}(;[0-9]{1,2})?)?[mGK]//g"`
echo "$output"
echo "</pre>"
echo "<a href='/cgi-bin/status.cgi'>Server Status</a>"
echo "</body></html>"
