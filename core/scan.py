# Import required modules
import requests
import urllib.parse as urlparse

# Define the scan() class
class scan(object):
	# Class: scan()
	# Purpose: Scan for XSS
	# Functions: __init__(), xss_scan()
	
	# Define the __init__() function
	def __init__(self, urls, payload_file):
		# Function: __init__()
		# Purpose: Initialize the scanner
		
		# Make sure a payload file was specified
		if payload_file == None:
			# Raise an exception
			raise Exception("[E] Payload file must be specified with -x or --payload!")
			
		# Dump everything to self
		self.urls = urls
		self.payload_file = payload_file
		
	# Define the xss_scan() function
	def xss_scan(self, url, payload_file):
		# Function: xss_scan()
		# Purpose: Scan for XSS
		
		# Attempt to open the payload file
		try:
			payload_open = open(payload_file, "r")
		except:
			# Raise an exception
			raise Exception("[E] Unable to open payload file!")
		
		# Dump the payloads to a list
		payloads = payload_open.readlines()
		
		# Parse the URL
		parsed = urlparse.urlparse(link)
		
		# Generate the seed
		seed = "".join(random.choice(string.ascii_uppercase) for i in range(5))
		
		# Obtain GET parameters and make a copy
		get_params = urlparse.parse_qsl(parsed.query)
		
		# Handle empty GET parameters
		if not get_params:
			# Yield results
			yield False
			yield None
			yield None
			return 0
			
		# Build a for loop to handle parameters and dump them into a 2D list
		for param, value in get_params:
			# Append parameter and value into param list
			param_list.append([param, str(value)])
			
		# Make a copy of the parameter list
		param_list_clone = param_lists
		
		# Build a for loop to go one parameter at a time
		for i in range(0, len(param_list)):
			# Build a for loop to handle payloads
			for payload in payloads:
				# Replace XXXXX with seed in payload
				seeded_payload = payload.replace("XXXXX", seed)
				
				# Set the payload in the current parameter
				param_list[i:1] = seeded_payload
				
				# Convert the parameter list to a dictionary
				scan_params = dict(param_list)
				
				# Set the scan headers
				scan_headers = {"User-Agent": "Mozilla/11.0"}
				
				# Attempt to get raw HTML
				try:
					raw = requests.get(link, params = url_params, headers = url_headers)
				except:
					# Raise an exception
					raise Exception("[E] Unable to get HTML for scanning!")
					
				# Check if seed is in HTML
				if seed in raw.text:
					# Yield results
					yield True
					yield param_list[i][0]
					yield payloads[p]
					return 0
					
			# Revert the paramater list back
			param_list = param_list_clone
			
		# Yield results
		yield False
		yield None
		yield None
				
# Define the __init__() function
def __init__(urls, payload_file):
	# Function: __init__()
	# Purpose: Provide basic logic for scanning
	
	# Create the scanner object
	scanner = scan(urls, payload_file)
	
	# Define vuln_sites
	vuln_sites = 0

	# Build a for loop to iterate through URLs
	for url in urls:
		# Attempt to scan for XSS
		try:
			vuln_status, param, payload = scanner.xss_scan(url, payload_file)
		except:
			# Raise an exception
			raise Exception("[E] Error scanning for XSS!")
			
		# Handle the results
		if vuln_status == True:
			# Display message
			print("[I] Vulnerable site!")
			print("[+] URL: {}".format(url))
			print("[+] Parameter: {}".format(param))
			print("[+] Payload: {}".format(payload))
			print("==============================")
			
			# Increment vuln_sites
			vuln_sites = vuln_sites + 1
			
	# Display finish message
	print("[F] Vulnerable sites: {}".format(int(vuln_sites)))
