#!/bin/bash

BASEDIR=$(dirname "$0")

sudo pip3 install aiohttp
sudo pip3 install aiohttp_jinja2
sudo pip3 install essentialdb

sudo cp $BASEDIR/essential_mm.service /lib/systemd/system/
sudo cp $BASEDIR/autostart /etc/xdg/lxsession/LXDE-pi/autostart
cp $BASEDIR/autoChromium.desktop  ~/.config/autostart/
sudo systemctl enable essential_mm
