#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
content=$(<$2); curl -sX POST $content $1
