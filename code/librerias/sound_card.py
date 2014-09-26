# coding=utf-8

import subprocess

class SoundCard:
    hub = None
    name = None

    def __init__(self, card_name):
        self.name = card_name

    def get_root_hub(self):
        if self.hub is None:
            # Get the physical path for the card_name dir
            abs_path_cmd = "readlink -f /proc/asound/%s" % (self.name)
            abs_path = subprocess.check_output(abs_path_cmd, shell=True)
            # Cut the trailing newline char
            abs_path = abs_path[:-1] # This should be something like /proc/asound/card21

            # Get the physical address of the hub where the card is connected
            addr_cmd = "cat %s/stream0 | grep \"USB Headphone\" | cut -d',' -f1 | cut -d'-' -f4" % (abs_path)
            addr = subprocess.check_output(addr_cmd, shell=True)

            # Soundcard hub, -3 to remove \n and soubndcard slot number in hub
            hub_addr = addr[:-3]

            # Save the hub address
            self.hub = hub_addr
        
        return self.hub

    def get_name(self):
        return self.name
