#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI -X OPTIONS -i $1 | grep 'Allow' | cut -d " " -f 2-
