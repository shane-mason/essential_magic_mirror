#!/bin/bash

BASEDIR=$(dirname "$0")
cd $BASEDIR/../essential_mm
/usr/bin/python3 mm_aioserver.py


