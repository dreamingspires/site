#!/bin/sh
set -e

cd ./public
python3 -m http.server 9000
