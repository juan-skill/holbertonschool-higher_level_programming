#!/bin/bash
# sends a POST request to the passed URL
curl -s --request POST "$1" --data "email=hr@holbertonschool.com&subject=I will always be here for PLD"
