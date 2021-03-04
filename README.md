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

### Install mopidy and plugins
1. Follow installation instructions at https://docs.mopidy.com/en/latest/installation/debian/ and https://docs.mopidy.com/en/latest/installation/raspberrypi/
2. Run as a servce: https://docs.mopidy.com/en/latest/running/service/
3. Install and configure plugins such as Spotify, Iris (web ui client), local: https://github.com/jaedb/Iris/wiki/Getting-started#installing
4. Change cache_dir to USB device to prevent SD card corruption
5. Chango config file in `/etc/mopidy/mopidy.conf` to:
```
[core]
cache_dir = /media/usb/cache/mopidy

[logging]
verbosity = 0

[audio]
output = alsasink

[http]
enabled = true
hostname = ::
port = 6680
allowed_origins = raspberrypi,localhost:8088
csrf_protection = true

[file]
enabled = true
media_dirs = XXXXXXXXXXXXXXXXXXXXX

[spotify]
username = XXXXXXXXXXXXXXXXXXXXX
password = XXXXXXXXXXXXXXXXXXXXX
client_id = XXXXXXXXXXXXXXXXXXXXX
client_secret = XXXXXXXXXXXXXXXXXXXXX

[iris]
enabled = true
country = NL
locale = nl_NL
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

### TODO
- MPD hostname and port to env - 1
- Update quasar, etc in UI - 1
- Update readme: mopidy.conf - 1
- Add upcoming songs component - 4
- Add quick actions: on (white), off, volume, - 1
- Make alarm check duration and not sleep when behind - 1 test?
- Fix MPD connection status thing -> mpd ws events to eventbus- 1





cd /home/docker/code/app

from led_core import LedCore
lc = LedCore()
lc.strip_action('start_alarm', duration=1, colors=[[0,0,0],[50,0,0]], playlist="spotify:playlist:3cRIUlmZUfJajVEzcoVSSa", volumes=[])


### Troubleshooting

#### If building api container throws signature error
See https://askubuntu.com/a/1264921 method 2 for a fix