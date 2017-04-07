# Mass XSS Scanner
# Version 1.0.0
# By Brandon Hammond

# Import required modules
import os
import sys
import getopt
import core.scrape
import core.scan

# Set the version and author
__version__ = "1.0.0"
__author__ = "Brandon Hammond"

# Define the main() function
def main():
	# Function: main()
	# Purpose: Process user input and provide basic control
	
	# Attempt to call getopt.getopt()
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hvq:p:x:r:", ["help", "version", "query=", "pages=", "payloads=", "proxy="])
	except:
		# Raise an exception
		raise Exception("[E] Error processing command line arguments!")
	
	# Predefine variables with their default values
	query = None
	pages = 2
	payload_file = None
	proxy = None
	
	# Build a for loop to process arguments
	for opt, arg in opts:
		# If the -h or --help option was used
		if opt in ("-h", "--help"):
			# Display help message and exit
			print("USAGE:")
			print("\tmassxss [-h] [-v] [-q QUERY] [-p PAGES] [-x PAYLOADS] [-r PROXY]")
			print("")
			print("Scrape Google and scan the results for XSS")
			print("")
			print("REQUIRED ARGUMENTS:")
			print("\t-q, --query QUERY\tSpecify the query to scrape with")
			print("\t-x, --payloads PAYLOADS\tSpecify the payload file")
			print("")
			print("OPTIONAL ARGUMENTS:")
			print("\t-h, --help\tDisplay this message and exit")
			print("\t-v, --version\tDisplay version info and exit")
			print("\t-p, --pages PAGES\tSpecify the number of pages to scan. Default is 2")
			print("\t-r, --proxy PROXY\tSpecify proxy for scraping in type%ip:port format. Supports HTTPS and HTTP proxies")
			exit(0)
			
		# If the -v or --version option was used
		elif opt in ("-v", "--version"):
			# Display version info and exit
			print("Mass XSS Scanner")
			print("Version {}".format(__version__))
			print("By {}".format(__author__))
			exit(0)
			
		# If the -q or --query option was used
		elif opt in ("-q", "--query"):
			# Set the query
			query = arg
			
		# If the -p or --pages option was used
		elif opt in ("-p", "--pages"):
			# Set the number of pages to use
			pages = int(arg)
			
		# If the -x or --payloads option was used
		elif opt in ("-x", "--payloads"):
			# Set the payload file
			payload_file = arg	
			
		# If the -r or --proxy option was used
		elif opt in ("-r", "--proxy"):
			# Set the proxy
			proxy = arg
			
		# If an invalid option was used
		else:
			# Raise an exception
			raise Exception("[E] Invalid argument: {}!".format(opt))
			
	# Display the banner
	print("==============================")
	print("Mass XSS Scanner")
	print("==============================")
	print("[+] Query: {}".format(query))
	print("[+] Pages: {}".format(str(pages)))
	print("[+] Payloads: {}".format(payload_file))
	print("==============================")

	# Attempt to get the URLs
	try:
		urls = core.scrape.__init__(query, pages, proxy)
	except:
		# Raise an exception
		raise Exception("[E] Error scraping Google!")
		
	# Scan for XSS
	core.scan.__init__(urls, payload_file)
		
# Make sure not running as module and call main
if __name__ == "__main__":
	main()
