#!/bin/sh
while true; do
    find . | entr -s "make site"
done
