#!/usr/bin/env bash
#a Bash script that takes in a URL, sends a request to that URL
echo "$(curl -s -w '%{size download}' -o /dev/null $1)"
