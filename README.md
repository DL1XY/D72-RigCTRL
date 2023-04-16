# D72-RigCTRL

Program to control the Kenwood TH-D72 dual-band transceiver on PC or Android phone via USB-OTG. 
Also provides basic satellite prediction functionality based on user's location.

## Connect a PC to TH-D72 
This should work similar on Windows. Make sure the radio's USB-UART bridge is detected by Windows and change the serial device in the terminal configuration.

### How to connect TH-D72 in serial mode 
* Make sure you have firmware v1.10 installed
* Connect TH-D72 via USB cable to your PC
* Turn TH-D72 on, make sure you are not in TNC mode
* Run `lsusb`, you should see `Silicon Labs CP210x UART Bridge` somewhere
* Check if you find `/dev/ttyUSB0` or `/dev/ttyUSB1`, this should be your TH-D72
* Start `putty` or any other terminal tool which can do serial communication.
* Use this configuration:
  * Connection type: `Serial`
  * Serial line: `/dev/ttyUSB0`
  * Speed: `9600`
  * Data bits: `8`
  * Stop bits: `1`
  * Parity: `None`
  * Flow control: `None`
* Start the session

That"s all, now you can send the commands described here. If you type in `FO 1` and press Enter, you should see the VFO configuration of Band B like `FO 1,0430000000,7,0,0,0,0,0,0,08,08,000,0,01600000,0`.

#### Important
* TH-D72 sends a questionmark `?` if it doesn't know the command you sent
* There is **no** new line after sending/receiving a command

### How to connect TH-D72 in TNC mode 
* Follow the steps in **How to connect TH-D72 in serial mode**
* Press `TNC` key several times until you see something like the following text in the terminal window.
```
bbRAM loaded with defaults



Kenwood Radio Modem
AX.25 Level 2 Version 2.0
Release 16/Nov/2010 2Chip Version 1.00
Checksum $7772
cmd:DA 230307131728
cmd:MY NOCALL
MYCALL   was NOCALL
cmd:
```
* Now you are in TNC mode and you can execute the commands described in the manual.

#### Important
* TH-D72 sends a questionmark followed by EH `?EH` in TNC mode if it doesn't know the command you sent
* TH-D72 is ready for TNC commands if `cmd:` appears in terminal

## Requirements
+ Python 3.x
+ Android SDK (>= API v20)
+ gcc
+ several Phython libraries (see requirements.txt)
+ several other libs to compile via Buildozer

## ToDo
+ UI & Polarview 
+ Serial connection handling (change /dev/tty0 to generic)
+ Android USB connection
+ TNC command handling
+ ...



