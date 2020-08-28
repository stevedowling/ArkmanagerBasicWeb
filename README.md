# ArkmanagerBasicWeb
cgi-bin bash scripts to start and stop Ark game instances via ArkManager (https://github.com/arkmanager/ark-server-tools). 

These scripts should be installed in the cgi-bin folder of a webserver on the same server as ArkManager. Has only been tested with lighttpd.

## status.cgi
Shows the installed instances and their status and gives the option to start and stop each instance

## start.cgi
Called from status.cgi to start an instance

## stop.cgi
Called from status.cgi to stop an instance
