# coding=utf-8

import sys
import usb.core
import usb.util
import pyaudio
import wave

def map_character(c):
    return key_pages[c]

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

class Keyboard:
    keyboard_array = []

    @staticmethod
    def detect(vendor_id, product_id):
        # find our keyboards
        print 'Detecting keyboards with vendor_id = ' + str(vendor_id) + ' and product_id = ' + str(product_id) + '...'
        keyboards = usb.core.find(find_all=True, idVendor=vendor_id, idProduct=product_id)

        print str(len(keyboards)) + ' keyboards of the specified type detected!'

        if len(keyboards) is 0:
            sys.exit("Make sure the keyboards are connected, or check that the vendor_id and product_id variables are correct.")

        for kb in keyboards:
            Keyboard.keyboard_array.append(Keyboard(kb))



    def __init__(self, keyboard):
        # make sure the hiddev kernel driver is not active
        if keyboard.is_kernel_driver_active(0):
            try:
                keyboard.detach_kernel_driver(0)
            except usb.core.USBError as e:
                sys.exit("Could not detach kernel driver: %s" % str(e))

        # set configuration
        try:
            keyboard.set_configuration() # This gives us an error (Errno 16: Resource busy), we don't know why ...
            keyboard.reset()
        except usb.core.USBError as e:
            # ... but we can ignore it and we get no problems.
            print "Error on setting configuration: " + str(e) + ". Continuing anyway."
            pass

        self._endpoint = keyboard[0][(3,0)][0]







class Main:
    def __init__(self):
        # Detect the keyboards
        #(id values found using 'lsusb --vv' command in ubuntu 12.04)
        Keyboard.detect(0x0d8c,0x000e)  
        Keyboard.detect(0x0c76,0x1607) 
        Keyboard.detect(0x1130,0xf211)  
        
if __name__ == "__main__":
    Main()
