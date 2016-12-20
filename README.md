# essential_magic_mirror
Testing for rasberry-pi magic mirror project I am working on. This may turn into something, or may not. For now, it is
only an experiment and should not be used.

# Prereq

    sudo echo 'deb http://mirrordirector.raspbian.org/raspbian/ testing main contrib non-free rpi' > /etc/apt/sources.list.d/stretch.list
    sudo apt-get update
    sudo apt-get dist-upgrade
    sudo apt-get autoremove


# Download

Clone from git using the following command in the /home/pi directory:

    git clone https://github.com/shane-mason/essential_magic_mirror.git

This will create a directory called 'essential_magic_mirror'

# Install Services

To install, run the following from any directory:

    bash /home/pi/essential_magic_mirror/install_mm.sh

It should start on reboot.



