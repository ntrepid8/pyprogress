pyprogress
==========

A command line progress indicator for python scripts

## Example Usage

	def main():
		print 'welcome to my script'
		write_progress(5)  # enter the percentage completed as an int or float
		# do more things...
		write_progress(50)
		# do more things...
		write_progress(100)  # done! 