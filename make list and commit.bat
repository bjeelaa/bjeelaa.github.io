@echo off
START /WAIT python makelist.py
git add .
git commit -m "new pdf files"
git branch -M master
git push -u origin main