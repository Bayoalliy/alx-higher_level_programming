#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.
curl -sL -X PUT 0.0.0.0:5000/catch_me -H "Content-Type: multipart/form-data" -H "Origin: School" -F "user_id=98"
