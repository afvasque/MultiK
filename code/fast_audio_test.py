import usb.core
import usb.util
import os
import subprocess

card_array = []
card_word_id_dictionary = {}

cards1 = usb.core.find(find_all = True, idVendor=0x0d8c)
cards2 = usb.core.find(find_all = True, idVendor=0x0c76)
cards3 = usb.core.find(find_all = True, idVendor=0x1130)

# Join the arrays into a single one
card_array = cards1 + cards2 + cards3

for t in card_array:
	# Convert, for example, 2 into 002, 34 into 034, etc.
	usb_bus = '{s:{c}>{n}}'.format(s=t.bus,n=3,c='0')
	usb_address = '{s:{c}>{n}}'.format(s=t.address,n=3,c='0')

	# Find the card with the corresponding bus and address
	command = "grep \"%s/%s\" /proc/asound/card*/*" % (usb_bus, usb_address)
	usbbus = subprocess.check_output(command, shell=True)
	card_number = usbbus.split("/")
	
	# Find the word id for that device
	command = "cat /proc/asound/%s/id" % card_number[3]
	id_word = subprocess.check_output(command, shell=True)
	# Delete the \n at the end
	id_word = id_word[:-1]

	# Create element in dictionary
	card_word_id_dictionary[t] = id_word
