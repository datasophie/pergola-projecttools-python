#!/bin/bash

if [ -d "dist" ];
then
  echo "[CICD] Cleaning previous builds"
  rm dist/*
else
  echo "First build, nothing to clean"
fi
 
echo "[CICD] Building"
python3 -m build
 
echo "[CICD] Publishing"
python3 -m twine upload dist/*

#echo "[CICD] Publishing to TEST PyPI"
#python3 -m twine upload --repository testpypi dist/* --verbose

#echo "[CICD] Publishing to locally configured repo"
#python3 -m twine upload -r local dist/* --config-file pypirc.local

echo "[CICD] Done ... Exiting"