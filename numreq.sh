#!/bin/bash
#### this script let you organize all the ip in an access.log, by number of requests
#### ---log analysis script ---
#### usage: numreq.sh access.log
cat $1 | cut -d " " -f 1 | sort | uniq -c | sort -unr