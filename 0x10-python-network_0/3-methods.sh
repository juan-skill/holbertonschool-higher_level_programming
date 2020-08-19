#!/bin/bash
# displays all HTTP methods the server will accept.
curl -sI "$1" | grep "Allow" | cut --complement -d " " -f 1
