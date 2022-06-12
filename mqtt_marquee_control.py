#!/usr/bin/env python
import subprocess
import time

import paho.mqtt.client
import paho.mqtt.client as mqtt

COMMANDS = {
    b"open": b"Q1QQ00QFF0F1QF0F0F0F",
    b"close": b"Q1QQ00QFF0F1QF0F0101",
    b"stop": b"Q1QQ00QFF0F1QF0FFFFF",
}


def on_message(client: paho.mqtt.client.Client, userdata, message: paho.mqtt.client.MQTTMessage):
    if message.payload in COMMANDS:
        subprocess.check_call(["./rfsend/send433", COMMANDS[message.payload]])


def main(host="192.168.1.2", topic="marquee"):
    client = mqtt.Client()
    client.on_message = on_message

    while True:
        try:
            client.connect(host)
        except OSError:
            time.sleep(5)
            continue
        break
    client.subscribe(topic)

    client.loop_forever()


if __name__ == "__main__":
    main()
