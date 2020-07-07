
  
1.)Step1, Install Raspbian official mirror <br>
====================================================
  a)Download Raspbian official mirror:<br>
  https://www.raspberrypi.org/downloads/<br>
  b)Use“SDFormatter.exe”to Format your TF Card<br>
  c)Use“Win32DiskImager.exe” Burning mirror to TF Card<br>

2.) Upgrade and Update your RPi and install git<br>
====================================================

```sudo apt update && sudo apt full-upgrade -y```<br>
```sudo apt-get install git -y```<br>

3.) Step2, Clone my repo onto your pi<br>
====================================================
Use SSH to connect the Raspberry Pi, <br>
And Ensure that the Raspberry Pi is connected to the Internet before executing the following commands:
-----------------------------------------------------------------------------------------------------

```git clone https://github.com/Juankcba/master-gui.git```<br>
```chmod -R 755 master-gui```<br>
```cd master-gui/LCD-drivers/``<br>
  
4.)Step3, According to your LCD's type, excute the corresponding driver:
====================================================

# 3.5” RPi Display(MPI3501):
### Driver install:
``` sudo ./LCD35-showsudo ./LCD35-show ```<br>

### WIKI:
CN: http://www.lcdwiki.com/zh/3.5inch_RPi_Display  <br>
EN: http://www.lcdwiki.com/3.5inch_RPi_Display
 

### for rotate, If the driver is already installed, execute the following command:

``` cd master-gui/LCD-drivers/```<br>
``` sudo ./rotate.sh 180 ```<br>

After execution, the system will automatically restart, and the display screen will rotate 90 degrees to display and touch normally.<br>
( ' 90 ' can be changed to 0, 90, 180 and 270, respectively representing rotation angles of 0 degrees, 90 degrees, 180 degrees, 270 degrees)<br>
(If the rotate.sh prompt cannot be found, use Method 1 to install the latest drivers)

5.) Installing X & Enabling the touchscreen via X
====================================================

``` sudo apt install lightdm  ```        <br>
``` sudo apt install raspberrypi-ui-mods  ```<br>
``` sudo reboot now```<br>

6.) Install VNC 
====================================================

``` sudo apt-get install realvnc-vnc-server ``` <br>
 ``` sudo raspi-config ``` <br>

active vnc option in Interfacing Options reboot then log with the vnc viewer

6.) Install Tinker && test 
====================================================

``` sudo apt-get install python-tk ``` <br>
``` sudo apt-get install python-tk ``` <br>

on vnc in the terminal put 

``` sudo python lcd.py ``` <br>

now add to boot

sudo nano /etc/xdg/lxsession/LXDE-pi/autostart

@/usr/bin/python /home/pi/master-gui/lcd.py

# master-gui
