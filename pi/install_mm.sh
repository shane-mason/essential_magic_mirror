#!/bin/bash

BASEDIR=$(dirname "$0")
sudo cp $BASEDIR/essential_mm.service /lib/systemd/system/
cp $BASEDIR/autoChromium.desktop  ~/.config/autostart/
sudo systemctl enable essential_mm
