#!/bin/bash
# Script of the response
curl -s -o /dev/null -w "%{size_download}\n" "$1"
