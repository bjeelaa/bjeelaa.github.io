#!/bin/bash

python makelist.py
git add .
git commit -m "new pdf files"
git branch -M master
git push -u origin

# If you want to emulate "pause" behavior
read -p "Press Enter to exit"