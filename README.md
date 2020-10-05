# Sunrise Alarm Clock
TODO description




## Setting up the Raspberry pi
### Initialize
Write newest version of Raspbian OS to SD card and power up the raspberry pi. Connect keyboard and screen and run initial updates:

`$ sudo apt-get upgrade && sudo apt-get update`

Enter into textual configuration tool:

`$ sudo raspi-config`

In configuration tool:
- Change default password
- Enable SSH
- Set correct timezone
- Enable and configure WLAN
- Change hostname (optional)


Now you can connect to the raspberrypi via SSH over WLAN for the next steps.

### Mount and use USB drive as filesystem (recommended)
Connect USB drive
```
# Find PARTUUID
$ blkid
# Create mountpoint
$ sudo mkdir /media/usb
# Edit fstab
$ sudo nano /etc/fstab
# Add the following line to the end of the file
PARTUUID=<partuuid from blkid without quotes> /media/usb utf8=1,user,umask=0,uid=1000,gid=1000 0 0
# Test fstab line
$ sudo mount -a
$ ls /media/usb
```

### Install docker and docker-compose
```
$ sudo apt-get install apt-transport-https ca-certificates software-properties-common -y
# Install git, python3 and python3-pip
$ sudo apt-get install -y git python3 python3-pip
$ curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
$ sudo usermod -aG docker pi
$ sudo reboot
# Reconnect and test docker
$ docker container run hello-world

# Install docker-compose
$ sudo pip3 install docker-compose
```

### Clone and build and run this project
Authenticate `git` on your raspberry pi: https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
```
$ cd /media/usb
$ git clone git@github.com:HarmvZ/sunrise-alarm-clock.git
$ cd sunrise-alarm-clock/
$ docker-compose -f docker-compose-production.yml up -d --build
```
Wait for building and bringing up of containers. When this is done you can access the control app at `http://<raspberry-pi-hostname>/`

