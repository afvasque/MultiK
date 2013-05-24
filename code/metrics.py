# coding=utf-8

import psutil
import os
import subprocess
import sys
import time
import datetime
from optparse import OptionParser
from jinja2 import Template


class Metrics:
	def __init__(self):
		# Save the current time
		self.start_time = time.time()

		# Define output filenames
		self.cpu_data_fn = 'cpu_%d.dat' % self.start_time
		self.mem_data_fn = 'mem_%d.dat' % self.start_time
		self.html_fn = 'report_%d.html' % self.start_time

		# Open output file for data
		self.cpu_data_file = open(self.cpu_data_fn, 'w')
		self.mem_data_file = open(self.mem_data_fn, 'w')

		# Capture and write data to files
		try:
			while True:
				timestamp_millis = time.time() * 1000
				cpu_p = psutil.cpu_percent(interval=float(options.interval), percpu=False) #used cpu
				mem_p = psutil.virtual_memory().percent #memory in use


				print "USED_CPU=%d \t USED_MEM=%d" % (cpu_p, mem_p)
				self.cpu_data_file.write("[%d, %d], " % (timestamp_millis, cpu_p))
				self.mem_data_file.write("[%d, %d], " % (timestamp_millis, mem_p))

		# Close data files and generate html file.
		except(KeyboardInterrupt):
			# Save the ending time
			self.end_time = time.time()

			# Close the data files
			self.cpu_data_file.close()
			self.mem_data_file.close()

			# Current directory (used for relative paths)
			cdir = os.path.dirname(__file__)

			# Open template and data files
			template_file = open(os.path.join(cdir,'metrics_template.html.jinja2'), 'r')
			cpu_data = open(self.cpu_data_fn, 'r')
			mem_data = open(self.mem_data_fn, 'r')

			# Create a new file for saving the report
			html_file = open(self.html_fn, 'w')

			# Replace the variables in the template
			template = Template(template_file.read().decode('utf-8'))
			report = template.render(
						cpu_data=cpu_data.read(),
						mem_data=mem_data.read(),
						start_time=datetime.datetime.fromtimestamp(self.start_time).strftime('%Y-%m-%d %H:%M:%S'),
						end_time=datetime.datetime.fromtimestamp(self.end_time).strftime('%Y-%m-%d %H:%M:%S'),
						total_users=options.total_users,
						interval=options.interval
						)
			report = report.encode('utf-8')

			# Write the report file
			html_file.write(report)

			# Close all used files
			template_file.close()
			cpu_data.close()
			mem_data.close()
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
parser.add_option("-i", "--interval", dest="interval", default=0.5,
                  help="set the interval for capturing the cpu usage", metavar="INTERVAL")
parser.add_option("-u", "--users", dest="total_users", default=-1,
                  help="set the number of users during the test", metavar="TOTAL_USERS")
parser.add_option("-o", "--open-graph", dest="open_graph", action="store_true",
                  help="open the graph in the default viewer when finishing")

(options, args) = parser.parse_args()

if __name__ == "__main__":
    Metrics()