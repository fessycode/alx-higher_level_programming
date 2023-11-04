#!/bin/bash
# Displays only the status code of http request
curl -s -w '%{http_code}' "$1" -o /dev/null
