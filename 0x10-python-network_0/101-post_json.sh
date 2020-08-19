#!/bin/bash
# sends a JSON POST request to a URL
curl -s --request POST "$1" -H "Content-type: application/json" --data @"$2"
