#!/bin/bash

# i know this is a bad practice but idgaf

inst_path="/home/$(whoami)/.local/lib/python3.8/site-packages/patsac"

if [ -e $inst_path ]
then
    rm -r $inst_path
fi

cp -r src $inst_path
