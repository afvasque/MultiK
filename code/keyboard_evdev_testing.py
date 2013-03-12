# coding=utf-8

from asyncore import file_dispatcher, loop
from evdev import InputDevice, categorize, ecodes

class InputDeviceDispatcher(file_dispatcher):
    def __init__(self, device):
        self.device = device
        file_dispatcher.__init__(self, device)
    def recv(self, ign=None):
        return self.device.read()
    def handle_read(self):
        for event in self.recv():
            print(repr(event))

#InputDeviceDispatcher(InputDevice('/dev/input/event22'))
#InputDeviceDispatcher(InputDevice('/dev/input/event23'))
#loop()



#f = open('/proc/bus/input/devices','r')


# count = 0
# print count
# found = False
# for line in f:
# 	if line.find('GASIA') is not -1:
# 		found = True
# 	if line.find('H: Handlers') is not -1 and line.find('event') is not -1 and found is True:
# 		found = False
# 		print line
#         print count
#         count = count + 1

# print "%d" % count

from evdev import InputDevice, list_devices

devices = map(InputDevice, list_devices())

for dev in devices:
    print( '%-20s %-32s %s' % (dev.fn, dev.name, dev.phys) )