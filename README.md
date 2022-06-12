# Homeautomation Marquee Control

Controling a Sunfun marquee using a 433MHz sending module on a Raspberry Pi.

## Features

- Listen to MQTT topic
- Execute specific command for 433MHz sender

## Resources

- Code in `rfsend` is a copy of https://github.com/hackenbergstefan/homeautomation-raspirollo which is a fork of https://github.com/bjwelker/Raspi-Rollo

## Wiring

- 433MHz sender is connected to GPIO2 (SDA)
- Codes for Sunfun marquee were sniffed using:
  - http://physudo.blogspot.com/2013/08/home-automation-mit-dem-arduino-und-433_17.html
  - http://physudo.blogspot.com/2013/08/home-automation-mit-dem-arduino-und-433_18.html
  - https://github.com/bjwelker/Raspi-Rollo/
  Code for sniffing: `Rollo_Code_Receiver.ino`
