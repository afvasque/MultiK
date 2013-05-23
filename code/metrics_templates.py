# coding=utf-8

import psutil
import os
import subprocess
import sys
import time
import datetime
from optparse import OptionParser


class Metrics:
	def __init__(self, interval):
		# Save the current time
		self.start_time = time.time()

		# Define output filenames
		self.data_fn = 'cpu_%d.dat' % self.start_time
		self.html_fn = 'cpu_%d.html' % self.start_time

		# Open output file for data
		self.data_file = open(self.data_fn, 'w')

		# Capture and write data to data file
		try:
			while True:
				timestamp_millis = time.time() * 1000
				cpu_p = psutil.cpu_percent(interval=interval, percpu=False)

				print "[%d , %d], " % (timestamp_millis, cpu_p)
				self.data_file.write("[%d, %d], " % (timestamp_millis, cpu_p))
		# Close data file and generate html file.
		except(KeyboardInterrupt):
			# Close the data file
			self.data_file.close()

			# Current directory (used for relative paths)
			cdir = os.path.dirname(__file__)

			# Open template and data files
			template_file = open(os.path.join(cdir,'metrics_template.html'), 'r')
			data = open(self.data_fn, 'r')

			# Create a new file for saving the report
			html_file = open(self.html_fn, 'w')

			# Replace the variables in the template
			template = template_file.read()
			report = template % { 'data': data.read() }

			# Write the report file
			html_file.write(report)

			# Close all used files
			template_file.close()
			data.close()
			html_file.close()

			# Show created file in the default viewer
			if (options.open_graph):
				html_full_path = os.path.join( os.getcwd(), self.html_fn )
				if sys.platform == 'linux2':
				    subprocess.call(["xdg-open", html_full_path])
				else:
				    os.startfile(html_full_path)











# For command-line arguments
parser = OptionParser()
parser.add_option("-i", "--interval", dest="interval", default=0.1,
                  help="set the interval for capturing the cpu usage", metavar="INTERVAL")
parser.add_option("-g", "--graph-update", dest="graph_update", default=1.5,
                  help="set the interval for refreshing the graph", metavar="INTERVAL")
parser.add_option("-o", "--open-graph", dest="open_graph", action="store_true",
                  help="open the graph in the default viewer when finishing")

(options, args) = parser.parse_args()

if __name__ == "__main__":
    Metrics(float(options.interval))