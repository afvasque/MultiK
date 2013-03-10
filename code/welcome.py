#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')

import gtk
import os

class Welcome:
	# This is a callback function. The data arguments are ignored
	# in this example. More on callbacks below.
	def test_keyboards(self, widget, data=None):
		os.system("gnome-terminal -t 'Test Keyboards - MultiK' -x bash -c 'python /home/esteban/pyprojects/MultiK/code/keyboard_library_testing.py'")

	def test_audio(self, widget, data=None):
		os.system("gnome-terminal -t 'Test Sound Cards - MultiK' -x bash -c 'python /home/esteban/pyprojects/MultiK/code/audio_library_testing.py'")

	def delete_event(self, widget, event, data=None):
		# If you return FALSE in the "delete_event" signal handler,
		# GTK will emit the "destroy" signal. Returning TRUE means
		# you don't want the window to be destroyed.
		# This is useful for popping up 'are you sure you want to quit?'
		# type dialogs.
		print "delete event occurred"

		# Change FALSE to TRUE and the main window will not be destroyed
		# with a "delete_event".
		return False

	# Another callback
	def destroy(self, widget, data=None):
		gtk.main_quit()

	def __init__(self):
		# create a new window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

		# set the window title
		self.window.set_title("MultiK")

		# define window position as center
		self.window.set_position(gtk.WIN_POS_CENTER)

		# When the window is given the "delete_event" signal (this is given
		# by the window manager, usually by the "close" option, or on the
		# titlebar), we ask it to call the delete_event () function
		# as defined above. The data passed to the callback
		# function is NULL and is ignored in the callback function.
		self.window.connect("delete_event", self.delete_event)

		# Here we connect the "destroy" event to a signal handler.
		# This event occurs when we call gtk_widget_destroy() on the window,
		# or if we return FALSE in the "delete_event" callback.
		self.window.connect("destroy", self.destroy)

		# Sets the border width of the window (between controls and actual border)
		self.window.set_border_width(20)



		# Create a VBox container
		self.vbox = gtk.VBox(True, 4)



		# Creates a new button with the label "Hello World".
		self.button_test_keyboards = gtk.Button("Test Keyboards")
		self.button_test_audio = gtk.Button("Test Sound Cards")

		# When the button receives the "clicked" signal, it will call the
		# function hello() passing it None as its argument.  The hello()
		# function is defined above.
		##self.button_test_keyboards.connect("clicked", self.hello, None)
		self.button_test_keyboards.connect("clicked", self.test_keyboards, None)
		self.button_test_audio.connect("clicked", self.test_audio, None)

		# This will cause the window to be destroyed by calling
		# gtk_widget_destroy(window) when "clicked".  Again, the destroy
		# signal could come from here, or the window manager.
		## self.button.connect_object("clicked", gtk.Widget.destroy, self.window)

		# This packs the VBox into the window (a GTK container).
		self.window.add(self.vbox)
		# This packs the button into the VBox (a GTK container).
		self.vbox.add(self.button_test_keyboards)
		self.vbox.add(self.button_test_audio)
		
		# The final step is to display these newly created widgets.
		self.button_test_keyboards.show()
		self.button_test_audio.show()

		# Display the VBox
		self.vbox.show()

		# and the window
		self.window.show()

	def main(self):
		# All PyGTK applications must have a gtk.main(). Control ends here
		# and waits for an event to occur (like a key press or mouse event).
		gtk.main()



# If the program is run directly or passed as an argument to the python
# interpreter then create a Welcome instance and show it
if __name__ == "__main__":
	welcome = Welcome()
	welcome.main()

