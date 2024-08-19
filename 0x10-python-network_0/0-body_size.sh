#!/bin/bash
#This sceipt prints the size of body of curl response(bytes).
curl -s -o dev//null -w "%{size_download}\n" $1
