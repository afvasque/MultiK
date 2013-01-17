# coding=utf-8

import sys
import usb.core
import usb.util
import wave
import event

# keycode mapping (for a latin american keyboard layout)
key_pages = [
'', '', '', '',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Enter', '^]', '^H',
'^I', ' ', "'", '¡', '`', '+', 'ç', '>', 'ñ', '´', '°', ',', '.',
'-', 'CapsLock', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
'PS', 'SL', 'Pause', 'Ins', 'Home', 'PU', '^D', 'End', 'PD', '->', '<-', '-v', '-^', 'NL',
'KP/', 'KP*', 'KP-', 'KP+', 'KPE', 'KP1', 'KP2', 'KP3', 'KP4', 'KP5', 'KP6', 'KP7', 'KP8',
'KP9', 'KP0', '\\', '<', 'Pow', 'KP=', 'F13', 'F14' ]

key_pages_shift = [
'', '', '', '',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
'!', '"', '·', '$', '%', '&', '/', '(', ')', '=', 'Enter', '^]', '^H',
'^I', ' ', '?', '¿', '^', '*', 'Ç', '<', 'Ñ', '¨', 'ª', ';', ':',
'_', 'CapsLock', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
'PS', 'SL', 'Pause', 'Ins', 'Home', 'PU', '^D', 'End', 'PD', '->', '<-', '-v', '-^', 'NL',
'KP/', 'KP*', 'KP-', 'KP+', 'KPE', 'KP1', 'KP2', 'KP3', 'KP4', 'KP5', 'KP6', 'KP7', 'KP8',
'KP9', 'KP0', '|', '>', 'Pow', 'KP=', 'F13', 'F14' ]

def map_character(c):
    return key_pages[c]

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]






class KeyboardLibrary:
    keyboard_array = []
    keypress = event.Event('A key has been pressed')

    def detect(self,vendor_id, product_id):
        # find our keyboards
        print 'Detecting keyboards with vendor_id = ' + str(vendor_id) + ' and product_id = ' + str(product_id) + '...'
        keyboards = usb.core.find(find_all=True, idVendor=vendor_id, idProduct=product_id)

        print str(len(keyboards)) + ' keyboards of the specified type detected!'

        if len(keyboards) is 0:
            sys.exit("Make sure the keyboards are connected, or check that the vendor_id and product_id variables are correct.")

        for kb in keyboards:
            self.keyboard_array.append(kb)



    def configure(self):
        
        for keyboard in self.keyboard_array:
            
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
                # # ... but we can ignore it and we get no problems.
                # print "Error on setting configuration: " + str(e) + ". Continuing anyway."
                pass

            keyboard._endpoint = keyboard[0][(0,0)][0]

    
    def start(self,vendor_id, product_id):
        # Detect the keyboards
        #(id values found using 'lsusb --vv' command in ubuntu 12.04)
        #self.detect(vendor_id,product_id)  
        #self.configure()

        #Display the keyboard input
        while True:
            for (i,kb) in enumerate(self.keyboard_array):   # i is the index and kb the Keyboard object
                try:
                    data = kb._endpoint.read(kb._endpoint.wMaxPacketSize, 20) # timeout is the last argument

                    # map the input to a character
                    map_keys = lambda c: key_pages_shift[c[1]] if c[0] is 2 else key_pages[c[1]]
                    data2 = "".join(map(map_keys, [(d[0], d[2]) for d in chunks(data, 8)]))

                    # fire the event
                    values = [str(i),data2] # id, char
                    self.keypress(values)
                    #print "#" + str(i) + " : " + data2
                except usb.core.USBError as e:
                    pass
