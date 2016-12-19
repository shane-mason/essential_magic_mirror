# essential_magic_mirror
Testing for rasberry-pi magic mirror project I am working on. This may turn into something, or may not. For now, it is
only an experiment and should not be used.

#Install Dependencies

Flask

    sudo pip3 install flask

EssentialDB

    sudo pip3 install essentialdb

# Set To Autostart:

Set the service to start


    sudo cp essential_magic_mirror/pi/essential_mm.service /lib/systemd/system/


Start the browser in kiosk mode

    essential_magic_mirror/pi/autoChromium.desktop  ~/.config/autostart/

