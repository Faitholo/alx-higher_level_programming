#!/bin/bash
# Script sends POST to URL
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
