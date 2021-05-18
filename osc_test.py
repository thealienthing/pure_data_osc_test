from pythonosc.udp_client import SimpleUDPClient
from time import sleep

ip = "127.0.0.1"
port = 9998

print("Sending OSC messages...")

client = SimpleUDPClient(ip, port)

count = 0
while True:
    client.send_message("/some/address", count)
    count += 1
    if count >= 1000:
        count = 0
    sleep(0.01)
