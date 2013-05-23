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
		self.start_time = time.time()
		self.data_fn = 'cpu_%d.dat' % self.start_time
		self.html_fn = 'cpu_%d.html' % self.start_time
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
			self.data_file.close()

			cdir = os.path.dirname(__file__)

			pre  = open(os.path.join(cdir,'cpu_chart_pre.html'), 'r')
			data = open(self.data_fn, 'r')
			post = open(os.path.join(cdir,'cpu_chart_post.html'), 'r')

			html_file = open(self.html_fn, 'w')

			html_file.write( pre.read() )
			html_file.write( data.read() )
			html_file.write( post.read() )

			pre.close()
			data.close()
			post.close()

			html_file.close()

			# Open file
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