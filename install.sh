#!/bin/bash

# i know this is a bad practice but idgaf

inst_path="/home/$(whoami)/.local/lib/python3.8/site-packages/patsac"

if [ ! -e $inst_path ]
then
    mkdir $inst_path
fi

rm -r $inst_path/*
cp -r src/* $inst_path
